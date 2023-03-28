#-----------------------
#Dictionary and Grocery
#Aiden Krahn
#March 27
#-----------------------
#--Define Dictionaries
#name of item and price
items = {}
destination = []
play = True
while play == True:
    addthing = input("What do you want?  ")
    price = int(input("What price is it?  "))
    howmany = int(input("How many?  "))
    whatstore = int(input("""What store is it in?
1. Superstore
2. General Store
3. Home Depot
4. Drug Store
5. Flower Shop
6. Grocery Store
- """))
    if whatstore == 1:
        destination.append("Super Store")
        
    elif whatstore == 2:
        destination.append("General Store")
        
    elif whatstore == 3:
        destination.append("Home Depot")
        
    elif whatstore == 4:
        destination.append("Drug Store")
        
    elif whatstore == 5:
        destination.append("Flower Shop")
        
    elif whatstore == 6:
        destination.append("Grocery Store")
        
    items.update({addthing: price * howmany})
    print(items)
    something = input("Stop there?(y/n)  ")
    if something == "y":
        break

    elif something == "n":
        play = True
total = sum(items.values())
print("You need to get-", items)
print("It will cost-", total)
print("You need to go-", destination)


