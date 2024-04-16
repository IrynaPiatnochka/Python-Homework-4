import random


days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
meals_time = ["Breakfast", "Lunch", "Dinner"]
meals = ["Shepherd Pie", "Pot Pie","Meatloaf","Pork Chops","Pan-Baked Bell Pepper","Fish","Kabobs","Meatballs","Sloppy Joes","Hot Dogs","Burgers","Steak","Baked Ham","Grilled Chicken Breasts","Roasted Whole Chicken","Ribs","Pork Loin","Boiled Shrimp","Chicken","Rice Casserole","Beef Roast","Macaroni Casserole"]
for day in days:
    for time in meals_time:
        r = random.randint(0, len(meals))
        print(day, "for", time, "I'm having", meals[r])