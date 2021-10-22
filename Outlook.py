import ctypes

def pop(msg):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, msg, 'Window title', 0x40000)