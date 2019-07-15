#! /usr/bin/python

"""
@Name of Project:
@Author
@Date:
@Summary
@Status:

"""

from ctypes import *
from debugger_defines import *

kernel = windll.kernel32

#What do i need for my debugger?
# list everything i need in comments then write the code
# I need to define a class for my Debugger
class Debugger():
	def __init__(self):
		pass

# I need a function to load my application
	def load(self, path_to_exe):	

#Do i need anything before this? What about the Flags?
		flag = CREATE_NEW_CONSOLE

#What about the variables to start up my two defines?
		startupinfo = Startupinfo()
		process_information = Process_information()

#I need to call "CreateProcessA" from win(windll.kernel32)
#If it doesnt work then show me why?(Error
		if kernel.CreateProcessA(path_to_exe,
                                None,
                                None,
                                None,
                                None,
                                flag,
                                None,
                                None,
                                byref(startupinfo),
                                byref(process_information)):
                        print("The Process ID is: %d\n" % process_information.dwProcessId)
		else:
                        print("Something is not working...%08x." % kernel.GetLastError())
