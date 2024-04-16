import random

items = ["Shepherd Pie", "Pot Pie","Meatloaf","Pork Chops","Bell Pepper","Fish","Kabobs","Meatballs","Sloppy Joes","Hot Dogs","Burgers","Steak","Baked Ham","Grilled Chicken Breasts","Roasted Whole Chicken","Ribs","Pork Loin","Boiled Shrimp","Chicken","Rice Casserole","Beef Roast","Macaroni Casserole"]
a = random.choice(items)
print(a)
while (True):
    y = input("Guess the meal we are going to have for dinner today!")
    if a == y:
        print("You got it, it's", a)
    else: 
        print("No, it's not.")