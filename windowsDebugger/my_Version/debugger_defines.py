#! /usr/bin/python

"""
//@File Name: debugger_defines.py
//@Summary: Example Windows Debugger based on Gray Hat Python
//@Author MaskedFox
//@Date: July, 2019
//@Email: iammaskedfx@gmail.com
//@Credits: Gray Hat Python
//@Status: On Going
"""


from ctypes import *

# Windows defines in Ctypes
DWORD = c_ulong 
LPSTR = c_char
WORD = c_uint
LPBYTE = c_ubyte
HANDLE = c_void_p
BOOL = c_bool

# Defining Flags for Process Creation Flags
CREATE_NEW_CONSOLE = 0X00000010
DEBUG_PROCESS = 0X00000001

# Defining STARTUPINFO
class Startupinfo(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpRsereved", LPSTR),
        ("lpDesktop", LPSTR),
        ("lpTitle", LPSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
        ]
#Defining Process_information
class Process_information(Structure):
    _fields_= [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
        ]
#Defining OpenProcess
class Open_process(Structure):
	_fields_=[
		("dwDesiredAccess", DWORD),
		("bInheritHandle", BOOL),
		("dwProcessId", DWORD),
		]
#Defining DebugActiveProcess
class Debug_active_process(Structure):
	_fields_= [
		("dwProcessId", DWORD),
		]
#Defining WaitForDebugEvent
class Wait_for_debug_event(Structure):
	_fields_= [
		("lpDebugEvent", LPDEBUG_EVENT),
		("dwMilliseconds", DWORD),
		]
#Defining ContinueDebugEvent
class Continue_debug_event(Structure):
	_fields_= [
		("dwProcessId", DWORD),
		("dwThreadId", DWORD),
		("dwContinuesStatus", DWORD),
		]



