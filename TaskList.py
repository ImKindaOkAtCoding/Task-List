print("Welcome To Your Task List")
print("Would You Like To Add Anything? (yes/no)")
addanything = input(": ")

if addanything == "yes":
    print("What Is It?")
    whatisit = input(": ")
    print("Would You Like To Set A Time Goal? (yes/no)")
    timegoalask = input(": ")

    if timegoalask == "yes":
        print("(Minutes/Hours/Days)")
        timeunit = input(": ")
        print()
        print("How Many:",timeunit,)
        howmanytimeunit = input(": ")
        print("Here Is Your Current Task List")
        print("Task:",whatisit,": Time:",howmanytimeunit,timeunit)
    
    else:
        print("Here Is Your Current Task List:")
        print(":",whatisit)

else:
    print("Ok Exiting!")