# calculator in Python(v0.4)
def Add(num1, num2):
	return num1 + num2

def Sub(num1, num2):
	return num1 - num2
def Square_Root(number):
    return number **0.5
# main
number = int(input("Enter a number: "))
res = Add(5, 3)
print(res)
print(Sub(5,3))
print("The square root of given number", number, "is", Square_Root(number))