import re
import string

f =  open("Tag 2/input.txt", "r")

x = re.findall("mol([],[])", f)
print(x)