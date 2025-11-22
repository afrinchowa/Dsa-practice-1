# byte is a function and it is immutable and it returns an object 
# bytearray is mutable .
# both range is 0 -256
# 
#  image compressing use

modlist =[1,2,3,45,5,6,7,8,8,9]
b=bytes(modlist)

print(type(b))


# bytearray
modlist1 =[1,2,3,45,5,6,7,8,8,9]
b1=bytearray(modlist1)
b1[0]=10
print(b1[0])
print(b1[1])

