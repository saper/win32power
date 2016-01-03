
# This is a public domain code

def displayOff():
	from ctypes import windll
	windll.user32.SendMessageA(0xffff, 0x0112, 0xf170, 2)

def displayOn():
	from ctypes import windll
	windll.user32.SendMessageA(0xffff, 0x0112, 0xf170, -1)
