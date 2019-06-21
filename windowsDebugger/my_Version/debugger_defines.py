#! /usr/bin/python

"""
@Name of Project:
@Author
@Date:
@Summary
@Status:

"""

import ctypes *

# Windows defines in Ctypes

DWORD = c_ulong 
LPSTR = c_char
WORD = c_uint
LPBYTE = c_ubyte
HANDLE = c_void_p

# Defining Flags for Process Creation Flags

CREATE_NEW_CONSOLE = 0X00000010
DEBUG_PROCESS = 0X00000001

# Defining STARTUPINFO

Class Startupinfo(Structure):
    __fields__ = 
        [
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
        ("dwFlags" DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
        ]

Class Process_information(Structure):
    __Fields__=
        [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
        ]



