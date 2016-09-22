# 5ml equals 1 teaspoon


def conversion(tsp, mil):
    ml = round((float(tsp) * .20), 1)
    tee = round((float(mil) * 5), 1)
    return ml or tee

print("This program will convert milliliters to teaspoons or teaspoons to milliliters \n")
milli = raw_input("How many milliliters? \n")
teaspoon = raw_input("How many teaspoons \n")


if teaspoon == "0":
    Milli = conversion(milli, 0)
    print(milli + " milliliters is equal to " + str(Milli) + " teaspoons")
elif milli == "0":
    Tee = conversion(0, teaspoon)
    print(teaspoon + " teaspoons is equal to " + str(Tee) + " milliliters")
elif teaspoon != "0" or milli != "0":
    print("Error!!! Please enter only 1 positive value in either milliliter or teaspoons. \n Enter zero for the other value")
