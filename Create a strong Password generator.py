#python Projects:
#_1. Create a strong Password generator:


import string
import random    

List1 = list(string.ascii_uppercase)
List2 = list(string.ascii_lowercase)
List3 = list(string.digits)
List4 = list(string.punctuation)
Char_no = input("Enter the No. of characters: ")

while True:
    try:
        Char_no = int(Char_no)
        if Char_no < 6:
            print("You need at least 6 characters to create your Password!!")
            Char_no = input("Please re-enter No. of characters: ")
        else:
            break
    except:
      print("Please, enter numbers only !")
      Char_no = input("Please re-enter No. of characters: ")
    
random.shuffle(List1)
random.shuffle(List2)
random.shuffle(List3)
random.shuffle(List4)

part1 = round(Char_no * 0.3) # 0.3 ==> 30% uppercase and 30% lowercase
part2 = round(Char_no * 0.2) # 0.2 ==> 20% digits and 20% sympoles

#print(List4)
Password = []
for i in range(part1):
    Password.append(List1[i])
    Password.append(List2[i])
for i in range(part2):
    Password.append(List3[i])
    Password.append(List4[i])
    
random.shuffle(Password)    
print(Password)
Password="".join(Password[0:]) #join to create a password not in list e.g.: "7A<bW5q/rO"
print(Password)     
    

