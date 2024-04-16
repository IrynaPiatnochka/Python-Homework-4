while (True):
    x = input("Guess what is my favorite color?")
    if (x == 'red'):
        print("You got it, it's ", x)
        break
    else: 
        print("No, it's not ", x)
        


i = 1
while (i < 5):
    print("Iteration #", i)
    i = i + 1
