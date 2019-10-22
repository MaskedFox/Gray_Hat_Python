Within this part of the book we start using PYDBG, however book doesn't tell you how to install it, etc
To avoid you wasting time like i did i have attached all the necessary dependencies for it to work under the folder `Tools_to_install`.

Once inside the folder you ll see the following programs:

```
InmunityDebugger_1_85_setup.exe
paimei-master
python-2.7.16.msi
```
Step 1:
Install Python2.7.16.msi (32 bit)

Step 2:
go into the folder `paimei-master` from the command line and run
the following command:
```
python setup.py install
```
The above should install PYDBG and all its dependencies, since i used the PDBG from original Github plus a working PYDASM file and put it within the PYDBG folder inside the `paimei-master` folder.
That's all you need for PYDBG to work =)

Step 3: install Inmunity Debugger if you haven't yet

SIDE NOTE:
The printf_random works, but at the books the describes it, however buffer_overflow.py and access_violation_handler.py work as suppose to per the book. Just fantastic how all comes together! 
