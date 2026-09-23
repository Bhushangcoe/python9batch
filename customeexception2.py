class MarkError(Exception):
    pass

marks=int(input("enter marks:"))
if(marks<0 or marks>100):
    raise MarkError("invalid marks")
else:
    print("marks=",marks)

print("result declared")    
