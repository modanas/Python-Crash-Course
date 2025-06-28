# program to  generate multiplication tables from 2 to 20 and write it to different files
def generateTable(n) :
   table = ""
   for i in range(1, 11) :
    table += f"{n} X {i} = {n * i}\n"

   with open(f"C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\tables\\table_of_{n}.txt", "w") as f :
     f.write(table)
    

for i in range(2, 21) :
  generateTable(i)