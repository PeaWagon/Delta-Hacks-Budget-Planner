
class UserDataBase(object):
	def __init__(self, user_capacity, transaction):
		self.UserList = self.add_user()
		self.userNum = user_capacity
		self.transaction = transaction
		
	def add_user(self):
		print(self.userNum)
		a = []
		for i in range(self.userNum):
			user = create_user()
			new = UserData(user.username)
			a.append(new)
		return a
a = UserDataBase(10, 10)
