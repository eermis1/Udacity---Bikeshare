import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import sys
import os
# reading dataframe
chicago = pd.read_csv("chicago.csv")
new_york_city = pd.read_csv(
    "new_york_city.csv")
washington = pd.read_csv(
    "washington.csv")

# 1) User determines which city would like to investigate
city = str(input("Hello User\n"
                 "Let's Explain Some US Bikeshare Data\n"
                 "Which City Would Like To Deep Dive\nPlease Enter; Chicago, New York City, Washington\n")).title()
print("\nYour Choice Is" + " " + str(city).title() + " " + "Lets Continue !")


# 2) User determines whether he/she would like to look into any spesific month or day / or no time filtering
time_period = input(
    "\nWould you like to filter the data by month, by day, or not at'all?\n"
    "Type 'Month' for monthly search\n"
    "Type 'Day' for daily search\n"
    "Type 'None' for no time filter\n")
if time_period == "none" or time_period == "None":  # no month / day filtering
    print("\nOK lets look in general\n" + "\nPlease See The Below Results\n")
    month = "nomonth"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
    day = "noday"  # to prevent program crash if user choose no filter , we need to indicate no month or day selected
elif time_period == "Month" or time_period == "month":  # if user would like to get monthly data ,ask which month ?
    month = str(input(
        "\nWhich month? January, February, March, April, May, or June.... ?\n"
        "Please write down one of them\n")).title()
    print("\nDanke !!\n" + "\nLets See The Informations Regarding To Your Choices\n")
    day = "noday"  # to prevent program crash if user choose month, no day selection indication

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

    month_integer = int(month_to_int(month))  # being sure , month is an integer
    # print(month_integer, type(month_integer))

elif time_period == "day" or time_period == "Day":
    day = int(input("\nWhich day ?\n"
                    "Please enter a integer between 1 & 365\n"))
    print("\nOK Gotcha!!\n" + "\nYou can find the informations below !  \n")
    month = "nomonth"  # to prevent program crash if user choose day, no month selection indication
else:
    print("C'mooon!")


def city_converter(city, day, month):  # data preperation for further functions
    if day == "noday" and month != "nomonth" and city == "Chicago":
        chicago = pd.read_csv(
            "chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.month
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.month
        return chicago

    elif day != "noday" and month == "nomonth" and city == "Chicago":
        chicago = pd.read_csv(
            "chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.dayofyear
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.dayofyear
        return chicago
    elif day == "noday" and month == "nomonth" and city == "Chicago":
        chicago = pd.read_csv(
            "chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"])
        chicago["End Time"] = pd.to_datetime(chicago["End Time"])
        return chicago

    elif day == "noday" and month != "nomonth" and city == "New York City":
        new_york_city = pd.read_csv(
            "new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.month
        return new_york_city

    elif day != "noday" and month == "nomonth" and city == "New York City":
        new_york_city = pd.read_csv(
            "new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.dayofyear
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.dayofyear
        return new_york_city
    elif day == "noday" and month == "nomonth" and city == "New York City":
        new_york_city = pd.read_csv(
            "new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"])
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"])
        return new_york_city

    elif day == "noday" and month != "nomonth" and city == "Washington":
        washington = pd.read_csv(
            "washington.csv")
        washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.month
        washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.month
        return washington

    elif day != "noday" and month == "nomonth" and city == "Washington":
        washington = pd.read_csv(
            "washington.csv")
        washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.dayofyear
        washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.dayofyear
        return washington
    elif day == "noday" and month == "nomonth" and city == "Washington":
        washington = pd.read_csv(
            "washington.csv")
        washington["Start Time"] = pd.to_datetime(washington["Start Time"])
        washington["End Time"] = pd.to_datetime(washington["End Time"])
        return washington

# analysing popular Destination regarding to city / day / month which are selected by user


def populardestination(city_converter, day, month):

    if day == "noday" and month == "nomonth":

        populardestination = city_converter(city, day, month).groupby(["Start Station", "End Station"]
                                                                      ).size().reset_index(name="Counts")
        maxcountofpopulardestination = populardestination["Counts"].values.argmax()
        print("The Most Popular Destination In City Of {} Is\n".format(
            city).upper(), populardestination.iloc[maxcountofpopulardestination])

    elif day == "noday" and month != "nomonth":

        populardestination = city_converter(city, day, month)[city_converter(
            city, day, month)["Start Time"] == month_to_int(month)]
        populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]
                                                          ).size().reset_index(name="Counts")
        maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
        print("The Most Popular Destination In City Of {} For The Start Month Of {} Is\n".format(
            city, month).upper(), populardestinationv1.iloc[maxcountofpopulardestination])

    elif day != "noday" and month == "nomonth":
        try:
            populardestination = city_converter(city, day, month)[
                city_converter(city, day, month)["Start Time"] == day]
            populardestinationv1 = populardestination.groupby(["Start Station", "End Station"]
                                                              ).size().reset_index(name="Counts")
            maxcountofpopulardestination = populardestinationv1["Counts"].values.argmax()
            print("The Most Popular Destination In City Of {} For The Start Day Of {} Is\n".format(
                city, day).upper(), populardestinationv1.iloc[maxcountofpopulardestination])
        except ValueError:  # some days have not data , to prevent program crash , exception has been made.
            print("No Record For Relevant Date\n".upper())


