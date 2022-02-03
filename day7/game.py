from random import random



list = ["saj","shivam","shyam"]
import random
random_guess = random.choice(list)
word =len(random_guess)

display = []
for _ in range(word):
    display += "*" 
print(display)
user = input("guess my friend name: ")
for possition in random_guess:
    for letter in possition:
        print(letter)
    print(letter)
    if user == letter:
       for display in possition:
           display += letter
       
print(display)
            
     
    

        

  
           
