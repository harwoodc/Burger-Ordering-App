print("Welcome to Burger Emmporium!")

size = input("What size burger do you want? S, M, or L ")

add_bacon = input("Do you want bacon? Y or N? ")

add_cheese = input("Do you want to order cheese? Y or N? ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_bacon == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if add_cheese == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
        
print(F"Your final bill is ${bill}.")