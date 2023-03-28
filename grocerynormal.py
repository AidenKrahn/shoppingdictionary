#-----------------------
#Dictionary and Grocery
#Aiden Krahn
#March 27
#-----------------------
#--Define Dictionaries
prices = {}
items = []
whtstre = {}

play = True
while play == True:
    addthing = input("What do you want?  ")
    price = int(input("What price is it?  "))
    whatstore = input("What store is it in?  ")

    prices.update({addthing: price})
    whtstre.update({addthing: whatstore})
    items.append(addthing)
    print(items)
    print(prices)
    print(whtstre)
    something = input("Stop there?(y/n)  ")
    if something == "y":
        break

    elif something == "n":
        play = True

