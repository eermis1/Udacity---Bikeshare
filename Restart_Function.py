# Restart function

# 1) User determines which city would like to investigate
city = str(input("Hello User\n"
                 "Let's Explain Some US Bikeshare Data\n"
                 "Which City Would Like To Deep Dive\nPlease Enter; Chicago, New York City, Washington\n")).title()

while city not in ("New York City", "Washington", "Chicago"):
    print("\nIncorrect Selection, Please Type 'Washington', 'New York City' or 'Chicago'")
    city = str(input()).title()
    print("\nYour Choice Is" + " " + str(city).title() + " " + "Evaluating...")
else:
    print("Your Choice Is {} Which Seems Included To My Back-End :) , I Can Show You Statistics.. Lets Continue...\n".format(
        str(city).title()))

# 2) User determines whether he/she would like to look into any spesific month or day / or no time filtering
time_period = str(input(
    "\nWould You Like To Filter The Data By Month, By Day, or Not At'All?\n"
    "Don't Forget You Can Search By Both Date & Month!!\n"
    "So..\n"
    "\nType 'Month' For Monthly Search..\n"
    "Type 'Day' For Daily Search..\n"
    "Type 'Both' For Day & Month Search..\n"
    "Type 'None' For No Time Filter..\n")).title()
while time_period not in ("Month", "Day", "Both", "None"):
    print("Incorrect Selection, Please Type 'Month', 'Day', 'Both', or 'None'")
    time_period = str(input()).title()
    print("Your Selection Is" + " " + str(time_period).title() + " " + "Evaluating...\n")
else:
    print("\nTime Selection Is {} Which Is Included To My System :) , I Can Show You Statistics.. Lets Continue...\n".format(
        str(time_period).title()))


def timeperiod_details():
    if time_period == "None":  # no month / day filtering
        print("\nLets Look Without Any Time Filter\n" +
              "Please See The Below For Statistics..\n")
        month = "nomonth"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
        day = "noday"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
        both = "noboth"
        return "No Time Filter"

    elif time_period == "Month":  # if user would like to get monthly data ,ask which month ?
        month = str(input(
            "\nWhich Month Would You Like To Investigate ? January, February, March, April, May, or June.... ?\n"
            "Please write down one of them\n")).title()
        day = "noday"
        both = "noboth"
        while month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("Incorrect Selection, Please Type a Month Between January - December")
            month = str(input()).title()
            print("Your Selection Is" + " " + str(month).title() + " " + "Evaluating...\n")
        else:
            print("Time Selection Is {} Which Is Included To My System :) , Lets Look Into Statistics.. Lets Continue...\n".format(
                str(month).title()))
            if month == "January":
                return 1
            elif month == "February":
                return 2
            elif month == "March":
                return 3
            elif month == "April":
                return 4
            elif month == "May":
                return 5
            elif month == "June":
                return 6
            elif month == "July":
                return 7
            elif month == "August":
                return 8
            elif month == "September":
                return 9
            elif month == "October":
                return 10
            elif month == "November":
                return 11
            elif month == "December":
                return 12
        return month
    elif time_period == "Day":
        typeofday = str(input("Would You Like To Filter Days by as Weekdays or as Day of Year Basis?\n"
                              "\nFor Weekdays Basis Filter Like Monday, Tuesday, Wednesday etc; Type 'Weekday'..\n"
                              "For Day of Year Basis Filter Like 200th , 40th; Type 'Yearday'..\n")).title()
        while typeofday not in ("Weekday", "Yearday", "YearDay"):
            print("Incorrect Selection, Please Type 'Weekday' or 'Yearday'")
            typeofday = str(input()).title()
            print("Your Selection Is" + " " + str(typeofday).title() + " " + "Evaluating...\n")
        else:
            print("Time Selection Is {} Which Is Included To My System :) , Lets Look Into Statistics.. Lets Continue...\n".format(
                str(typeofday).title()))
        return typeofday


print(timeperiod_details())


# restart = str(input("Would You Like To Restart?\n"
#                     "Type 'Y' For Restart\n"
#                    "Type 'N' For Quit\n")).title()

# if restart == "Y":
#    citycheck()
# else:
#     quit()
