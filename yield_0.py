# Python3 code to demonstrate yield keyword

# Use of yield
def printresult(String):
    for i in String:
        if i == 'e':
            yield i

# initializing string
String = "GeeksforGeeks"
ans = 0
print(f"The number of 'e's in word is : ", end = "")
String = String.strip()

for j in printresult(String):
    ans += 1

print(ans)
