

"""Create users and transactions randomly."""

import random

from budgeter.read_stores import get_store_data
from budgeter.userdata import UserData

def create_transaction():
    """Creates a random transaction."""
      
    # fill in basic purchase data
    item = {"Year": random.randint(2012,2019),
            "Month": random.choice(["January",
                     "February", "March", "April",
                     "May", "June", "July", "August",
                     "September", "October",
                     "November", "December"]),
            "Day": None,
            "Company Name": None,
            "Category": None,
            # maybe later make the amount more
            # reasonable based on store category
            "Amount": random.uniform(0.0, 500.0),
            "is_yearly": False,
            "is_monthly": False
            }

    # set category name
    store_data = get_store_data()
    categories = list(store_data.keys())
    item["Category"] = random.choice(categories)

    # set store name
    stores = store_data[item["Category"]]
    item["Company Name"] = random.choice(stores)

    # determine yearly/monthly purchase
    # most purchases will not be bills, so chance
    # should be small
    chance = 0.02 # chance to make yearly/monthly
    choice = random.randint(1, 100)
    if choice == 1 or choice == 2:
        ym = random.choice(["year", "month"])
        if ym == "year":
            data["is_yearly"] = True
        else:
            data["is_monthly"] = True

    # determine if year is leap year
    leap = False
    year = item["Year"]
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    else:
        leap = True

    # determine day of purchase
    if item["Month"] in ("September", "April", "June", "November"):
        item["Day"] = random.randint(1,30)
    elif item["Month"] == "Feburary":
        if leap:
            item["Day"] = random.randint(1,29)
        else:
            item["Day"] = random.randint(1,28)
    else:
        item["Day"] = random.randint(1,31)
    return item

def create_username():
    """Creates a random username."""
    # initialise username
    username = ""

    # how many characters for the username
    min_length = 3
    max_length = 8
    len_username = random.randint(min_length, max_length)

    # which characters can be in the username
    # ord("A") to ord("Z") and ord("a") to ord("z")
    valid = [i for i in range(65, 91)] + [j for j in range(97, 123)]

    # generate username
    for i in range(len_username):
        char = random.choice(valid)
        username += chr(char)
    return username

def create_user(num_transactions):
    user = UserData(create_username())
    for i in range(num_transactions):
        user.add_item(create_transaction())
    return user
    
