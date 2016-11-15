setwd('E:/Study/ECS171/Project')
load('D_minus_rows.rda')

#Drop some variables
name = names(D)
D=D[,-c(5,7,10,11,12,15,18,19,20,21)]

#covert to numeric data
D$ind_empleado=as.numeric(D$ind_empleado)
#> table(D$ind_empleado,exclude = NULL)
#2        3        4        5        6     <NA> 
#  2492     3566     2523 13610977       17        0 

D$pais_residencia=as.numeric(D$pais_residencia)
#From 2 to 119, No NA

D$age=as.numeric(as.character(D$age))
#No NA
#quantile(D$age,0.99)
#99% 
#88
#Delete age>88
D=D[D$age<=88,]

#table(D$ind_nuevo)
#0        1 
#12808368   811207

D$antiguedad=as.numeric(as.character(D$antiguedad))
#median(D$antiguedad) is 50
#Change antiguated = -999999 to 50
D$antiguedad[D$antiguedad==-999999]=50

D$tiprel_1mes = as.numeric(D$tiprel_1mes)
#            A       I       N       P       R 
#  121913 6133834 7225855       4    4637     866 
#convert to 1-6

D$indresi=as.numeric(D$indresi)
#N        S    
# 65555 13421554
#N is 2,S is 3


#D$conyuemp, most of people is NA, remove this variable
D = D[,-10]

D$canal_entrada=as.numeric(D$canal_entrada)

#D$ind_actividad_cliente
#0       1    
#7298639 6188470

#Fix NA of renta by mean
D$renta[is.na(D$renta)]=mean(D$renta,na.rm = TRUE)

D$segmento = as.numeric(D$segmento)
#Null          01 - TOP  02 - PARTICULARES 03 - UNIVERSITARIO
#159192             553912            7838426            4935579

D$ind_nomina_ult1[is.na(D$ind_nomina_ult1)]=0
D$ind_nom_pens_ult1[is.na(D$ind_nom_pens_ult1)]=0

save(D,file='clean_data_pre_train.rda')
write.csv(D, file = "clean_data_pre_train.csv", row.names = FALSE)

#Creat the training data
D = D[,c(-1,-2)]
save(D,file='clean_data_train.rda')
write.csv(D, file = "clean_data_train.csv", row.names = FALSE)
