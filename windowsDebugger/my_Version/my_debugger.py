#! /usr/bin/python

"""
@Name of Project:
@Author
@Date:
@Summary
@Status:

"""

from ctypes import *
from my_debugger_defines import *

win = windll.kernel32

class Debugger():
	def __init__(self):
		pass
	
#What do i need for my debugger?
# list everything i need in comments then write the code

# i need a function to load my application
	def load(self, path_to_exe):
		
#Do i need anything before this? What about the Flags?
		flag = CREATE_NEW_CONSOLE
	
		startupinfo = Startupinfo()
		processinformation = Process_information()
#I need to call CreateProcess from win(windll.kernel32)
		if win.CreateProcessA(path_to_exe,
			None,
			None,
			None,
			None,
			flag,
			None,
			None,
			startupinfo,
			process_information)
			print("The Process ID is: %d\n", processinformation.dwPrceossId)
		else print("Something is not working...")
	
			
		

