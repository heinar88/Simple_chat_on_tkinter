import tkinter as tk
from tkmacosx import Button


class MessageBox(tk.Frame):
    """ This class creates a frame in which there will be a class for output messages and a scrollbar class """
    def __init__(self, root_frame=None):
        super().__init__(root_frame)
        self.scrollbar = tk.Scrollbar(self)
        self.config(padx=3, pady=3)
        self.output_place = tk.Listbox(self,
                                       height=10,
                                       width=60,
                                       bd=3,
                                       relief=tk.GROOVE,
                                       yscrollcommand=self.scrollbar.set)
        self.output_place.config(font='SanFrancisco 14')
        self.scrollbar.config(command=self.output_place.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_place.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.pack(expand=tk.YES, fill=tk.BOTH)


class MessageInputField(tk.Entry):
    """ This class creates a window for user input """
    def __init__(self, root_frame=None, textvariable=None):
        super().__init__(root_frame, textvariable=textvariable)
        self.config(bg='white', fg='black', width=60, bd=3, relief=tk.GROOVE)
        self.pack(side=tk.LEFT, fill=tk.Y, expand=tk.YES)

    def set_handlers(self, clear_func=None, send_func=None):
        self.bind('<FocusIn>', clear_func)
        self.bind('<Return>', send_func)


class SendButton(Button):
    def __init__(self, root_frame=None, text="Send", command=None):
        super().__init__(master=root_frame, text=text, command=command)
        self.config({'bg': 'white', 'text': 'Send', 'height': 30, 'width': 90})
        self.pack()


class ClearButton(Button):
    def __init__(self, root_frame=None, text="Clear", command=None):
        super().__init__(master=root_frame, text=text, command=command)
        self.config({'bg': 'white', 'text': 'Clear', 'height': 30, 'width': 90})
        self.pack()


class ConfigModalWindow(tk.Toplevel):
    """ This class creates a modal window on top of the main program window,
        the form in this window requests data for the configuration of the connection to server """
    def __init__(self, click_on_accept, main_window):
        super().__init__()
        self.title('Connection configure')
        self.label_ip = tk.Label(self, text='Input server IP')
        self.entry_ip = tk.Entry(self)
        self.label_port = tk.Label(self, text='Input server port')
        self.entry_port = tk.Entry(self)
        self.label_nickname = tk.Label(self, text='Enter you nickname')
        self.entry_nickname = tk.Entry(self)
        self.button = tk.Button(self, text='Accept', command=click_on_accept)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", main_window.quit())
        self.pack_widgets()

    def pack_widgets(self):
        self.label_ip.grid(column=0, row=0, padx=3, pady=3)
        self.label_port.grid(column=0, row=1, padx=3, pady=3)
        self.entry_ip.grid(column=1, row=0, padx=3, pady=3)
        self.entry_port.grid(column=1, row=1, padx=3, pady=3)
        self.label_nickname.grid(column=0, row=2, padx=3, pady=3)
        self.entry_nickname.grid(column=1, row=2, padx=3, pady=3)
        self.button.grid(column=1, row=3, padx=3, pady=3)
