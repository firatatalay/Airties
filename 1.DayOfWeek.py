days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def day_of_week(S, K):
    #The index of the value given to the variable S is found in the array and the number of days given K is added.
    #Since 1 week consists of 7 days, mod operation is done and additions are made as much as the remaining number of days.
    return days[(days.index(S) + K%7) % 7]

print(day_of_week("Mon", 5))