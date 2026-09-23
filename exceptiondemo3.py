print("welcome to files")
print('hello')
try:
    file=open("data.text","r")
    d=file.read()
    print(d)
except:
    print("file not found") 

print("program end")       