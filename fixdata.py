import pandas as pd

train = pd.read_csv('train_ver2.csv')
head = train.head()
train.shape

#delete dead people which have 34762 rows
data =  train[train.indfall != 'S']
# fill NAs by 'N' for indfall variable
data.loc[data.indfall.isnull(),'indfall'] = 'N'
#modify extreme values of age variable using median values based on different group,say [18,30] and [30,100]

data['age'] = pd.to_numeric(data['age'],errors = 'coerce')
data.loc[data.age < 18,"age"] = data.loc[(data.age >= 18) & (data.age <= 30),"age"].median(skipna = True)
data.loc[data.age > 100,"age"] = data.loc[(data.age > 30) & (data.age <= 100),"age"].median(skipna=True)
data["age"].fillna(data["age"].median(),inplace=True)
data["age"] = data["age"].astype(int)

data.cod_prov.mode() #the mode of cod_prov column is 28
data["cod_prov"].fillna(28,inplace=True)
#assign missing renta using median under different region
grouped = data.groupby("cod_prov").agg({"renta":lambda x: x.median(skipna=True)}).reset_index()
new_incomes = pd.merge(data,grouped,how="inner",on="cod_prov").loc[:, ["cod_prov","renta_y"]]
new_incomes = new_incomes.rename(columns={"renta_y":"renta"}).sort_values("renta").sort_values("cod_prov")
data.sort_values("cod_prov",inplace=True)
data = data.reset_index()
new_incomes = new_incomes.reset_index()

data.loc[data.renta.isnull(),"renta"] = new_incomes.loc[data.renta.isnull(),"renta"].reset_index()
data.loc[data.renta.isnull(),"renta"] = data.loc[data.renta.notnull(),"renta"].median()
data.loc[data.sexo.isnull(),"sexo"] = 'V'

x.drop(['Unnamed: 0','index'],axis=1).to_csv('fixdata.csv')
#x.to_csv('fixdata.csv')

x = pd.read_csv('fixdata.csv')
x.shape

del x['Unnamed: 0']

result = x.sort(['fecha_dato'])



