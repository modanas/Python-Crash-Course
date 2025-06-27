# try with finally block : finally block will be executed no matter what

def main():
   try:
    a = int(input("Enter a number : "))
    print(a)

   except Exception as e:
    print(e)

   finally:
     print("Finally block will be executed")

main()