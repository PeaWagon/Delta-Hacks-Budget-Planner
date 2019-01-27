from budgeter.userdata import UserData
from budgeter.create_user import create_user
class UserDataBase(object):
	def __init__(self, user_capacity, transaction):
		self.transaction = transaction
		self.userNum = user_capacity
		self.UserList = self.add_user()
		
	def add_user(self):
		a = []
		for i in range(self.userNum):
			user = create_user(self.transaction)
			a.append(user)
		return a
#a = UserDataBase(10, 10)
#print(a.UserList[0].data["is_yearly"])