def is_leap(year): ##defines function is_leap and checks whether said yr is leap or not
    leap= False ##we assume year is not leap by default
    if(year %4 ==0): ##checks if year is divisible by 4
        if(year % 100 != 0) or(year % 400 == 0):
            leap=True ##if the above conditions are met then the year is a leap yr

    return leap ##returns result of our logic

year = int(input("Enter an year: ")) ##asks the user to input a yr

if is_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

##if it is divisible by 4 it is a leap year
##if it is divisible by 100 it is not a leap year unless it is also divisible by 400

