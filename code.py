print("What day is it?")
day = input() # user_input for day
print("Did you work out yesterday?")
ans = input() #user input on whether or not they worked out the day before
if ans=="yes" or ans == "YES":
    if day=="Monday" or day=="Thursday":
        print("Time for chest and Tricepts!")
    elif day == "Tuesday" or day=="Friday":
        print("It's Back and Bicepts time!")
    elif day=="Wednesday" or day=="Saturday":
        print("LEG DAY!!")
    elif day== "Sunday":
        print("Lets go for a run!")
    else: #for if the user said no
        print("What day was yesterday?")
day = input()
if day == "Monday" or day == "Thursday":
    print("Chest and Tricepts but go a little harder!")
elif day == "Tuesday" or day=="Friday":
    print( "Back and Bicepts but put a little more into this one!")
elif day == "Wednesday" or day=="Saturday":
    print( "Time to SQUAT!")
else:
    print( "Chest and Tricepts with a nice run after!")
