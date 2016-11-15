install.packages("drat", repos = "https://cran.rstudio.com")
drat:::addRepo("dmlc")
install.packages("xgboost", repos="http://dmlc.ml/drat/", type ="source" )
require(xgboost)

set.seed(1)
#data(agaricus.train, package = "xgboost")
#ata(agaricus.test, package = "xgboost")
load('simple_train_response_no0.rda')
#train = agaricus.train
#test = agaricus.test

param = list('objective' = 'multi:softmax',
             'eval_metric' = 'mlogloss',
             'eta' = 1, 'max.depth' = 3,
             'num_class'=24)
#bst.cv =xgb.cv(params = param, data = as.matrix(train$data), label = train$label,
#               nfold=10,nrounds = 80)
plot(log(bst.cv$test.logloss.mean),type = 'l')

bst = xgboost(params = param, data = as.matrix(train_res_no0[,1:8]), 
              label = train_res_no0[,dim(train_res_no0)[2]]-1, 
              nrounds = 5, nthread = 2)
preds = predict(bst,as.matrix(train_res_no0[,1:8]))
head(preds)

names = dimnames(train_res_no0[, 1:8])[[2]]
trees = xgb.model.dt.tree(names, model = bst)
importance_matrix = xgb.importance(names, model = bst)
xgb.plot.importance(importance_matrix)
xgb.plot.tree(feature_names = names, model = bst, n_first_tree = 4)
