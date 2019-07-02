

a = [1,2,3,4,5,6,7,8]

def isOdd(x):
    return x%2 != 0

def ditambahkan(x):
    return x+100

t = list(filter(isOdd,a))

d = list(map(ditambahkan,a))
print("use of the map = list(map(ditambahkan,a)):")
print(d)

print("use of is odd = list(filter(isOdd,a)):")
print(t)


def func(x):
    return x+5

func2 = lambda x:x+5

print("without lamda :",func(10))
print("with lamda:",func2(10))

def func5(x,y):
    return x+y

func6 = lambda x,y:x+y

print("without lamda",func5(5,4))
print("with lamda",func6(5,4))


print("--------------------------------------------------")




g = list(map(lambda x:x+1,a))

print(g)