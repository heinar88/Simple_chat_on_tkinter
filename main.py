import socket
import sys
from threading import Thread
from gui_core import *
from tkinter.messagebox import showwarning


class Client(tk.Tk):
    def __init__(self):
        super().__init__()
        self.nickname = None
        self.server_ip = None
        self.server_port = None
        self.client_socket = None
        self.first_click = True
        self.title('Chat')
        self.modal_win = ConfigModalWindow(self.set_server_params, self)
        self.msg_in_input_box = tk.StringVar()
        self.msg_in_input_box.set('Input you message here')
        self.message_box = MessageBox(self)
        self.input_box = MessageInputField(self, self.msg_in_input_box)
        self.send_button = SendButton(self, 'Send', self.send_msg)
        self.clear_button = ClearButton(self, 'Clear', self.clear)
        self.protocol("WM_DELETE_WINDOW", self.close_app)
        self.set_event_handlers(self.clear, self.send_msg)
        self.config(padx=3, pady=3)
        self.mainloop()

    def create_modal_win_for_conf(self):
        self.modal_win = ConfigModalWindow(self.set_server_params, self)

    def create_client_sock(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.connect((self.server_ip, self.server_port))
        Thread(target=self.print_message).start()

    def print_message(self, event=None):
        while True:
            user_response = self.client_socket.recv(1024)
            if user_response:
                user_msg = user_response.decode('utf-8')
                user_nickname = user_msg.split()[0]
                user_data = user_msg[user_msg.rfind('>') + 1:]
                self.message_box.output_place.insert(tk.END, f'{user_nickname} >>> {user_data}')
            else:
                break

    def set_server_params(self):
        if all([self.modal_win.entry_ip.get(),
                self.modal_win.entry_port.get(), self.modal_win.entry_nickname.get()]):
            self.server_ip = str(self.modal_win.entry_ip.get())
            self.server_port = int(self.modal_win.entry_port.get())
            self.nickname = str(self.modal_win.entry_nickname.get())
            self.create_client_sock()
            self.modal_win.destroy()
        else:
            showwarning('Not valid data in field', 'Fill all field')

    def send_msg(self, event=None):
        if self.input_box.get():
            my_msg = f'{self.nickname} >>> {self.input_box.get()}'
            self.client_socket.send(bytes(my_msg, 'utf-8'))
            self.message_box.output_place.insert(tk.END, my_msg)
            self.msg_in_input_box.set('')

    def clear(self, event=None):
        self.input_box.delete(0, 'end')

    def close_app(self):
        if self.client_socket:
            self.client_socket.close()
        self.quit()

    def set_first_click_status(self):
        if self.first_click:
            self.input_box.delete(0, "end")
            self.first_click = False

    def set_event_handlers(self, clear_func, send_func):
        self.input_box.bind('<FocusIn>', clear_func)
        self.input_box.bind('<Return>', send_func)


if __name__ == '__main__':
    sys.stderr = open('error.txt', 'w')
    Client()
