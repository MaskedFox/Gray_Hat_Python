"""
//@File Name: my_test.py
//@Summary: Example Windows Debugger from Gray Hat Python
//@Author MaskedFox
//@Date: June 04, 2019
//@Email: iammaskedfx@gmail.com
//@Credits: Gray Hat Python
//@Status: On Going
"""

import my_debugger

debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to : ")
debugger.attach(int(pid))
debugger.detach()




