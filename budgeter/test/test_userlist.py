
from budgeter.userlist import UserDataBase

def test_UserDataBase():
    # make a database of 1000 users with 100 transactions each
    mydb = UserDataBase(1000, 100)
    mydb.write_database()

def test_UserDataBase_write_database():
    mydb = UserDataBase(10, 30)
    mydb.write_database("small_database.csv")

def test_UserDataBase_read_database():
    # make an empty database
    mydb = UserDataBase(0,0)
    mydb.read_database("small_database.csv")
    assert mydb.num_users == 10
    assert mydb.user_list[0].num_transactions == 30
    

if __name__ == "__main__":
    test_UserDataBase()
    test_UserDataBase_write_database()
    test_UserDataBase_read_database()
