from budgeter.userlist import UserDataBase
from budgeter.read_stores import get_store_data
from budgeter.DataBase_stores import DataBase_stores

class analyse_stores:
	stores_List = get_store_data()	
	def __init__(self, category):
		self.category = category
		self.storesInCateg = self.stores_List[category]
		self.store_data = self.getData()
		
	
	def GetPrice(self):
		amountList = []
		for store in self.storesInCateg:
			Data_anal = DataBase_stores(store)
			amountList.append(Data_anal.info)
		new = sorted(amountList, key=lambda amount: float(amount['amount']), reverse=True)
		return new
	def cheapest(self):
		if self.GetPrice() == []:
			return "none"
		return self.GetPrice()[-1]["store name"]
	def expensive(self):
		if self.GetPrice() == []:
			return "none"
		return self.GetPrice()[0]["store name"]
	def getData(self):
		data = {
			"Most Economic": self.cheapest(),
			"Most Expensive": self.expensive(),
		}
		return data
a = analyse_stores("Clothing")
print(a.store_data["Most Economic"])