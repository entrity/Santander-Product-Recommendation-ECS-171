import numpy as np
import pandas as pd
from sklearn import preprocessing, ensemble
from sklearn.metrics import confusion_matrix

data = pd.read_csv('flat_train.csv')

testdata = pd.read_csv('flat_test.csv')

# columns to be used as features
feature_cols = ["mode_resident_country","mode_sex","final_age", "mode_customer_type",
                "mode_province","last_inactive","mean_income","mode_segmentation",'first_saving',
                'sum_saving','first_guarantee', 'sum_guarantee', 'first_current', 'sum_current',
                'first_derivada', 'sum_derivada', 'first_payroll', 'sum_payroll','first_junior',
                'sum_junior', 'first_maspart', 'sum_maspart','first_part', 'sum_part',
                'first_partplus', 'sum_partplus',
       'first_stdep', 'sum_stdep', 'first_mtdep', 'sum_mtdep', 'first_ltdep',
       'sum_ltdep', 'first_eacct', 'sum_eacct', 'first_fund', 'sum_fund',
       'first_mortgage', 'sum_mortgage', 'first_pension', 'sum_pension',
       'first_loan', 'sum_loan', 'first_tax', 'sum_tax', 'first_credit',
       'sum_credit', 'first_security', 'sum_security', 'first_home',
       'sum_home', 'first_nompayroll', 'sum_nompayroll', 'first_nompension',
       'sum_nompension', 'first_debit', 'sum_debit']
target_cols = ['ind_ahor_fin_ult1','ind_aval_fin_ult1','ind_cco_fin_ult1','ind_cder_fin_ult1',
               'ind_cno_fin_ult1','ind_ctju_fin_ult1','ind_ctma_fin_ult1','ind_ctop_fin_ult1',
               'ind_ctpp_fin_ult1','ind_deco_fin_ult1','ind_deme_fin_ult1','ind_dela_fin_ult1',
               'ind_ecue_fin_ult1','ind_fond_fin_ult1','ind_hip_fin_ult1','ind_plan_fin_ult1',
               'ind_pres_fin_ult1','ind_reca_fin_ult1','ind_tjcr_fin_ult1','ind_valo_fin_ult1',
               'ind_viv_fin_ult1','ind_nomina_ult1','ind_nom_pens_ult1','ind_recibo_ult1']

X_train = data[feature_cols]
y_train = data[target_cols]

X_test = testdata[feature_cols]

X_train.mode_province = X_train.mode_province.astype('object')
X_test.mode_province = X_test.mode_province.astype('object')
X_train.last_inactive = X_train.last_inactive.astype('object')
X_test.last_inactive = X_test.last_inactive.astype('object')

#process multi-label category variables
for ind, col in enumerate(feature_cols):
    if X_train[col].dtype == 'object':
        lab = preprocessing.LabelEncoder()
        lab.fit(list(X_train[col].values) + list(X_test[col].values))
        temp_X_train = lab.transform(list(X_train[col].values)).reshape(-1,1)
        temp_X_test = lab.transform(list(X_test[col].values)).reshape(-1,1)
    else:
        temp_X_train = np.array(X_train[col]).reshape(-1,1)
        temp_X_test = np.array(X_test[col]).reshape(-1,1)
    if ind == 0:
        X_train_new = temp_X_train.copy()
        X_test_new = temp_X_test.copy()
    else:
        X_train_new = np.hstack([X_train_new,temp_X_train])
        X_test_new = np.hstack([X_test_new,temp_X_test])

y_train = y_train.astype('float16')
#y_test = y_test.astype('float16')

#fit randome forest
RF = ensemble.RandomForestClassifier(n_estimators = 100, max_depth = 10, min_samples_leaf = 10,
                                     n_jobs = 4, random_state = 2016)

# RF = ensemble.RandomForestClassifier(n_estimators = 100, max_depth = 10, min_samples_leaf = 10,
#                                      n_jobs = 4, random_state = 2016)
RF.fit(X_train_new,y_train)
#predict probs of customers buy that product
y_preds = np.array(RF.predict_proba(X_test_new))[:,:,1].T


#RF.score(X_test_new,y_test)

#predict if customers buy one product
#y_preds = np.array(RF.predict_proba(X_test_new))[:,:,1].T
y = np.array(RF.predict(X_test_new))

customers = {}

class customer:
    def __init__( self, sum_saving, sum_guarantee, sum_current, sum_derivada,
    sum_payroll, sum_junior, sum_maspart, sum_part, sum_partplus, sum_stdep,
    sum_mtdep, sum_ltdep, sum_eacct, sum_fund, sum_mortgage, sum_pension,
    sum_loan, sum_tax, sum_credit, sum_security, sum_home, sum_nompayroll,
    sum_nompension, sum_debit ):
        self.products = [sum_saving == 0, sum_guarantee == 0, sum_current == 0,
        sum_derivada == 0, sum_payroll == 0, sum_junior == 0, sum_maspart == 0,
        sum_part == 0, sum_partplus == 0, sum_stdep == 0, sum_mtdep == 0,
        sum_ltdep == 0, sum_eacct == 0, sum_fund == 0, sum_mortgage == 0,
        sum_pension == 0, sum_loan == 0, sum_tax == 0, sum_credit == 0,
        sum_security == 0, sum_home == 0, sum_nompayroll == 0,
        sum_nompension == 0, sum_debit == 0]
    def new_products( self, products ):
        things = []
        for ind, thing in enumerate(self.products):
            if thing == False and products[ind] == 1: #new products
                things.append( str( target_cols[ind] ) )
        return ' '.join( things )

for i in range( 0, len( data['custo'] ) ):
    customers[data['custo'][i]] = customer( data['sum_saving'][i],
    data['sum_guarantee'][i], data['sum_current'][i],
    data['sum_derivada'][i], data['sum_payroll'][i], data['sum_junior'][i],
    data['sum_maspart'][i], data['sum_part'][i], data['sum_partplus'][i],
    data['sum_stdep'][i], data['sum_mtdep'][i], data['sum_ltdep'][i],
    data['sum_eacct'][i], data['sum_fund'][i], data['sum_mortgage'][i],
    data['sum_pension'][i], data['sum_loan'][i], data['sum_tax'][i],
    data['sum_credit'][i], data['sum_security'][i], data['sum_home'][i],
    data['sum_nompayroll'][i], data['sum_nompension'][i], data['sum_debit'][i] )

with open('submission.csv', 'w') as outf:
    outf.write('ncodpers,added_products')
    for ind, thing in enumerate( y ):
        outf.write( str( testdata['custo'][ind] ) + ',' + customers[testdata['custo'][ind]].new_products( thing ) + '\n' )

# conf_mat = []
#
# for i in range(y.shape[1]):
#     conf_mat.append(confusion_matrix(y_test.iloc[:,i],y[:,i]))
#
#
# from sklearn.metrics import roc_curve
# from matplotlib import pyplot as plt
#
# num_plots = 24
# colormap = plt.cm.gist_ncar
# plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0,0.9,num_plots)])
# for i in range(y.shape[1]):
#     fpr,tpr,thresholds = roc_curve(y_test.iloc[:,i], y_preds[:,i], pos_label = 1)
#     plt.plot(fpr,tpr)
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC Curve')
# plt.legend(target_cols,ncol = 3, loc = 'lower right',fontsize = 'small')
# plt.show()
