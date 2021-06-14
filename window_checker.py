import ctypes


class Window_checker:
	black_list=[
	'Menedżer zadań Windows',
	'Process Explorer',
	'sysinternals',
	'Wireshark'
	]
	
	white_list=[
	'Chrome',
	'Mozilla',
	'Firefox',
	'IceWeasel',
	'Opera',
	]
	windows=[]

	def __init__(self):
		self.windows = self.get_windows()
	
	#Checks if browser is opened 
	def is_browser(self):
		#refresh windows list
		self.windows = self.get_windows()

		#check white list
		for i in self.windows:	
			for j in self.white_list:
				if str.__contains__(self.cut_bad_chars(i),self.cut_bad_chars(j)):
					return True
		return False
		
		
	#Checks if engineering tools are opened
	def is_tools(self):
		#refresh windows list
		self.windows = self.get_windows()

		#check black list
		for i in self.windows:	
			for j in self.black_list:
				if str.__contains__(self.cut_bad_chars(i),self.cut_bad_chars(j)):
					return True
		return False			
	#Prints list of windows				
	def print_windows(list):
		for i in list():
			print(i)

	#cut special chars
	def cut_bad_chars(self,str):
		result=""
		for i in str:
			if ord(i)<128:
				result+=i
		return result
			
	#Creates a list of opened windows
	def get_windows(self):
		user32=ctypes.windll.user32
		EnumWindows = user32.EnumWindows
		EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
		GetWindowText = user32.GetWindowTextW
		GetWindowTextLength = user32.GetWindowTextLengthW
		IsWindowVisible = user32.IsWindowVisible
		EnumChildWindows = user32.EnumChildWindows

		handler_taskmanager=""
		handler_control=""
		
		def enum_windows(hwnd, lParam):
			global handler_taskmanager
			global handler_control
			
			if IsWindowVisible(hwnd):
				length = GetWindowTextLength(hwnd)
				buff = ctypes.create_unicode_buffer(length + 1)
				GetWindowText(hwnd, buff, length + 1)
				self.windows.append(self.cut_bad_chars(buff.value))
			return True
		EnumWindows(EnumWindowsProc(enum_windows), 0)
		return self.windows
		
sender = Window_checker()
print("Browser: " + str(sender.is_browser()))
print("Tools: " + str(sender.is_tools()))