print(populardestination(city_converter, day, month))

# analysing trip duration by gender regarding to city / day / month which are selected by user


def totaltripbygender(city_converter, month, day):

    if day == "noday" and month == "nomonth":
        try:

            sumbygender = city_converter(city, day, month).groupby(
                "Gender").describe()["Trip Duration"]
            print("Stats Of Trip Duration By Gender In City Of {} Are\n".format(city).upper(), sumbygender)
        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())
    elif day == "noday" and month != "nomonth":
        try:

            gendersum = city_converter(city, day, month)[city_converter(
                city, day, month)["Start Time"] == month_to_int(month)]
            sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
            print("Stats Of Trip Duration By Gender In City Of {} For The Start Month Of {} Are\n".format(
                city, month).upper(), sumbygender)
        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())
    elif day != "noday" and month == "nomonths":
        try:
            gendersum = city_converter(city, day, month)[
                city_converter(city, day, month)["Start Time"] == day]
            sumbygender = gendersum.groupby("Gender").describe()["Trip Duration"]
            print("Stats Of Trip Duration By Gender In City Of {} For The Start Day Of {} Are\n".format(
                city, day).upper(), sumbygender)
        except ValueError:  # some days have not data , to prevent program crash , exception has been made.
            print("No Record For Relevant Date In Selected City".upper() +
                  " " + "Sorry: (".upper() + " Please Try Another Date\n".upper())

        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())


print(totaltripbygender(city_converter, month, day))

# analysing trip duration by birthyears regarding to city / day / month which are selected by user


def tripdurationbybirthyears(city_converter, month, day):

    if day == "noday" and month == "nomonth":
        try:

            tripdurationbybirthyears = city_converter(city, day, month).groupby("Birth Year").sum()[
                "Trip Duration"]
            tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
            print("Top 5 Trip Time Spent Regarding To Birth Years In City Of {} Are\n".format(
                city).upper(), tripdurationbybirthyears.head())
        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())
    elif day == "noday" and month != "nomonth":
        try:

            tripdurationbybirthyears = city_converter(city, day, month)[city_converter(
                city, day, month)["Start Time"] == month_to_int(month)]
            tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()[
                "Trip Duration"]
            tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
            print("Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Month Of {} Are\n".format(
                city, month).upper(), tripdurationbybirthyears.head())
        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())

    elif day != "noday" and month == "nomonth":
        try:
            tripdurationbybirthyears = city_converter(city, day, month)[
                city_converter(city, day, month)["Start Time"] == day]
            tripdurationbybirthyears = tripdurationbybirthyears.groupby("Birth Year").sum()[
                "Trip Duration"]
            tripdurationbybirthyears = tripdurationbybirthyears.sort_values(ascending=False)
            print("Top 5 Trip Time Spent Regarding To Birth Years In City Of {} For The Start Day Of {} Are\n".format(
                city, day).upper(), tripdurationbybirthyears.head())
        except ValueError:  # some days have not data , to prevent program crash , exception has been made.
            print("No Record For Relevant Date In Selected City".upper() +
                  " " + "Sorry: (".upper() + " Please Try Another Date\n".upper())
        # some data sources (like washington) do not contain gender info. to prevent program crash , exception has been made.
        except KeyError:
            print("No Gender Information In Selected City".upper() +
                  " " + "Sorry:(".upper() + " Please Try Another City\n".upper())


print(tripdurationbybirthyears(city_converter, month, day))

