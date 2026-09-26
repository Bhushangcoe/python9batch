class MarkError(Exception):
    def __init__(self,marks):
        super().__init__()
        self.marks=marks
        print('your marks',self.marks,'enter  marks between 0-100')

marks=int(input("enter marks:"))
if(marks<0 or marks>100):
    raise MarkError("invalid marks")
else:
    print("marks=",marks)

print("result declared")    
