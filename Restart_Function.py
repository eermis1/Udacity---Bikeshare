import pandas as pd

# 1) User determines which city would like to investigate

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
    "Type 'Spesific' For Spesific Date Search..\n"
    "Type 'Both' For Day & Month Combined Search..\n"
    "Type 'None' For No Time Filter..\n")).title()
while time_period not in ("Month", "Day", "Both", "None", "Spesific"):
    print("\\Incorrect Selection, Please Type 'Month', 'Day', 'Both', 'Spesific' or 'None'\n")
    time_period = str(input()).title()
    print("\n\\Evaluating...")
else:
    print("Time Selection Is {}\n"
          "Lets Move On...\n".format(
              str(time_period).title()))

if time_period == "None":  # no month / day filtering
    print("\nLets Look Without Any Time Filter\n" +
          "Please See The Below For Statistics..\n")

elif time_period == "Month":  # if user would like to get monthly data ,ask which month ?
    month = str(input(
        "\nWhich Month Would You Like To Investigate ? January, February, March, April, May, or June.... ?\n"
        "Please write down one of them\n")).title()
    while month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
        print("\\Incorrect Selection, Please Type a Month Between January - December")
        month = str(input()).title()
        print("\\Evaluating...\n")
    else:
        print("Time Selection Is {} Which Is Included To My System :)\n".format(
            str(month).title()))
        print("Your Selections Are;\n"
              "City = {}\n"
              "Time Option = {}\n"
              "Month = {}\n"
              "Perfect !!.. lets See Statistics....\n".format(city, time_period, month))

elif time_period == "Day":
    typeofday = str(input("Would You Like To Filter Days by as Weekdays or as Day of Year Basis?\n"
                          "\nFor Weekdays Basis Filter Like Monday, Tuesday, Wednesday etc; Type 'Weekday'..\n"
                          "For Day of Year Basis Filter Like 200th , 40th; Type 'Yearday'..\n")).title()
    while typeofday not in ("Weekday", "Yearday"):
        print("\\Incorrect Selection, Please Type 'Weekday' or 'Yearday'")
        typeofday = str(input()).title()
        print("\\Evaluating...\n")
    else:
        print("In Order To Show You Statistics, We Have Only One More Step..\n".format(
            str(typeofday).title()))

    if typeofday == "Weekday":
        weekday = str(input("Which Day of Week Would You Like To Investigate?\n"
                            "Type 'Monday', 'Tuesday' or etc...\n")).title()
        while weekday not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print("\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc....")
            weekday = str(input()).title()
            print("\\Evaluating...")
        else:
            print("Excellent!!\n")
            print("Your Selections Are;\n"
                  "City = {}\n"
                  "Time Option = {}\n"
                  "Day Option = {}\n"
                  "Day Selection = {}\n"
                  "Perfect !!.. lets See Statistics....\n".format(city, time_period, typeofday, weekday))

    elif typeofday == "Yearday":
        yearday = int(input("Which Date Would You Like To Investigate?\n"
                            "Type 200, 150 etc...\n"))
        while yearday < 0 or yearday > 365:
            print("\\Incorrect Selection, Please Type A Number Between 1 - 365")
            yearday = int(input())
            print("\\Evaluating...")
        else:
            print("Excellent!!\n")
            print("Your Selections Are;\n"
                  "City = {}\n"
                  "Time Option = {}\n"
                  "Day Option = {}\n"
                  "Day Selection = {}\n"
                  "Perfect !!.. lets See Statistics....\n".format(city, time_period, typeofday, yearday))

elif time_period == "Both":
    print("Please Type Weekday & Month Which You Would Like To Investigate")
    both_day = str(input("First, Enter Weekday Like 'Monday', 'Tuesday' etc..\n")).title()
    while both_day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
        print("\\Incorrect Selection, Please Type 'Monday', 'Tuesday', 'Wednesday' or etc....")
        both_day = str(input()).title()
        print("\\Evaluating...\n")
    else:
        print("Perfect!.., 1 Last Question ..\n".format(str(both_day).title()))
        both_month = str(
            input("Type Month For Investigate Like 'January', 'February' etc..\n")).title()
        while both_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("\\Incorrect Selection, Please Type 'January', 'February' or etc....")
            both_month = str(input()).title()
            print("\\Evaluating...\n")
        else:
            print("Perfect!.., We Are OK\n")
            print("Your Selections Are;\n"
                  "City = {}\n"
                  "Time Option = {}\n"
                  "Day Option = {}\n"
                  "Month Option = {}\n"
                  "Perfect !!.. lets See Statistics....\n".format(city, time_period, both_day, both_month))

elif time_period == "Spesific":
    print("Please Type Date & Month Which You Would Like To Investigate")
    spesific_day = int(input("First, Enter Month Date Like '15', '20' etc..\n"))
    while spesific_day < 1 and spesific_day > 31:
        print("\\Incorrect Selection, Please Type A Number Between 1 - 31....")
        spesific_day = int(input())
        print("\\Evaluating...\n")
    else:
        print("Perfect!.., 1 Last Question ..\n".format(str(spesific_day).title()))
        spesific_month= str(
            input("Type Month For Investigate Like 'January', 'February' etc..\n")).title()
        while spesific_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("\\Incorrect Selection, Please Type 'January', 'February' or etc....")
            spesific_month = str(input()).title()
            print("\\Evaluating...\n")
        else:
            print("Perfect!.., We Are OK\n")
            print("Your Selections Are;\n"
                  "City = {}\n"
                  "Time Option = {}\n"
                  "Day Option = {}\n"
                  "Month Option = {}\n"
                  "Perfect !!.. lets See Statistics....\n".format(city, time_period, spesific_day, spesific_month))


