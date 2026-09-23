class Ageexception(Exception):
    pass

age = int(input("Enter your age: "))
print(age)


if age < 16:
        raise Ageexception("you are not eligible for vote")
else:
      ('you can vote ')