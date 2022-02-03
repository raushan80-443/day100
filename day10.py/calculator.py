
def add(n1,n2):
    return f"{n1 + n2} "



def subtract(n1,n2):
    return f"{n1 -n2} "

def multiply(n1,n2):
    return f"{n1*n2}"

def divide(n1,n2):
    return f"{n1/n2}"

sign = {
"+" : "add",
"-":"subtract",
"*":"multiply",
"/":"divide"
}


num1 = int(input("write 1st number"))
for calculate in sign:
    print(calculate)
operation = input("what do you want to do")
num2 =int(input("write 2nd number"))

functions = sign[operation]
print(functions)
def check(functions):
    signature = ""
    if functions == "add":
        work = add(num1,num2)
        signature = functions
  
        
    elif functions == "subtract":
        work = subtract(num1,num2)
             
        signature = functions

    elif functions == "multiply":
        work = multiply(num1,num2)
        signature = functions
       
    elif functions == "divide":
        work = divide(num1,num2)
        signature = functions
    else: 
        print(f"you have to select from this signs {calculate}: ")
    
    print(f"{num1} {signature} {num2} = {work}")


check(functions)




