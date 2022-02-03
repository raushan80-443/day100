def percentage(score,total_score):
    percentage = score *100 / total_score
    print(f"{percentage}%")


a = 0
while a == 0:
    score = int(input("write your number: "))
    total_score = int(input("write your total number: "))
    percentage(score,total_score)
    ask = input("\nwant to calculate again \nyes or no: ")
    if ask == "yes":
        continue
    else:
        a == 1
        break



