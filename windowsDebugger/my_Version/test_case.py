#! /usr/bin/python

"""
@Name of Project:
@Author
@Date:
@Summary
@Status:

"""
from debugger_defines import *
from my_debugger import *
from ctypes import *

path = "C:\\WINDOWS\\system32\\calc.exe"
debugger = my_debugger.Debugger()
debugger.load(path)

