from budgeter.userdata import UserData
from budgeter.create_user import create_user
#from budgeter.DataBase_stores import DataBase_stores
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
