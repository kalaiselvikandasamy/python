determine if a Python shell is executing in 32bit or 64bit mode on OS.
import struct
print(struct.calcsize("p")*8)
