import userlist
class DataBase_stores(object):
	Users = userlist.UserDataBase(10)
	Customs = Users.UserList
	def __init__(self, store_name):
		self.store_name = store_name
		self.userList = []
		self.info = set_up()
	
	def getUser():
		for users in Customs:
			for stores in users.data["Company Name"]:
				if stores == self.store_name:
					self.userList.append(users)
		return 

	def getNumUser(self):
		return len(self.userList)		
	def getAmount(self):
		amount = 0
		for users in self.userList:
			amount_index = users.data["Company Name"].index(self.store_name)
			amount += users.data["Amount"][amount_index]
		return amount
	
	def getFrequent(self):
		yearly = 0
		monthly = 0
		for users in self.info["user_lst"]:
			if users.data["is_yearly"]:
				yearly+=1
			else:
				monthly+=1
		return "Yearly: " + str(yearly) + "\n" + "Monthly: " + str(monthly)
	def set_up(self):
			info = {
				"store name": self.store_name,
				"user_list": self.userList,
				"user_num": getNumUser(),
				"amount": getAmount(),
				"average amount": amount/len(self.userList),
				"Frequent": str
			}
			return info

					
		