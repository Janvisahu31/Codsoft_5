
import random


char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
      "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
      "0","1","2","3","4","5","6","7","8","9","!","@","#","$"]

password=[]
n=int(input("Enter the length of the password"))

for i in range(1,n+1):
        s=random.choice(char)
        password.append(s)

print("".join(password))
