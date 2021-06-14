# -*- coding: utf-8 -*-
import ctypes

user32=ctypes.windll.user32
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = user32.GetWindowTextW
GetWindowTextLength = user32.GetWindowTextLengthW
IsWindowVisible = user32.IsWindowVisible
EnumChildWindows = user32.EnumChildWindows

handler_taskmanager=""
handler_control=""

black_list=[
"Menedżer zadań Windows",
"Process Explorer",
"sysinternals",
]
white_list=[


]

windows=[]
def foreach_window(hwnd, lParam):
	global handler_taskmanager
	global handler_control
	
	#if IsWindowVisible(hwnd):
	length = GetWindowTextLength(hwnd)
	buff = ctypes.create_unicode_buffer(length + 1)
	GetWindowText(hwnd, buff, length + 1)
	windows.append(buff.value.encode('utf-8'))
	return True

EnumWindows(EnumWindowsProc(foreach_window), 0)

for i in windows:
	print (i)

#for i in windows:	
#	for j in black_list:
#		if str.__contains__(i,j):
#			print(i)
