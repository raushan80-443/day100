print("""
 _ __ __ _ (_)
| '__/ _` || |
| | | (_| || |
|_|  \__,_|/ |
         |__/""")
a =[]

B  = "thisisawesom"
for letter in range(len(B)):
    a += "_"  
print(a)
guess = input("guess a letter: ")
for pattern in range(len(B)):
    print(pattern)