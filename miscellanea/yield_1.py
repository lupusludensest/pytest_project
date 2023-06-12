# A Python program to show return statement

class Test:
    def __init__(self):
        self.str = "GeeksForGeeks"
        self.x = "Shubham Singh"

# This function returns an object of Test
def fun():
    return Test()

# Driver code to test above method
t = fun()
print(t.str)
print(t.x)