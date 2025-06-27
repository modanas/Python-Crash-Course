# try with else block : if try block is successful then else block will be executed

try:
 a = int(input("Enter a number : "))
 print(a)

except Exception as e:
 print(e)

else:
 print("Nothing went wrong")