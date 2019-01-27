
import os
import csv

from budgeter.userdata import UserData
from budgeter.create_user import create_user, create_username

# where the data is stored
data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

class UserDataBase(object):

    def __init__(self, user_capacity, transaction):
        """Create a database of users randomly.

        Parameters
        ----------
        user_capacity : int
            The number of users to make.
        transaction : int
            The number of transactions to make
            per user.

        """
        self.num_users = user_capacity
        self.user_list = [create_user(transaction) for i in range(user_capacity)]

    def write_database(self, out="userdatabase.csv"):
        outputfile = os.path.join(data_dir, out)
        with open(outputfile, "w") as f:
            fo = csv.writer(f)
            try:
                fo.writerow(self.user_list[0].data.keys())
            except IndexError:
                # no users!
                pass
            for user in self.user_list:
                fo.writerow([user.username])
                for t in range(user.num_transactions):
                    fo.writerow(user[t])

    def read_database(self, inp="userdatabase.csv"):
        inputfile = os.path.join(data_dir, inp)
        with open(inputfile, "r") as f:
            fi = csv.reader(f)
            transaction = []
            # placeholder for UserData object
            user = None
            header = True
            for row in fi:
                if header:
                    header = False
                    continue
                # check if line is a username
                if len(row) == 1:
                    # if user is not empty
                    if user is not None:
                        self.user_list.append(user)
                        self.num_users += 1
                    # create new user
                    user = UserData(row[0])
                # add transaction to current user
                else:
                    newtrs = user.setup_data()
                    newtrs["Year"] = row[0]
                    newtrs["Month"] = row[1]
                    newtrs["Day"] = row[2]
                    newtrs["Company Name"] = row[3]
                    newtrs["Category"] = row[4]
                    newtrs["Amount"] = row[5]
                    newtrs["is_yearly"] = row[6]
                    newtrs["is_monthly"] = row[7]
                    user.add_item(newtrs)
            # add last user
            if user is not None:
                self.user_list.append(user)
                self.num_users += 1

