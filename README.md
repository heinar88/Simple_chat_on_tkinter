<h1 align="center">Simple Chat on Python</h1>

___
### What is it 
___
<p>This application is a simple chat written using sockets that support connection on TCP  protocol.
Client GUI implemented on the library <b>tkinter</b> included in the standard library Python.</p>

<p>All work with network connections is implemented by the functions of the Python standard library, used two modules:</p>
<ul>
    <li><b>asyncio</b></li>
    <li><b>socket</b></li>
</ul>
<p>Also, used modules from the standard library:</p>
<ul>
    <li><b>os</b></li>
    <li><b>sys</b></li>
</ul>
<p>This code is written in python version 3.9.9, but it will work on python version 3.8 and higher.
All additional dependencies you can be found in <b>requirements.txt</b></p>

___
### Structure and installation
___

<p>This application consists of three modules:</p>
<ul>
    <li><b>async_server.py</b></li>
    <li><b>gui_core.py</b></li>
    <li><b>main.py</b></li>
</ul>
<p>The <b>async_server</b> module is started with the parameters
<b>-p int</b> and <b>-ip int</b> where it is specified IP-address
and port on host.</p>  

<p>The <b>gui_core</b> module contains classes for creating widget objects.</p>
<p>The <b>main.py</b> module combines network and GUI interaction and handle events users interface.
</p>

<p>For start work server use:</p>

```
python3 async_server -ip [your IP ] -p [your port]
```
if you do not specify startup options, the server will start on
<b>localhost</b> and <b>5000 port</b>.

<p>For start work GUI-client use:</p>

```
python3 main.py
```
<p>For install  dependencies, use:</p>

```
pip install -r requirements.txt
```
