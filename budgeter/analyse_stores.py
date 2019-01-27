import DataBase_stores
import userlist
import UserData
import read_stores
got_store_data
class analyse_stores:
	clients = userlist.UserDataBase(10)
	#the parameters of get_store_data
	stores_List = read_stores.get_store_data(cvsf)
	
	def __init__(self, category):
		self.category = category
		self.store_data = getData()
		self.storesInCateg = stores_List[category]
		
	def getData(self):
		data = {
			"Most Economic": str,
			"Most Expensive": str,
			"Most Popular": str,
		}
		return data
	
	def GetAmount(a):
		return a["amount"]
	
	def GetPrice(self):
		amountList = []
		for store in self.storesInCateg:
			Data_anal = DataBase_stores.DataBase_stores(store)
			amountList.append(Data_anal.info)
		new = sorted(amountList, reverse=True, key = GetAmount)
		self.store_data["Most Economic"] = new["store name"][-1] + str(new["average amount"]) 
		self.store_data["Most Expensive"] = new["store name"][0] + str(new["average amount"]) 
		return
		
		
			