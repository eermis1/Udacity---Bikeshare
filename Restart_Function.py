# Restart function

# 1) User determines which city would like to investigate


def main():
    city = str(input("Hello User\n"
                     "Let's Explain Some US Bikeshare Data\n"
                     "Which City Would Like To Deep Dive\nPlease Enter; Chicago, New York City, Washington\n")).title()
    while city not in ("New York City", "Washington", "Chicago"):
        print("\\Incorrect Selection, Please Type 'Washington', 'New York City' or 'Chicago'\n")
        city = str(input()).title()
        print("\n\\Evaluating...")
    else:
        print("Your Choice Is {} Which Seems To Be OK For Investigate :)\n"
              "I Can Show You Some Statistics.. Lets Continue...\n".format(
                  str(city).title()))

# 2) User determines whether he/she would like to look into any spesific month or day / or no time filtering
    time_period = str(input(
        "\nWould You Like To Filter The Data By Month, By Day, or Not At'All?\n"
        "Don't Forget You Can Search By Both Date & Month Together!!\n"
        "So..\n"
        "\nType 'Month' For Monthly Search..\n"
        "Type 'Day' For Daily Search..\n"
        "Type 'Both' For Day & Month Combined Search..\n"
        "Type 'None' For No Time Filter..\n")).title()
    while time_period not in ("Month", "Day", "Both", "None"):
        print("\\Incorrect Selection, Please Type 'Month', 'Day', 'Both', or 'None'\n")
        time_period = str(input()).title()
        print("\n\\Evaluating...")
    else:
        print("Time Selection Is {}\n"
              "Lets Move On...\n".format(
                  str(time_period).title()))

    if time_period == "None":  # no month / day filtering
        print("\nLets Look Without Any Time Filter\n" +
              "Please See The Below For Statistics..\n")
        month = "nomonth"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
        day = "noday"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
        both = "noboth"

    elif time_period == "Month":  # if user would like to get monthly data ,ask which month ?
        month = str(input(
            "\nWhich Month Would You Like To Investigate ? January, February, March, April, May, or June.... ?\n"
            "Please write down one of them\n")).title()
        day = "noday"
        both = "noboth"
        while month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("\\Incorrect Selection, Please Type a Month Between January - December")
            month = str(input()).title()
            print("\\Evaluating...\n")
        else:
            print("Time Selection Is {} Which Is Included To My System :)\n".format(
                str(month).title()))
            print("Before Going Into Statistic Calculations, The Selections Which Were Choosen By You;\n"
                  "City = {}\n"
                  "Time Period Property = {}\n"
                  "Month = {}\n".format(city, time_period, month))
            restart = str(input("Are You Sure About Your Filters? You Can Restart The Program..\n"
                                "Type 'Y' For Restart\n"
                                "Type 'N' For Continue\n")).title()
            while restart not in ("Y", "N"):
                print("\\Incorrect Selection, Please Type 'Y' or 'N'")
                restart = str(input()).title()
            else:
                if restart == "Y":
                    main()
                elif restart == "N":
                    pass

    elif time_period == "Day":
        month = "nomonth"
        both = "noboth"
        typeofday = str(input("Would You Like To Filter Days by as Weekdays or as Day of Year Basis?\n"
                              "\nFor Weekdays Basis Filter Like Monday, Tuesday, Wednesday etc; Type 'Weekday'..\n"
                              "For Day of Year Basis Filter Like 200th , 40th; Type 'Yearday'..\n")).title()
        while typeofday not in ("Weekday", "Yearday", "YearDay", "WeekDay"):
            print("\\Incorrect Selection, Please Type 'Weekday' or 'Yearday'")
            typeofday = str(input()).title()
            print("\\Evaluating...\n")
        else:
            print("In Order To Show You Statistics, We Have Only One More Step..\n".format(
                str(typeofday).title()))

        if typeofday == "Weekday" or typeofday == "WeekDay":
            weekday = str(input("Which Day of Week Would You Like To Investigate?\n"
                                "Type 'Monday', 'Tuesday' or etc...\n")).title()
            while weekday not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
                print("\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc....")
                weekday = str(input()).title()
                print("\\Evaluating...")
            else:
                print("Excellent!!\n")

            print("Before Going Into Statistical Calculations, The Selection Which Have Been Choosen By You;\n"
                  "City = {}\n"
                  "Time Period Property = {}\n"
                  "Day Type = {}\n"
                  "Day = {}\n".format(city, time_period, typeofday, weekday))
            restart = str(input("Are You Sure About Your Filters? You Can Restart The Program..\n"
                                "Type 'Y' For Restart\n"
                                "Type 'N' For Continue\n")).title()
            while restart not in ("Y", "N"):
                print("\\Incorrect Selection, Please Type 'Y' or 'N'")
                restart = str(input()).title()
            else:
                if restart == "Y":
                    main()
                elif restart == "N":
                    pass
        elif typeofday == "Yearday" or typeofday == "YearDay":
            yearday = int(input("Which Date Would You Like To Investigate?\n"
                                "Type 200, 150 etc...\n"))
            while yearday < 0 or yearday > 365:
                print("\\Incorrect Selection, Please Type A Number Between 1 - 365")
                yearday = int(input())
                print("\\Evaluating...")
            else:
                print("Excellent!!\n")
            print("Before Going Into Statistical Calculations, The Selection Which Have Been Choosen By You;\n"
                  "City = {}\n"
                  "Time Period Property = {}\n"
                  "Day Type = {}\n"
                  "Day = {}\n".format(city, time_period, typeofday, yearday))
            restart = str(input("Are You Sure About Your Filters? You Can Restart The Program..\n"
                                "Type 'Y' For Restart\n"
                                "Type 'N' For Continue\n")).title()
            while restart not in ("Y", "N"):
                print("\\Incorrect Selection, Please Type 'Y' or 'N'")
                restart = str(input()).title()
            else:
                if restart == "Y":
                    main()
                elif restart == "N":
                    pass

    elif time_period == "Both":
        day = "noday"
        month = "nomonth"
        print("Please Type Weekday & Month Which You Would Like To Investigate")
        both_day = str(input("First, Enter Weekday Like 'Monday', 'Tuesday' etc..\n")).title()
        while both_day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print("\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc....")
            both_day = str(input()).title()
            print("\\Evaluating...\n")
        else:
            print("Perfect!.., 1 Last Question ..\n".format(str(both_day).title()))
            both_month = str(input("Type Month For Investigate\n")).title()
            while both_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
                print("\\Incorrect Selection, Please Type 'January', 'February' or etc....")
                both_month = str(input()).title()
                print("\\Evaluating...\n")
            else:
                print("Perfect!.., We Are OK\n")

            print("Before Going Into Statistical Calculations, The Selection Which Have Been Choosen By You;\n"
                  "City = {}\n"
                  "Time Period Property = {}\n"
                  "Day = {}\n"
                  "Month = {}\n".format(city, time_period, both_day, both_month))
            restart = str(input("Are You Sure About Your Filters? You Can Restart The Program..\n"
                                "Type 'Y' For Restart\n"
                                "Type 'N' For Continue\n")).title()
            while restart not in ("Y", "N"):
                print("\\Incorrect Selection, Please Type 'Y' or 'N'")
                restart = str(input()).title()
            else:
                if restart == "Y":
                    main()
                elif restart == "N":
                    pass


print(main())
# time = timeperiod_details()
# print(time[0])
# print(time[1])


# restart = str(input("Would You Like To Restart?\n"
#                     "Type 'Y' For Restart\n"
#                    "Type 'N' For Quit\n")).title()

# if restart == "Y":
#    citycheck()
# else:
#     quit()
