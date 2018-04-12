#deneme
import pandas as pd
import calendar
import colorama
import sys
colorama.init()
green = "\033[01;32m"
red = "\033[01;31m"
native = "\033[m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
""" I added colors to some printings in order to better     illustration """

def main():
    """ in order to make add restart functionality i kept all functions in 1 main function
    so regarding to user input code goes to main function starting point"""

    city = str(input("Hello User\n"
                     "Let's Explain Some US Bikeshare Data\n"
                     "Which City Would Like To Deep Dive\nPlease Enter; Chicago, New York City, Washington\n")).title()
    while city not in ("New York City", "Washington", "Chicago"):
        print(red + "\Incorrect Selection, Please Type 'Washington', 'New York City' or 'Chicago'\n" + native)
        city = str(input()).title()
        print(yellow + "\n\\Evaluating..." + native)
    else:
        print(green + "Your Choice Is {} Which Seems To Be OK For Investigate :)\n"
              "I Can Show You Some Statistics.. Lets Continue...\n".format(
                str(city).title()) + native)

    time_period = str(input(
        "\nWould You Like To Filter The Data By Month, By Day, or Not At'All?\n"
        "Don't Forget You Can Search By Both Date & Month Together!!\n"
        "So..\n"
        "\nType 'Month' For Monthly (Ex:January) Search..\n"
        "Type 'Day' For Daily (Ex:Monday or 200th) Search..\n"
        "Type 'Spesific' For Spesific Date (Ex:18-March) Search..\n"
        "Type 'Both' For Day & Month Combined (Ex: Tuesday&January) Search..\n"
        "Type 'None' For No Time Filter..\n")).title()
    while time_period not in ("Month", "Day", "Both", "None", "Spesific"):
        print(red + "\\Incorrect Selection, Please Type 'Month', 'Day', 'Both', 'Spesific' or 'None'\n" + native)
        time_period = str(input()).title()
        print(yellow + "\n\\Evaluating..." + native)
    else:
        print(green + "Time Selection Is {}\n"
              "Lets Move On...\n".format(
                  str(time_period).title()) + native)

    if time_period == "None":
        print("\nLets Look Without Any Time Filter\n" +
              "Please See The Below For Statistics..\n")
        restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                            "Type 'Y' For Re-Adjust\n"
                            "Type 'N' For Continue\n")).title()
        while restart not in ("Y", "N"):
            print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
            restart = str(input()).title()
        if restart == "Y":
            main()
        else:
            pass
    elif time_period == "Month":
        month = str(input(
            "\nWhich Month Would You Like To Investigate ? January, February, March, April, May, or June.... ?\n"
            "Please write down one of them\n")).title()
        while month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print(red + "\\Incorrect Selection, Please Type a Month Between January - December" + native)
            month = str(input()).title()
            print(yellow + "\\Evaluating...\n" + native)
        else:
            print(green + "Time Selection Is {} Which Is Included To My System :)\n".format(
                str(month).title()) + native)
            print(cyan + "Your Selections Are;\n"
                  "City = {}\n"
                  "Time Option = {}\n"
                  "Month = {}\n"
                  "Perfect !!.. Before Seeing Statistics....\n".format(city, time_period, month) + native)
            restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                                "Type 'Y' For Re-adjust\n"
                                "Type 'N' For Continue\n")).title()
            while restart not in ("Y", "N"):
                print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
                restart = str(input()).title()
            if restart == "Y":
                main()
            else:
                pass
    elif time_period == "Day":
        typeofday = str(input("Would You Like To Filter Days by as Weekdays or as Day of Year Basis?\n"
                              "\nFor Weekdays Basis Filter Like Monday, Tuesday, Wednesday etc; Type 'Weekday'..\n"
                              "For Day of Year Basis Filter Like 200th , 40th; Type 'Yearday'..\n")).title()
        while typeofday not in ("Weekday", "Yearday"):
            print(red + "\\Incorrect Selection, Please Type 'Weekday' or 'Yearday'" + native)
            typeofday = str(input()).title()
            print(yellow + "\\Evaluating...\n" + native)
        else:
            print(green + "In Order To Show You Statistics, We Have Only One More Step..\n".format(str(typeofday).title()) + native)

        if typeofday == "Weekday":
            weekday = str(input("Which Day of Week Would You Like To Investigate?\n"
                                "Type 'Monday', 'Tuesday' or etc...\n")).title()
            while weekday not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
                print(red + "\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc...." + native)
                weekday = str(input()).title()
                print(yellow + "\\Evaluating..." + native)
            else:
                print(green + "Excellent!!\n" + native)
                print(cyan + "Your Selections Are;\n"
                      "City = {}\n"
                      "Time Option = {}\n"
                      "Day Option = {}\n"
                      "Day Selection = {}\n"
                      "Perfect !!.. Before Seeing Statistics....\n".format(city, time_period, typeofday, weekday) + native)
                restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                                    "Type 'Y' For Re-Adjust\n"
                                    "Type 'N' For Continue\n")).title()
                while restart not in ("Y", "N"):
                    print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
                    restart = str(input()).title()
                if restart == "Y":
                    main()
                else:
                    pass

        elif typeofday == "Yearday":
            yearday = int(input("Which Date Would You Like To Investigate?\n"
                                "Type 200, 150 etc...\n"))
            while yearday < 0 or yearday > 365:
                print(red + "\\Incorrect Selection, Please Type A Number Between 1 - 365" + native)
                yearday = int(input())
                print(yellow + "\\Evaluating..." + native)
            else:
                print(green + "Excellent!!\n" + native)
                print(cyan + "Your Selections Are;\n"
                      "City = {}\n"
                      "Time Option = {}\n"
                      "Day Option = {}\n"
                      "Day Selection = {}\n"
                      "Perfect !!.. Before Seeing Statistics....\n".format(city, time_period, typeofday, yearday) + native)
                restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                                    "Type 'Y' For Re-Adjust\n"
                                    "Type 'N' For Continue\n")).title()
                while restart not in ("Y", "N"):
                    print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
                    restart = str(input()).title()
                if restart == "Y":
                    main()
                else:
                    pass

    elif time_period == "Both":
        print("Please Type Weekday & Month Which You Would Like To Investigate")
        both_day = str(input("First, Enter Weekday Like 'Monday', 'Tuesday' etc..\n")).title()
        while both_day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print(red + "\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc...." + native)
            both_day = str(input()).title()
            print(yellow + "\\Evaluating...\n" + native)
        else:
            print(green + "Perfect!.., 1 Last Question ..\n".format(str(both_day).title()) + native)
            both_month = str(
                input("Type Month For Investigate Like 'January', 'February' etc..\n")).title()
            while both_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
                print(red + "\\Incorrect Selection, Please Type 'January', 'February' or etc...." + native)
                both_month = str(input()).title()
                print(yellow + "\\Evaluating...\n" + native)
            else:
                print(green + "Perfect!.., We Are OK\n" + native)
                print(cyan + "Your Selections Are;\n"
                      "City = {}\n"
                      "Time Option = {}\n"
                      "Day Option = {}\n"
                      "Month Option = {}\n"
                      "Perfect !!.. Before Seeing Statistics....\n".format(city, time_period, both_day, both_month) + native)
                restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                                    "Type 'Y' For Re-Adjust\n"
                                    "Type 'N' For Continue\n")).title()
                while restart not in ("Y", "N"):
                    print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
                    restart = str(input()).title()
                if restart == "Y":
                    main()
                else:
                    pass

    elif time_period == "Spesific":
        print("Please Type Date & Month Which You Would Like To Investigate")
        spesific_day = int(input("First, Enter A Date Like '15', '20' etc..\n"))
        while spesific_day < 1 and spesific_day > 31:
            print(red + "\\Incorrect Selection, Please Type A Number Between 1 - 31...." + native)
            spesific_day = int(input())
            print(yellow + "\\Evaluating...\n" + native)
        else:
            print(green + "Perfect!.., 1 Last Question ..\n".format(str(spesific_day).title()) + native)
            spesific_month = str(input("Type Month For Investigate Like 'January', 'February' etc..\n")).title()
            while spesific_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
                print(red + "\\Incorrect Selection, Please Type 'January', 'February' or etc...." + native)
                spesific_month = str(input()).title()
                print(yellow + "\\Evaluating...\n" + native)
            else:
                print(green + "Perfect!.., We Are OK\n" + native)
                print(cyan + "Your Selections Are;\n"
                      "City = {}\n"
                      "Time Option = {}\n"
                      "Day Option = {}\n"
                      "Month Option = {}\n"
                      "Perfect !!.. Before Seeing Statistics....\n".format(city, time_period, spesific_day, spesific_month) + native)
                restart = str(input("Would You Like To Re-Adjust Your Selections?\n"
                                    "Type 'Y' For Re-Adjust\n"
                                    "Type 'N' For Continue\n")).title()
                while restart not in ("Y", "N"):
                    print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
                    restart = str(input()).title()
                if restart == "Y":
                    main()
                else:
                    pass

    def month_to_int(time_period):
        """ you were right my Teacher ! i added together other month --> integer functions"""

        if time_period == "Month":

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

        if time_period == "Both":

            if both_month == "Janaury":
                return 1
            elif both_month == "February":
                return 2
            elif both_month == "March":
                return 3
            elif both_month == "April":
                return 4
            elif both_month == "May":
                return 5
            elif both_month == "June":
                return 6
            elif both_month == "July":
                return 7
            elif both_month == "August":
                return 8
            elif both_month == "September":
                return 9
            elif both_month == "October":
                return 10
            elif both_month == "November":
                return 11
            elif both_month == "December":
                return 12

        if time_period == "Spesific":

            if spesific_month == "January":
                return 1
            elif spesific_month == "February":
                return 2
            elif spesific_month == "March":
                return 3
            elif spesific_month == "April":
                return 4
            elif spesific_month == "May":
                return 5
            elif spesific_month == "June":
                return 6
            elif spesific_month == "July":
                return 7
            elif spesific_month == "August":
                return 8
            elif spesific_month == "September":
                return 9
            elif spesific_month == "October":
                return 10
            elif spesific_month == "November":
                return 11
            elif spesific_month == "December":
                return 12

    def city_converter(time_period, city):
        """this function prepares DataFrame regarding to user input, it contains whole combinations"""
        if time_period == "Month" and city == "Chicago":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
            chicago["Start Time_weekday"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.month
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.month
            return chicago

        elif time_period == "Day" and city == "Chicago":
            if typeofday == "Weekday":
                chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
                chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
                chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
                chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.weekday_name
                return chicago

            elif typeofday == "Yearday":
                chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
                chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
                chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.dayofyear
                chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.dayofyear
                return chicago

        elif time_period == "None" and city == "Chicago":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"])
            chicago["End Time"] = pd.to_datetime(chicago["End Time"])
            chicago["Start Time_weekday"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
            chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
            return chicago

        elif time_period == "Both" and city == "Chicago":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
            chicago["End Time_month"] = pd.to_datetime(chicago["End Time"]).dt.month
            chicago["Start Time_month"] = pd.to_datetime(chicago["Start Time"]).dt.month
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.weekday_name
            return chicago

        elif time_period == "Spesific" and city == "Chicago":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time_hour"] = pd.to_datetime(chicago["Start Time"]).dt.hour
            chicago["End Time_month"] = pd.to_datetime(chicago["End Time"]).dt.month
            chicago["Start Time_month"] = pd.to_datetime(chicago["Start Time"]).dt.month
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.day
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.day
            return chicago

        if time_period == "Month" and city == "New York City":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
            new_york_city["Start Time_weekday"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.month
            return new_york_city

        elif time_period == "Day" and city == "New York City":
            if typeofday == "Weekday":
                new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
                new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
                new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
                new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.weekday_name
                return new_york_city

            elif typeofday == "Yearday":
                new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
                new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
                new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.dayofyear
                new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.dayofyear
                return new_york_city

        elif time_period == "None" and city == "New York City":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"])
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"])
            new_york_city["Start Time_weekday"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
            new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
            return new_york_city

        elif time_period == "Both" and city == "New York City":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
            new_york_city["End Time_month"] = pd.to_datetime(new_york_city["End Time"]).dt.month
            new_york_city["Start Time_month"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.weekday_name
            return new_york_city

        elif time_period == "Spesific" and city == "New York City":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time_hour"] = pd.to_datetime(new_york_city["Start Time"]).dt.hour
            new_york_city["End Time_month"] = pd.to_datetime(new_york_city["End Time"]).dt.month
            new_york_city["Start Time_month"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.day
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.day
            return new_york_city

        elif time_period == "Month" and city == "Washington":
                washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
                washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
                washington["Start Time_weekday"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
                washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.month
                washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.month
                return washington

        elif time_period == "Day" and city == "Washington":
            if typeofday == "Weekday":
                washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
                washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
                washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
                washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.weekday_name
                return washington

            elif typeofday == "Yearday":
                washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
                washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
                washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.dayofyear
                washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.dayofyear
                return washington

        elif time_period == "None" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time"] = pd.to_datetime(washington["Start Time"])
            washington["End Time"] = pd.to_datetime(washington["End Time"])
            washington["Start Time_weekday"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
            washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
            return washington

        elif time_period == "Both" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
            washington["End Time_month"] = pd.to_datetime(washington["End Time"]).dt.month
            washington["Start Time_month"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.weekday_name
            return washington

        elif time_period == "Spesific" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time_hour"] = pd.to_datetime(washington["Start Time"]).dt.hour
            washington["End Time_month"] = pd.to_datetime(washington["End Time"]).dt.month
            washington["Start Time_month"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.day
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.day
            return washington

    def populardestination(city_converter, time_period):    # calculates popular destination

        if time_period == "None":

            populardestination = city_converter(time_period, city).groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
            maxcountofpopulardestination = populardestination["Counts"].values.argmax()
            print(yellow + "The Most Popular Destination In City Of {} Is\n".format(city).upper() + native, populardestination.iloc[maxcountofpopulardestination])

        elif time_period == "Month":
            try:
                populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)]
                populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name= "Counts")
                maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                print(yellow + "The Most Popular Destination In City Of {} For The Start Month Of {} Is\n".format(city, month).upper() + native, populardestinationv1.iloc[maxcountofpopulardestination])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Destination In City Of {} For The Start Month Of {} Is\n".format(city, month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == weekday]
                    populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                    maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                    print(yellow + "The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, weekday).upper() + native, populardestinationv1.iloc[maxcountofpopulardestination])
                except (ValueError, KeyError):
                    print(yellow + "The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, weekday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)
            elif typeofday == "Yearday":
                try:
                    populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == yearday]
                    populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                    maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                    print(yellow + "The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, yearday).upper() + native, populardestinationv1.iloc[maxcountofpopulardestination])
                except (ValueError, KeyError):
                    print(yellow + "The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, yearday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
            try:
                populardestination = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == both_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                print(yellow + "The Most Popular Destination In City Of {} For The Combination Of {} - {} Is\n".format(city, both_month, both_day).upper() + native, populardestinationv1.iloc[maxcountofpopulardestination])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Destination In City Of {} For The Combination Of {} - {} Is\n".format(city, both_month, both_day).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
            try:
                populardestination = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == spesific_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                print(yellow + "The Most Popular Destination In City Of {} For The Combination Of {} - {} Is\n".format(city, spesific_day, spesific_month).upper() + native, populardestinationv1.iloc[maxcountofpopulardestination])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Destination In City Of {} For The Combination Of {} - {} Is\n".format(city, spesific_day, spesific_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(populardestination(city_converter, time_period))

    def totaltripbygender(city_converter, time_period):  # calculates total trip taken by gender

        if time_period == "None":
            try:
                sumbygender = city_converter(time_period, city).groupby("Gender").describe()["Trip Duration"]
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} Are\n".format(city).upper() + native, sumbygender)
            except (ValueError, KeyError):
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} Are\n".format(city).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Month":
            try:
                gendersum = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)]
                sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Month Of {} Are\n".format(city, month).upper() + native, sumbygender)
            except (ValueError, KeyError):
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Month Of {} Are\n".format(city, month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    gendersum = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == weekday]
                    sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
                    print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Of {} Are\n".format(city, weekday).upper() + native, sumbygender)
                except (ValueError, KeyError):
                    print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Of {} Are\n".format(city, weekday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)


            elif typeofday == "Yearday":
                try:
                    gendersum = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == yearday]
                    sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
                    print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Of {} Are\n".format(city, yearday).upper() + native, sumbygender)
                except (ValueError, KeyError):
                    print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Of {} Are\n".format(city, yearday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
            try:
                gendersum = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == both_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, both_day, both_month).upper() + native, sumbygender)
            except (ValueError, KeyError):
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, both_day, both_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)


        elif time_period == "Spesific":
            try:
                gendersum = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == spesific_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, spesific_day, spesific_month).upper() + native, sumbygender)
            except (ValueError, KeyError):
                print(yellow + "Stats Of Trip Duration By Gender In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, spesific_day, spesific_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(totaltripbygender(city_converter, time_period))

    def tripdurationbybirthyears(city_converter, time_period):  # calculates total trip taken depending birth years

        if time_period == "None":
            try:
                tripdurationbybirthyears = city_converter(time_period, city).groupby("Birth Year").sum()["Trip Duration"]
                tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} Are\n".format(city).upper() + native, tripdurationbybirthyears.head())
            except (ValueError, KeyError):
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} Are\n".format(city).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Month":
            try:
                tripdurationbybirthyears = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)]
                tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()["Trip Duration"]
                tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Month Of {} Are\n".format(city, month).upper() + native, tripdurationbybirthyears.head())
            except (ValueError, KeyError):
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Month Of {} Are\n".format(city, month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)


        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    tripdurationbybirthyears = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == weekday]
                    tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()["Trip Duration"]
                    tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                    print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Of {} Are\n".format(city, weekday).upper() + native, tripdurationbybirthyears.head())
                except (ValueError, KeyError):
                    print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Of {} Are\n".format(city, weekday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

            elif typeofday == "Yearday":
                try:
                    tripdurationbybirthyears = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == yearday]
                    tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()["Trip Duration"]
                    tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                    print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Of {} Are\n".format(city, yearday).upper() + native, tripdurationbybirthyears.head())
                except (ValueError, KeyError):
                    print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Of {} Are\n".format(city, yearday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
            try:
                tripdurationbybirthyears = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == both_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()["Trip Duration"]
                tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, both_day, both_month).upper() + native, tripdurationbybirthyears.head())
            except (ValueError, KeyError):
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, both_day, both_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
            try:
                tripdurationbybirthyears = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == spesific_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()["Trip Duration"]
                tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, spesific_day, spesific_month).upper() + native, tripdurationbybirthyears.head())
            except (ValueError, KeyError):
                print(yellow + "Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Combination Of {} - {} Are\n".format(city, spesific_day, spesific_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(tripdurationbybirthyears(city_converter, time_period))

    def usertypesize(city_converter, time_period):

        if time_period == "None":
            countofusertypes = city_converter(time_period, city).groupby("User Type").size()
            print(yellow + "The Count Of User types In City Of {} Are\n".format(city).upper() + native, countofusertypes)

        elif time_period == "Month":
            try:
                countofusertypesv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == month_to_int(time_period)]
                countofusertypes = countofusertypesv1.groupby("User Type").size()
                print(yellow + "The Count Of User Types In City Of {} For The End Month Of {} Are\n".format(city, month).upper() + native, countofusertypes)
            except (ValueError, KeyError):
                print(yellow + "The Count Of User Types In City Of {} For The End Month Of {} Are\n".format(city, month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    countofusertypesv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == weekday]
                    countofusertypes = countofusertypesv1.groupby("User Type").size()
                    print(yellow + "The Count Of User Types In City Of {} For The End Day Of {} are\n".format(city, weekday).upper() + native, countofusertypes)
                except (ValueError, KeyError):
                    print(yellow + "The Count Of User Types In City Of {} For The End Day Of {} are\n".format(city, weekday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

            elif typeofday == "Yearday":
                try:
                    countofusertypesv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == yearday]
                    countofusertypes = countofusertypesv1.groupby("User Type").size()
                    print(yellow + "The Count Of User Types In City Of {} For The End Day Of {} are\n".format(city, yearday).upper() + native, countofusertypes)
                except (ValueError, KeyError):
                    print(yellow + "The Count Of User Types In City Of {} For The End Day Of {} are\n".format(city, yearday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
            try:
                countofusertypesv1 = city_converter(time_period, city)[(city_converter(time_period, city)["End Time"] == both_day) & (city_converter(time_period, city)["End Time_month"] == month_to_int(time_period))]
                countofusertypes = countofusertypesv1.groupby("User Type").size()
                print(yellow + "The Count Of User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, both_day, both_month).upper() + native, countofusertypes)
            except (ValueError, KeyError):
                print(yellow + "The Count Of User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, both_day, both_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
            try:
                countofusertypesv1 = city_converter(time_period, city)[(city_converter(time_period, city)["End Time"] == spesific_day) & (city_converter(time_period, city)["End Time_month"] == month_to_int(time_period))]
                countofusertypes = countofusertypesv1.groupby("User Type").size()
                print(yellow + "The Count Of User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, spesific_day, spesific_month).upper() + native, countofusertypes)
            except (ValueError, KeyError):
                print(yellow + "The Count Of User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, spesific_day, spesific_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(usertypesize(city_converter, time_period))

    def usertype(city_converter, time_period):

        if time_period == "None":
            tripduration = city_converter(time_period, city).groupby("User Type").sum()["Trip Duration"]
            print(yellow + "The Total Trip Duration Regarding To User types In City Of {} Are\n".format(city).upper() + native, tripduration)

        elif time_period == "Month":
            try:
                tripdurationv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == month_to_int(time_period)]
                tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Month Of {} Are\n".format(city, month).upper() + native, tripduration)
            except (ValueError, KeyError):
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Month Of {} Are\n".format(city, month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    tripdurationv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == weekday]
                    tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
                    print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Of {} are\n".format(city, weekday).upper() + native, tripduration)
                except (ValueError, KeyError):
                    print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Of {} are\n".format(city, weekday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

            if typeofday == "Yearday":
                try:
                    tripdurationv1 = city_converter(time_period, city)[city_converter(time_period, city)["End Time"] == yearday]
                    tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
                    print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Of {} are\n".format(city, yearday).upper() + native, tripduration)
                except (ValueError, KeyError):
                    print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Of {} are\n".format(city, yearday).upper() + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
            try:
                tripdurationv1 = city_converter(time_period, city)[(city_converter(time_period, city)["End Time"] == both_day) & (city_converter(time_period, city)["End Time_month"] == month_to_int(time_period))]
                tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, both_day, both_month).upper() + native, tripduration)
            except (ValueError, KeyError):
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, both_day, both_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
            try:
                tripdurationv1 = city_converter(time_period, city)[(city_converter(time_period, city)["End Time"] == spesific_day) & (city_converter(time_period, city)["End Time_month"] == month_to_int(time_period))]
                tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, spesific_day, spesific_month).upper() + native, tripduration)
            except (ValueError, KeyError):
                print(yellow + "The Total Trip Duration Regarding To User Types In City Of {} For The End Day Combination Of {} - {} are\n".format(city, spesific_day, spesific_month).upper() + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(usertype(city_converter, time_period))

    def starttime_properties_month(city):
        """this function calculates the most popular month of a city therefore it always show
            the most popular month regardless of user input"""

        if city == "Chicago":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.month
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.month
            chicagov2 = chicago.groupby("Start Time").size().reset_index(name="Counts")
            maxofmonth = chicagov2["Counts"].values.argmax()
            monthnumber = chicagov2["Start Time"].iloc[maxofmonth]
            print(yellow + "The Most Interaction Occured Month For Start Time In Chicago Is\n" + native, calendar.month_name[monthnumber])
        elif city == "New York City":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.month
            new_york_cityv2 = new_york_city.groupby("Start Time").size().reset_index(name="Counts")
            maxofmonth = new_york_cityv2["Counts"].values.argmax()
            monthnumber = new_york_cityv2["Start Time"].iloc[maxofmonth]
            print(yellow + "The Most Interactio Occured Month For Start Time In New York City Is\n" + native,
                  calendar.month_name[monthnumber])
        elif city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/Udacity/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.month
            washingtonv2 = washington.groupby("Start Time").size().reset_index(name="Counts")
            maxofmonth = washingtonv2["Counts"].values.argmax()
            monthnumber = washingtonv2["Start Time"].iloc[maxofmonth]
            print(yellow + "The Most Interactio Occured Month For Start Time In Washington Is\n" + native,
                  calendar.month_name[monthnumber])

    print(starttime_properties_month(city))

    def first_5_raw(city_converter, time_period):
        """brings top5 trip duration's raw data regarding to user input"""

        if time_period == "None":
            first_5_raw = city_converter(time_period, city).sort_values("Trip Duration", ascending=False, inplace=False)
            print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time Can Be Shown Below\n" + native, first_5_raw.head())

        elif time_period == "Month":
            try:
                first_5_raw = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)].sort_values("Trip Duration", ascending=False, inplace=False)
                print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' Can Be Shown Below\n".format(month) + native, first_5_raw.head())
            except (ValueError, KeyError):
                print(yellow + "Top 5 Trip Duration's Raw Data Regarding Raw Data To Start Time '{}' Can Be Shown Below\n".format(month) + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Day":
            if typeofday == "Weekday":
                try:
                    first_5_raw = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == weekday].sort_values("Trip Duration", ascending=False, inplace=False)
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding Raw Data To Start Time '{}' Can Be Shown Below\n".format(weekday) + native, first_5_raw.head())
                except (ValueError, KeyError):
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding Raw Data To Start Time '{}' Can Be Shown Below\n".format(weekday) + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

            elif typeofday == "Yearday":
                try:
                    first_5_raw = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == yearday].sort_values("Trip Duration", ascending=False, inplace=False)
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' Can Be Shown Below\n".format(yearday) + native, first_5_raw.head())
                except (ValueError, KeyError):
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' Can Be Shown Below\n".format(yearday) + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Both":
                try:
                    first_5_raw = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == both_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))].sort_values("Trip Duration", ascending=False, inplace=False)
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' & '{}' Can Be Shown Below\n".format(both_day, both_month) + native, first_5_raw.head())
                except (ValueError, KeyError):
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' & '{}' Can Be Shown Below\n".format(both_day, both_month) + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
                try:
                    first_5_raw = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == spesific_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))].sort_values("Trip Duration", ascending=False, inplace=False)
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' & '{}' Can Be Shown Below\n".format(spesific_day, spesific_month) + native, first_5_raw.head())
                except (ValueError, KeyError,):
                    print(yellow + "Top 5 Trip Duration's Raw Data Regarding To Start Time '{}' & '{}' Can Be Shown Below\n".format(spesific_day, spesific_month) + native)
                    print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(first_5_raw(city_converter, time_period))

    def themostpopularday(city_converter, time_period):
        if time_period == "None":
            themostpopularday = city_converter(time_period, city).groupby(["Start Time_weekday"]).size().reset_index(name="Counts")
            countofthemostpopularday = themostpopularday["Counts"].values.argmax()
            print(yellow + "The Most Popular Day For Whole Dataset W/o Any Filter Is\n" + native, themostpopularday.iloc[countofthemostpopularday])

        elif time_period == "Month":
            try:
                themostpopularday = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)]
                themostpopulardayv2 = themostpopularday.groupby(["Start Time_weekday"]).size().reset_index(name="Counts")
                countofthemostpopularday = themostpopulardayv2["Counts"].values.argmax()
                print(yellow + "The Most Popular Day For Month Of {} Is\n".format(month) + native, themostpopulardayv2.iloc[countofthemostpopularday])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Day For Month Of {} Is\n".format(month) + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(themostpopularday(city_converter, time_period))

    def themostpopularhour(city_converter, time_period):
        if time_period == "None":
            themostpopularhour = city_converter(time_period, city).groupby(["Start Time_hour"]).size().reset_index(name="Counts")
            countofthemostpopularhour = themostpopularhour["Counts"].values.argmax()
            print(yellow + "The Most Popular Hour For Whole Dataset W/o Any Filter Is\n" + native, themostpopularhour.iloc[countofthemostpopularhour])
        elif time_period == "Month":
            try:
                themostpopularhour = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(time_period)]
                themostpopularhourv2 = themostpopularhour.groupby(["Start Time_hour"]).size().reset_index(name="Counts")
                countofthemostpopularhour = themostpopularhourv2["Counts"].values.argmax()
                print(yellow + "The Most Popular Hour For Month Of {} Is\n".format(month) + native, themostpopularhourv2.iloc[countofthemostpopularhour])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Hour For Month Of {} Is\n".format(month) + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

        elif time_period == "Spesific":
            try:
                themostpopularhour = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == spesific_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int(time_period))]
                themostpopularhourv2 = themostpopularhour.groupby(["Start Time_hour"]).size().reset_index(name="Counts")
                countofthemostpopularhour = themostpopularhourv2["Counts"].values.argmax()
                print(yellow + "The Most Popular Hour For Combination Of Day = {} & Month = {} Is\n".format(spesific_day, spesific_month) + native, themostpopularhourv2.iloc[countofthemostpopularhour])
            except (ValueError, KeyError):
                print(yellow + "The Most Popular Hour For Combination Of Day = {} & Month = {} Is\n".format(spesific_day, spesific_month) + native)
                print(red + "No Record Found For Relevant Selections In Selected City".upper() + " " + "Sorry: (".upper() + " Please Try Another One\n".upper() + native)

    print(themostpopularhour(city_converter, time_period))


    print(green + "\nThank You - See Ya Again\n" + native)
    print(yellow + "Uppps, I Almost Forgot\n"
                          "Would You Like To Re-Run??\n"
                          "\nType 'Y' For Re-Run\n"
                          "Type 'N' For Quit\n" + native)
    final_run = str(input()).title()
    while final_run not in ("Y", "N"):
        print(red + "\\Incorrect Selection, Please Type 'Y' or 'N'" + native)
        final_run = str(input()).title()
    if final_run == "Y":
        main()
    else:
        quit()


print(main())
