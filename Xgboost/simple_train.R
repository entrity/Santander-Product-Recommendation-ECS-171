#Simplify the training data set
setwd('E:/Study/ECS171/Project')
load('clean_data_train.rda')
load('response.rda')

#For pais_residencia, if Spain 1, not Spain 0
train$pais_residencia=train$pais_residencia==38

#For age, cut into 5 group
#quantile(train$age,c(0.2,0.4,0.6,0.8))
#20% 40% 60% 80% 
 # 23  31  43  53 
train$age[train$age<=23]=0
train$age[train$age>23 & train$age<=31]=1
train$age[train$age>31 & train$age<=43]=2
train$age[train$age>43 & train$age<=53]=3
train$age[train$age>53]=4

#For renta(customer seniority)
#quantile(train$renta,c(0.2,0.4,0.6,0.8))
#20% 40% 60% 80% 
#18  38  86 152
train$renta[train$renta<=18]=0
train$renta[train$renta>18 & train$renta<=38]=1
train$renta[train$renta>38 & train$renta<=86]=2
train$renta[train$renta>86 & train$renta<=152]=3
train$renta[train$renta>152]=4

#For indresi, drop, same as the "pais_residencia" info now
train = train[,-7]

#For canal_entrada, delete temporally, too complex and may useless
train = train[,-7]

#For tiprel_1mes, drop, because it is silimar to ind_actividad_cliente
train = train[,-6]

#For renta
#quantile(train$renta,c(0.2,0.4,0.6,0.8))
#20%       40%       60%       80% 
#68766.63 102064.47 133876.54 155275.86
train$renta[train$renta<=68766]=0
train$renta[train$renta>68766 & train$renta<=102064]=1
train$renta[train$renta>102064 & train$renta<=133876]=2
train$renta[train$renta>133876 & train$renta<=155275]=3
train$renta[train$renta>155275]=4

#Combine response and train
train_res = cbind(train,response)
save(train_res,file='simple_train_response.rda')

#Make things more simple,only retain the response not 0 rows
train_res_no0 = train_res[train_res$response>0,]
train_res_no0$pais_residencia = as.numeric(train_res_no0$pais_residencia)
save(train_res_no0,file='simple_train_response_no0.rda')
write.csv(train_res_no0,file='simple_train_response_no0.csv',row.names = FALSE)
