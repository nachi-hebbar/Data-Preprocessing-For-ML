import sklearn
import pandas as pd
import matplotlib.pyplot as plt
housing=pd.read_csv(r"C:\Users\Lenovo\Downloads\housing\housing.csv")
#print(housing.info())
housing.hist(bins=50,figsize=(20,15))
#plt.show()
corr_matrix=housing.corr()
#print(corr_matrix["median_house_value"].sort_values(ascending=False))
housing.plot(kind="scatter",x="longitude",y="latitude",alpha=0.1,s=housing["population"]/100,label="population",c="median_house_value",cmap=plt.get_cmap("jet"),colorbar=True)
plt.legend()
plt.show()
