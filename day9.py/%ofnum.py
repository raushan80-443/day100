


def ofnumber(number,prcentagee):
    answer = number * prcentagee/100
    print(f"the answer is {answer}")
no = True
while no == True:
    usernumber = int(input("write the number: "))
    percentage = int(input("write the %: "))
    ofnumber(usernumber,percentage)
   
    ask = input("want to run again \ny for yes n for no: ")
    if ask == "yes":
        continue
    else:
        no = False
        print("bye see you soon")

    ofnumber(usernumber,percentage)
    