"""
//@File Name: my_debuffer_defines.py
//@Summary: Example Windows Debugger from Gray Hat Python
//@Author MaskedFox
//@Date: June 04, 2019
//@Email: iammaskedfx@gmail.com
//@Credits: Gray Hat Python
//@Status: On Going
"""

from ctypes import *

# Let's map the Microsoft types to ctypes for clarity
WORD = c_ushort
DWORD = c_ushort
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

#Constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

#Structures for CreateProcessA() function
class STARTUPINFO(Structure):
    _fields_ = [
            ("cb",  DWORD),
            ("lpReserved",  LPTSTR),
            ("lpDesktop",   LPTSTR),
            ("lpTitle",     LPTSTR),
            ("dwX",         DWORD),
            ("dwY",         DWORD),
            ("dwXSize",     DWORD),
            ("dwYSize",     DWORD),
            ("dwXCounterChars", DWORD),
            ("dwYCounterChars", DWORD),
            ("dwFlags", DWORD),
            ("wShowWindow",    WORD),
            ("cbReserved2",    WORD),
            ("lpReserved2", LPBYTE),
            ("hStdInput", HANDLE),
            ("hStdOutput", HANDLE),
            ("hStdError",    HANDLE),
        ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess:", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]


