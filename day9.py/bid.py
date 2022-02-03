
from turtle import clear


bid = {}
def store_in_dir(name,value):
    bid[name]= value
    # print(bid)

def winner(dictoinary):
    max = 0
    winner = ""
    for check in dictoinary:
        if dictoinary[check] > max:
            max = dictoinary[check]
            winner = check
    print(f"the winner is {winner} and his bid was{max} ")

no = 0

while no ==0:
    namea = input("please write your name")
    valuea = int(input("what is your bid fo redmi note 5"))
    store_in_dir(namea,valuea)
    person = input("want to bid for  my note 5 phone \n yes or no ")
    if person == "yes":
        clear()
        continue
    else:
        winner(bid)
        no = 2


