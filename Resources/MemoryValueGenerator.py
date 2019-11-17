# -*- coding: None -*-

# Created by: Mihai Razvan-Viorel
#
# Email: razvan.mihai@mta.ro

''' Asociated common cathode code to represent 0-9 digits'''
digits = ('7E','30','6d','79','33','5b','5f','70','7f','7b')

''' Write to memmory locations 0-1023 for unsigned operations. Result displayed on 4 7-segment displays'''
f = open("_27C64_mem.bin", "w")
for i in range(256):
    f.write(digits[i%10].decode("hex"))
for i in range(256):
    f.write(digits[(i/10)%10].decode("hex"))
for i in range(256):
    f.write(digits[i/100].decode("hex"))
for i in range(256):   
    f.write('00'.decode("hex"))

''' Write to memmory locations 1024-1791 for signed operations. Result displayed on 4 7-segment displays'''
for i in range(0,128):
    print i
    f.write(digits[i%10].decode("hex"))
for i in range(128,0,-1):
    print i
    f.write(digits[i%10].decode("hex"))
    
for i in range(0,128):
    f.write(digits[(i/10)%10].decode("hex"))
for i in range(128,0,-1):
    f.write(digits[(i/10)%10].decode("hex"))

for i in range(0,128):
    f.write(digits[i/100].decode("hex"))
for i in range (128,0,-1):
    f.write(digits[i/100].decode("hex"))
    
for i in range(0,128):
    f.write('00'.decode("hex"))
for i in range (128,0,-1):
    f.write('01'.decode("hex"))
f.close()

#open and read the file after the appending:
f = open("_27C64_mem.bin", "r")
print(f.read())
