from budgeter.DataBase_stores import DataBase_stores
from budgeter.analyse_stores import analyse_stores
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

store_fortino = DataBase_stores("Fortinos")
store_best_bus = DataBase_stores("Best Buy")
store_HomeDep = DataBase_stores("Home Depot")
store_coffee_time = DataBase_stores("Coffee Time")

x = np.arange(4)
money = [store_fortino.info["average amount"], store_best_bus.info["average amount"], store_HomeDep.info["average amount"], store_coffee_time.info["average amount"]]

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
plt.bar(x, money)
plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))
plt.show()