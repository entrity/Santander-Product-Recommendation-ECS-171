setwd('E:/Study/ECS171/Project')
load('clean_data_pre_train.rda')


library(dplyr)
D = D %>% 
  arrange(ncodpers,fecha_dato)

D$ind_nomina_ult1[is.na(D$ind_nomina_ult1)]=0
D$ind_nom_pens_ult1[is.na(D$ind_nom_pens_ult1)]=0

product = D[,14:37]
product_new1 = product[2:nrow(product),1:12]-product[1:(nrow(product)-1),1:12]
product_new2 = product[2:nrow(product),13:24]-product[1:(nrow(product)-1),13:24]
product_new = cbind(product_new1,product_new2)
rm(product_new1,product_new2,product)
#product_new = rbind(product[1,],product_new)
product_new = rbind(product_new,rep(0,24))
#fix na of the last 2 and 3 product
#product_new$ind_nom_pens_ult1[is.na(product_new$ind_nom_pens_ult1)]=0
#product_new$ind_nomina_ult1[is.na(product_new$ind_nomina_ult1)]=0

#Covert <0 to 0
for (i in 1:24){
  product_new[,i][product_new[,i]<0]=0
}

#Substitude the last row of each one with 0 vector
index=duplicated(D$ncodpers)
index_last = index[-1]
index_last = c(index_last,FALSE)
rm(D,index)
#product_new[!index_last,]=matrix(0, 941043, 24)
#product_new1 = product_new[1:6000000,]
#product_new2 = product_new[6000001:nrow(product_new),]
#index_last1 = index_last[1:6000000]
#product_new1[!index_last1,]=matrix(0,387803,24)
#table(index_last[1:600000])
#product_new[!index,1:12]=first_month[,1:12]
#product_new[!index,13:24]=first_month[,13:24]

#Convert to 1 vector
#response1 = max.col(product_new[1:5000000,],ties.method="random")
#response = max.col(product_new[5000000,],ties.method="random")

#Select the rows have change
sum1 = rowSums(product_new[1:4000000,],na.rm = TRUE)
sum2 = rowSums(product_new[4000001:8000000,],na.rm = TRUE)
sum3 = rowSums(product_new[8000001:12000000,],na.rm = TRUE)
sum4 = rowSums(product_new[12000001:nrow(product_new),],na.rm = TRUE)
sum = c(sum1,sum2,sum3,sum4)
rm(sum1,sum2,sum3,sum4)
index_1 = sum>0
response_1 = max.col(product_new[index_1,],ties.method="random")
response = rep(0,times=nrow(product_new))
response[index_1]=response_1

#Substitude the last month with 0
response[!index_last]=0

save(response,file = 'response.rda')
write.csv(response,file = 'response.csv',row.names = FALSE)

save(product_new,file = 'product_new.rda')
write.csv(product_new,file = 'product_new.csv',row.names = FALSE)