def month_to_int(month):

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


def month_to_int_both(both_month):

    if both_month == "January":
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


def month_to_int_spesific(spesific_month):

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


def city_converter(time_period, city):  # data preperation for further functions
    if time_period == "Month" and city == "Chicago":
        chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.month
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.month
        return chicago

    elif time_period == "Day" and city == "Chicago":
        if typeofday == "Weekday":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.weekday_name
            return chicago

        elif typeofday == "Yearday":
            chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
            chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.dayofyear
            chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.dayofyear
            return chicago

    elif time_period == "None" and city == "Chicago":
        chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"])
        chicago["End Time"] = pd.to_datetime(chicago["End Time"])
        return chicago

    elif time_period == "Both" and city == "Chicago":
        chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
        chicago["End Time_month"] = pd.to_datetime(chicago["End Time"]).dt.month
        chicago["Start Time_month"] = pd.to_datetime(chicago["Start Time"]).dt.month
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.weekday_name
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.weekday_name
        return chicago

    elif time_period == "Spesific" and city == "Chicago":
        chicago = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/chicago.csv")
        chicago["End Time_month"] = pd.to_datetime(chicago["End Time"]).dt.month
        chicago["Start Time_month"] = pd.to_datetime(chicago["Start Time"]).dt.month
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.day
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.day
        return chicago

    if time_period == "Month" and city == "New York City":
        new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.month
        return new_york_city

    elif time_period == "Day" and city == "New York City":
        if typeofday == "Weekday":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.weekday_name
            return new_york_city

        elif typeofday == "Yearday":
            new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
            new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.dayofyear
            new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.dayofyear
            return new_york_city

    elif time_period == "None" and city == "New York City":
        new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"])
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"])
        return new_york_city

    elif time_period == "Both" and city == "New York City":
        new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
        new_york_city["End Time_month"] = pd.to_datetime(new_york_city["End Time"]).dt.month
        new_york_city["Start Time_month"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.weekday_name
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.weekday_name
        return new_york_city

    elif time_period == "Spesific" and city == "New York City":
        new_york_city = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/new_york_city.csv")
        new_york_city["End Time_month"] = pd.to_datetime(new_york_city["End Time"]).dt.month
        new_york_city["Start Time_month"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.day
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.day
        return new_york_city

        if time_period == "Month" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.month
            return washington

        elif time_period == "Day" and city == "Washington":
            if typeofday == "Weekday":
                washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
                washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
                washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.weekday_name
                return washington

            elif typeofday == "Yearday":
                washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
                washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.dayofyear
                washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.dayofyear
                return washington

        elif time_period == "None" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
            washington["Start Time"] = pd.to_datetime(washington["Start Time"])
            washington["End Time"] = pd.to_datetime(washington["End Time"])
            return washington

        elif time_period == "Both" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
            washington["End Time_month"] = pd.to_datetime(washington["End Time"]).dt.month
            washington["Start Time_month"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.weekday_name
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.weekday_name
            return washington

        elif time_period == "Spesific" and city == "Washington":
            washington = pd.read_csv("C:/Users/ASUS PC/Desktop/UDACITY/Python Calismalar/Bikeshare/washington.csv")
            washington["End Time_month"] = pd.to_datetime(washington["End Time"]).dt.month
            washington["Start Time_month"] = pd.to_datetime(washington["Start Time"]).dt.month
            washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.day
            washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.day
            return washington


print(city_converter(time_period, city))


def populardestination(city_converter):

    if time_period == "None":

        populardestination = city_converter(time_period, city).groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
        maxcountofpopulardestination = populardestination["Counts"].values.argmax()
        print("The Most Popular Destination In City Of {} Is\n".format(city).upper(), populardestination.iloc[maxcountofpopulardestination])


    elif time_period == "Month":

        populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == month_to_int(month)]
        populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name= "Counts")
        maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
        print("The Most Popular Destination In City Of {} For The Start Month Of {} Is\n".format(city, month).upper(), populardestinationv1.iloc[maxcountofpopulardestination])

    elif time_period == "Day":
        if typeofday == "Weekday":
            try:
                populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == weekday]
                populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                print("The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, weekday).upper(), populardestinationv1.iloc[maxcountofpopulardestination])
            except ValueError:  # some days have not data , to prevent program crash , exception has been made.
                print("No Record For Relevant Date\n".upper())
        elif typeofday == "Yearday":
            try:
                populardestination = city_converter(time_period, city)[city_converter(time_period, city)["Start Time"] == yearday]
                populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
                maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
                print("The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(city, yearday).upper(), populardestinationv1.iloc[maxcountofpopulardestination])
            except ValueError:  # some days have not data , to prevent program crash , exception has been made.
                print("No Record For Relevant Date\n".upper())

    elif time_period == "Both":
        try:
            populardestination = city_converter(time_period, city)[(city_converter(time_period, city)["Start Time"] == both_day) & (city_converter(time_period, city)["Start Time_month"] == month_to_int_both(both_month))]
            populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]).size().reset_index(name="Counts")
            maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
            print("The Most Popular Destination In City Of {} For The Combination Of {} - {} Is\n".format(city, both_month, both_day).upper(), populardestinationv1.iloc[maxcountofpopulardestination])
        except ValueError:  # some days have not data , to prevent program crash , exception has been made.
            print("No Record For Relevant Date\n".upper())

# elif spesific ekle üsttekinin benzeri


print(populardestination(city_converter))
