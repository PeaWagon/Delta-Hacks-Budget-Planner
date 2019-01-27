from budgeter.userlist import UserDataBase
user = UserDataBase(1000, 100)
class DataBase_stores(object):
    def __init__(self, store_name):
        self.Customs = user.UserList
        self.store_name = store_name
        self.userList = []
        self.getUser()
        self.info = self.set_up()
	
    def getUser(self):
        for users in self.Customs:
            or stores in users.data["Company Name"]:
                if stores == self.store_name:
                    self.userList.append(users)
        return 

    def getNumUser(self):
        if len(self.userList)==0:
            return 0
        return len(self.userList)		
    def getAmount(self):
        if self.userList == []:
            return 0
        amount = 0
        for users in self.userList:
            amount_index = users.data["Company Name"].index(self.store_name)
            amount += users.data["Amount"][amount_index]
        return amount
    def getAverage(self):
        if self.userList == []:
            return 0
        return self.getAmount()/len(self.userList)
    def getFrequent(self):
        if self.userList == []:
            return "No one buys it"
        yearly = 0
        monthly = 0
        for users in self.userList:
            if users.data["is_yearly"]:
                yearly+=1
            else:
                monthly+=1
        return "Yearly: " + str(yearly) + "\n" + "Monthly: " + str(monthly)
    def set_up(self):
            info = {
            "store name": self.store_name,
                "user_list": self.userList,
                "user_num": self.getNumUser(),
                "amount": self.getAmount(),
                "average amount": self.getAverage(),
                "Frequent": self.getFrequent()
            }
            return info