# analysing trip duration regarding user types regarding to city / day / month which have been selected by user


def usertype(city_converter, month, day):
    if day == "noday" and month == "nomonth":
        tripduration = city_converter(city, day, month).groupby("User Type").sum()["Trip Duration"]
        print("The Total Trip Duration Regarding To User types In City Of {} Are\n".format(
            city).upper(), tripduration)

    elif day == "noday" and month != "nomonth":
        tripdurationv1 = city_converter(city, day, month)[city_converter(
            city, day, month)["End Time"] == month_to_int(month)]
        tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
        print("The Total Trip Duration Regarding To User Types In City Of {} For The End Month Of {} Are\n".format(
            city, month).upper(), tripduration)

    elif day != "noday" and month == "nomonth":
        try:
            tripdurationv1 = city_converter(city, day, month)[
                city_converter(city, day, month)["End Time"] == day]
            tripduration = tripdurationv1.groupby("User Type").sum()["Trip Duration"]
            print("The Total Trip Duration Regarding To User Types In City Of {} For The End Day Of {} are\n".format(
                city, day).upper(), tripduration)
        except ValueError:
            print("No Record For Relevant Date\n".upper())


print(usertype(city_converter, month, day))

# Count of user types regarding to city / month / day which have been selected by user


def usertypesize(city_converter, month, day):
    if day == "noday" and month == "nomonth":
        countofusertypes = city_converter(city, day, month).groupby(
            "User Type").size()
        print("The Count Of User types In City Of {} Are\n".format(
            city).upper(), countofusertypes)

    elif day == "noday" and month != "nomonth":
        countofusertypesv1 = city_converter(city, day, month)[city_converter(
            city, day, month)["End Time"] == month_to_int(month)]
        countofusertypes = countofusertypesv1.groupby("User Type").size()
        print("The Count Of User Types In City Of {} For The End Month Of {} Are\n".format(
            city, month).upper(), countofusertypes)

    elif day != "noday" and month == "nomonth":
        try:
            countofusertypesv1 = city_converter(city, day, month)[
                city_converter(city, day, month)["End Time"] == day]
            countofusertypes = countofusertypesv1.groupby("User Type").size()
            print("The Count Of User Types In City Of {} For The End Day Of {} are\n".format(
                city, day).upper(), countofusertypes)
        except ValueError:
            print("No Record For Relevant Date\n".upper())


print(usertypesize(city_converter, month, day))


def starttime_properties_month(city):
    if city == "Chicago":
        chicago = pd.read_csv(
            "chicago.csv")
        chicago["Start Time"] = pd.to_datetime(chicago["Start Time"]).dt.month
        chicago["End Time"] = pd.to_datetime(chicago["End Time"]).dt.month
        chicagov2 = chicago.groupby("Start Time").size().reset_index(name="Counts")
        maxofmonth = chicagov2["Counts"].values.argmax()
        monthnumber = chicagov2["Start Time"].iloc[maxofmonth]
        print("Most Occured Month For Start Time In Chicago Is", calendar.month_name[monthnumber])
    elif city == "New York City":
        new_york_city = pd.read_csv(
            "new_york_city.csv")
        new_york_city["Start Time"] = pd.to_datetime(new_york_city["Start Time"]).dt.month
        new_york_city["End Time"] = pd.to_datetime(new_york_city["End Time"]).dt.month
        new_york_cityv2 = new_york_city.groupby("Start Time").size().reset_index(name="Counts")
        maxofmonth = new_york_cityv2["Counts"].values.argmax()
        monthnumber = new_york_cityv2["Start Time"].iloc[maxofmonth]
        print("Most Occured Month For Start Time In New York City Is",
              calendar.month_name[monthnumber])
    elif city == "Washington":
        washington = pd.read_csv(
            "washington.csv")
        washington["Start Time"] = pd.to_datetime(washington["Start Time"]).dt.month
        washington["End Time"] = pd.to_datetime(washington["End Time"]).dt.month
        washingtonv2 = washington.groupby("Start Time").size().reset_index(name="Counts")
        maxofmonth = washingtonv2["Counts"].values.argmax()
        monthnumber = washingtonv2["Start Time"].iloc[maxofmonth]
        print("Most Occured Month For Start Time In Washington Is",
              calendar.month_name[monthnumber])


print(starttime_properties_month(city))

print("\nThank You - See Ya Again\n")
