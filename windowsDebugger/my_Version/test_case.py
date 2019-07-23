#! /usr/bin/python

"""
//@File Name: test_cases.py
//@Summary: Example Windows Debugger based on Gray Hat Python
//@Author MaskedFox
//@Date: July, 2019
//@Email: iammaskedfx@gmail.com
//@Credits: Gray Hat Python
//@Status: On Going
"""

import my_debugger

path = "C:\\WINDOWS\\system32\\calc.exe"
debugger = my_debugger.Debugger()
debugger.load(path)

