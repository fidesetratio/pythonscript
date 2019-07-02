height = input()

if int(height) <= 1:
    print("you cannot ride")
elif int(height) >=2:
    print("you can ride but there is a reason we give you a warning")
else:
    print("You can ride")



print("Please input your age?")
age = int(input())
print("Pleas input your sex")
sex = input()

if age <= 10 and sex == 'M':
    print("Boy")
elif (age >=10 and sex == 'M'):
    print("Man")
elif (age <= 10 and sex == 'F'):
    print("Girl")
elif (age >= 10 and sex == 'F'):
    print("Women")
else:
    print("We don't know you")
