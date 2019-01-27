

from budgeter.userdata import UserData
from budgeter.create_user import create_user

def test_UserData():
    user = UserData("test")
    user.add_item({"Year": 2019,
                   "Month": "January",
                    "Day": 27,
                    "Company Name": "Tim Hortons",
                    "Category": "Coffee Shops",
                    "Amount": 5000,
                    "is_yearly": True,
                    "is_monthly": False
                   })
    assert user.num_transactions == 1
    assert user[0] == [2019, "January", 27,
                       "Tim Hortons", "Coffee Shops",
                       5000, True, False]

def test_UserData_monthly_expenses():
    user = create_user(1000)
    exp_ind = user.monthly_expenses("January", 2019)
    for xpi in exp_ind:
        assert "January" in user[xpi]
        assert 2019 in user[xpi]

def test_UserData_monthly_piegraph():
    user = create_user(500)
    user.monthly_piegraph("March", 2018)
    

if __name__ == "__main__":
    test_UserData()
    test_UserData_monthly_expenses()
    test_UserData_monthly_piegraph()
