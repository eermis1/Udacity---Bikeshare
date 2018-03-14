# Restart function


def citycheck():

    city = str(input("Hello User\n"
                     "Let's Explain Some US Bikeshare Data\n"
                     "Which City Would Like To Deep Dive\nPlease Enter; Chicago, New York City, Washington\n")).title()

    while city not in ("New York City", "Washington", "Chicago"):
        print("Incorrect Selection, Please Type 'Washington', 'New York City' or 'Chicago'")
        city = str(input()).title()
        print("Your Choice Is" + " " + str(city).title() + " " + "Evaluating...\n")

    else:
        print("\nYour Choice Is {} Which Is Included To My Program :) , Lets Continue...\n".format(
            str(city).title()))
        return city


print("seçtiğiniz şehir =", citycheck())
