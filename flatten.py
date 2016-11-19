import csv
import time

TRAIN_DATA_FILE = 'fix_data.csv'
TEST_DATA_FILE = 'fix_test.csv'
TRAIN_OUTPUT_FILE = 'flat_train.csv'
TEST_OUTPUT_FILE = 'flat_test.csv'

class Customer:
    def __init__(self):
        self.custo = -1

        #Demographic
        self.mode_ind_employee = -1
        self.mode_resident_country = -1
        self.mode_sex = -1
        self.final_age = -1
        self.first_cust_start_date = -1
        self.mode_customer_type = -1
        self.mode_empl_spouse = -1
        self.mode_join_channel = -1
        self.mode_province = -1
        self.last_inactive = -1
        self.months_last_inactive = -1
        self.mean_income = -1
        self.mode_segmentation = -1
        self.final_segmentation = -1

        #Behavioral
        self.first_saving = -1
        self.sum_saving = 0
        self.first_guarantee = -1
        self.sum_guarantee = 0
        self.first_current = -1
        self.sum_current = 0
        self.first_derivada = -1
        self.sum_derivada = 0
        self.first_payroll = -1
        self.sum_payroll = 0
        self.first_junior = -1
        self.sum_junior = 0
        self.first_maspart = -1
        self.sum_maspart = 0
        self.first_part = -1
        self.sum_part = 0
        self.first_partplus = -1
        self.sum_partplus = 0
        self.first_stdep = -1
        self.sum_stdep = 0
        self.first_mtdep = -1
        self.sum_mtdep = 0
        self.first_ltdep = -1
        self.sum_ltdep = 0
        self.first_eacct = -1
        self.sum_eacct = 0
        self.first_fund = -1
        self.sum_fund = 0
        self.first_mortgage = -1
        self.sum_mortgage = 0
        self.first_pension = -1
        self.sum_pension = 0
        self.first_loan = -1
        self.sum_loan = 0
        self.first_tax = -1
        self.sum_tax = 0
        self.first_credit = -1
        self.sum_credit = 0
        self.first_security = -1
        self.sum_security = 0
        self.first_home = -1
        self.sum_home = 0
        self.first_nompayroll = -1
        self.sum_nompayroll = 0
        self.first_nompension = -1
        self.sum_nompension = 0
        self.first_debit = -1
        self.sum_debit = 0

        #Response Variables
        self.ind_ahor_fin_ult1 = -1
        self.ind_aval_fin_ult1 = -1
        self.ind_cco_fin_ult1 = -1
        self.ind_cder_fin_ult1 = -1
        self.ind_cno_fin_ult1 = -1
        self.ind_ctju_fin_ult1 = -1
        self.ind_ctma_fin_ult1 = -1
        self.ind_ctop_fin_ult1 = -1
        self.ind_ctpp_fin_ult1 = -1
        self.ind_deco_fin_ult1 = -1
        self.ind_deme_fin_ult1 = -1
        self.ind_dela_fin_ult1 = -1
        self.ind_ecue_fin_ult1 = -1
        self.ind_fond_fin_ult1 = -1
        self.ind_hip_fin_ult1 = -1
        self.ind_plan_fin_ult1 = -1
        self.ind_pres_fin_ult1 = -1
        self.ind_reca_fin_ult1 = -1
        self.ind_tjcr_fin_ult1 = -1
        self.ind_valo_fin_ult1 = -1
        self.ind_viv_fin_ult1 = -1
        self.ind_nomina_ult1 = -1
        self.ind_nom_pens_ult1 = -1
        self.ind_recibo_ult1 = -1

    # def init(self, custo, mode_ind_employee, mode_resident_country, mode_sex,
    # final_age, first_cust_start_date, mode_customer_type, mode_empl_spouse,
    # mode_join_channel, mode_province, last_inactive, months_last_inactive,
    # mean_income, mode_segmentation, final_segmentation, first_saving,
    # sum_saving, first_guarantee, sum_guarantee, first_current, sum_current,
    # first_derivada, sum_derivada, first_payroll, sum_payroll, first_junior,
    # sum_junior, first_maspart, sum_maspart, first_part, sum_part,
    # first_partplus, sum_partplus, first_stdep, sum_stdep, first_mtdep,
    # sum_mtdep, first_ltdep, sum_ltdep, first_eacct, sum_eacct, first_fund,
    # sum_fund, first_mortgage, sum_mortgage, first_pension, sum_pension,
    # first_loan, sum_loan, first_tax, sum_tax, first_credit, sum_credit,
    # first_security, sum_security, first_home, sum_home, first_nompayroll,
    # sum_nompayroll, first_nompension, sum_nompension, first_debit, sum_debit,
    # ind_ahor_fin_ult1, ind_aval_fin_ult1, ind_cco_fin_ult1, ind_cder_fin_ult1,
    # ind_cno_fin_ult1, ind_ctju_fin_ult1, ind_ctma_fin_ult1, ind_ctop_fin_ult1,
    # ind_ctpp_fin_ult1, ind_deco_fin_ult1, ind_deme_fin_ult1, ind_dela_fin_ult1,
    # ind_ecue_fin_ult1, ind_fond_fin_ult1, ind_hip_fin_ult1, ind_plan_fin_ult1,
    # ind_pres_fin_ult1, ind_reca_fin_ult1, ind_tjcr_fin_ult1, ind_valo_fin_ult1,
    # ind_viv_fin_ult1, ind_nomina_ult1, ind_nom_pens_ult1, ind_recibo_ult1):
    #     self.custo = custo
    #
    #     #Demographic
    #     self.mode_ind_employee = mode_ind_employee
    #     self.mode_resident_country = mode_resident_country
    #     self.mode_sex = mode_sex
    #     self.final_age = final_age
    #     self.first_cust_start_date = first_cust_start_date
    #     self.mode_customer_type = mode_customer_type
    #     self.mode_empl_spouse = mode_empl_spouse
    #     self.mode_join_channel = mode_join_channel
    #     self.mode_province = mode_province
    #     self.last_inactive = last_inactive
    #     self.months_last_inactive = months_last_inactive
    #     self.mean_income = mean_income
    #     self.mode_segmentation = mode_segmentation
    #     self.final_segmentation = final_segmentation
    #
    #     #Behavioral
    #     self.first_saving = first_saving
    #     self.sum_saving = sum_saving
    #     self.first_guarantee = first_guarantee
    #     self.sum_guarantee = sum_guarantee
    #     self.first_current = first_current
    #     self.sum_current = sum_current
    #     self.first_derivada = first_derivada
    #     self.sum_derivada = sum_derivada
    #     self.first_payroll = first_payroll
    #     self.sum_payroll = sum_payroll
    #     self.first_junior = first_junior
    #     self.sum_junior = sum_junior
    #     self.first_maspart = first_maspart
    #     self.sum_maspart = sum_maspart
    #     self.first_part = first_part
    #     self.sum_part = sum_part
    #     self.first_partplus = first_partplus
    #     self.sum_partplus = sum_partplus
    #     self.first_stdep = first_stdep
    #     self.sum_stdep = sum_stdep
    #     self.first_mtdep = first_mtdep
    #     self.sum_mtdep = sum_mtdep
    #     self.first_ltdep = first_ltdep
    #     self.sum_ltdep = sum_ltdep
    #     self.first_eacct = first_eacct
    #     self.sum_eacct = sum_eacct
    #     self.first_fund = first_fund
    #     self.sum_fund = sum_fund
    #     self.first_mortgage = first_mortgage
    #     self.sum_mortgage = sum_mortgage
    #     self.first_pension = first_pension
    #     self.sum_pension = sum_pension
    #     self.first_loan = first_loan
    #     self.sum_loan = sum_loan
    #     self.first_tax = first_tax
    #     self.sum_tax = sum_tax
    #     self.first_credit = first_credit
    #     self.sum_credit = sum_credit
    #     self.first_security = first_security
    #     self.sum_security = sum_security
    #     self.first_home = first_home
    #     self.sum_home = sum_home
    #     self.first_nompayroll = first_nompayroll
    #     self.sum_nompayroll = sum_nompayroll
    #     self.first_nompension = first_nompension
    #     self.sum_nompension = sum_nompension
    #     self.first_debit = first_debit
    #     self.sum_debit = sum_debit
    #
    #     #Response Variables
    #     self.ind_ahor_fin_ult1 = ind_ahor_fin_ult1
    #     self.ind_aval_fin_ult1 = ind_aval_fin_ult1
    #     self.ind_cco_fin_ult1 = ind_cco_fin_ult1
    #     self.ind_cder_fin_ult1 = ind_cder_fin_ult1
    #     self.ind_cno_fin_ult1 = ind_cno_fin_ult1
    #     self.ind_ctju_fin_ult1 = ind_ctju_fin_ult1
    #     self.ind_ctma_fin_ult1 = ind_ctma_fin_ult1
    #     self.ind_ctop_fin_ult1 = ind_ctop_fin_ult1
    #     self.ind_ctpp_fin_ult1 = ind_ctpp_fin_ult1
    #     self.ind_deco_fin_ult1 = ind_deco_fin_ult1
    #     self.ind_deme_fin_ult1 = ind_deme_fin_ult1
    #     self.ind_dela_fin_ult1 = ind_dela_fin_ult1
    #     self.ind_ecue_fin_ult1 = ind_ecue_fin_ult1
    #     self.ind_fond_fin_ult1 = ind_fond_fin_ult1
    #     self.ind_hip_fin_ult1 = ind_hip_fin_ult1
    #     self.ind_plan_fin_ult1 = ind_plan_fin_ult1
    #     self.ind_pres_fin_ult1 = ind_pres_fin_ult1
    #     self.ind_reca_fin_ult1 = ind_reca_fin_ult1
    #     self.ind_tjcr_fin_ult1 = ind_tjcr_fin_ult1
    #     self.ind_valo_fin_ult1 = ind_valo_fin_ult1
    #     self.ind_viv_fin_ult1 = ind_viv_fin_ult1
    #     self.ind_nomina_ult1 = ind_nomina_ult1
    #     self.ind_nom_pens_ult1 = ind_nom_pens_ult1
    #     self.ind_recibo_ult1 = ind_recibo_ult1

    def getTrainRow(self):
        #self.mode_ind_employee = mode(self.ind_employee)
        self.mode_resident_country = mode(self.resident_country)
        self.mode_sex = mode(self.sex)
        self.mode_customer_type = mode(self.customer_type)
        #self.mode_empl_spouse = mode(self.empl_spouse)
        #self.mode_join_channel = mode(self.join_channel)
        self.mode_province = mode(self.province)
        self.last_inactive = last_inactive_period(self.months_inactive)
        self.months_last_inactive = months_last_inactive_period(self.months_inactive)
        self.mean_income = mean(self.income)
        self.mode_segmentation = mode(self.segmentation)

        return [self.custo,
        self.mode_resident_country, self.mode_sex, self.final_age,
        self.first_cust_start_date, self.mode_customer_type,
        self.mode_province,
        self.last_inactive, self.months_last_inactive, self.mean_income,
        self.mode_segmentation, self.final_segmentation, self.first_saving,
        self.sum_saving, self.first_guarantee, self.sum_guarantee,
        self.first_current, self.sum_current, self.first_derivada,
        self.sum_derivada, self.first_payroll, self.sum_payroll,
        self.first_junior, self.sum_junior, self.first_maspart,
        self.sum_maspart, self.first_part, self.sum_part, self.first_partplus,
        self.sum_partplus, self.first_stdep, self.sum_stdep, self.first_mtdep,
        self.sum_mtdep, self.first_ltdep, self.sum_ltdep, self.first_eacct,
        self.sum_eacct, self.first_fund, self.sum_fund, self.first_mortgage,
        self.sum_mortgage, self.first_pension, self.sum_pension,
        self.first_loan, self.sum_loan, self.first_tax, self.sum_tax,
        self.first_credit, self.sum_credit, self.first_security,
        self.sum_security, self.first_home, self.sum_home,
        self.first_nompayroll, self.sum_nompayroll, self.first_nompension,
        self.sum_nompension, self.first_debit, self.sum_debit,
        self.ind_ahor_fin_ult1, self.ind_aval_fin_ult1, self.ind_cco_fin_ult1,
        self.ind_cder_fin_ult1, self.ind_cno_fin_ult1, self.ind_ctju_fin_ult1,
        self.ind_ctma_fin_ult1, self.ind_ctop_fin_ult1, self.ind_ctpp_fin_ult1,
        self.ind_deco_fin_ult1, self.ind_deme_fin_ult1, self.ind_dela_fin_ult1,
        self.ind_ecue_fin_ult1, self.ind_fond_fin_ult1, self.ind_hip_fin_ult1,
        self.ind_plan_fin_ult1, self.ind_pres_fin_ult1, self.ind_reca_fin_ult1,
        self.ind_tjcr_fin_ult1, self.ind_valo_fin_ult1, self.ind_viv_fin_ult1,
        self.ind_nomina_ult1, self.ind_nom_pens_ult1, self.ind_recibo_ult1]

    def getTestRow(self):
        #self.mode_ind_employee = mode(self.ind_employee)
        self.mode_resident_country = mode(self.resident_country)
        self.mode_sex = mode(self.sex)
        self.mode_customer_type = mode(self.customer_type)
        #self.mode_empl_spouse = mode(self.empl_spouse)
        #self.mode_join_channel = mode(self.join_channel)
        self.mode_province = mode(self.province)
        self.last_inactive = last_inactive_period(self.months_inactive)
        self.months_last_inactive = months_last_inactive_period(self.months_inactive)
        self.mean_income = mean(self.income)
        self.mode_segmentation = mode(self.segmentation)

        return [self.custo,
        self.mode_resident_country, self.mode_sex, self.final_age,
        self.first_cust_start_date, self.mode_customer_type,
        self.mode_province,
        self.last_inactive, self.months_last_inactive, self.mean_income,
        self.mode_segmentation, self.final_segmentation, self.first_saving,
        self.sum_saving, self.first_guarantee, self.sum_guarantee,
        self.first_current, self.sum_current, self.first_derivada,
        self.sum_derivada, self.first_payroll, self.sum_payroll,
        self.first_junior, self.sum_junior, self.first_maspart,
        self.sum_maspart, self.first_part, self.sum_part, self.first_partplus,
        self.sum_partplus, self.first_stdep, self.sum_stdep, self.first_mtdep,
        self.sum_mtdep, self.first_ltdep, self.sum_ltdep, self.first_eacct,
        self.sum_eacct, self.first_fund, self.sum_fund, self.first_mortgage,
        self.sum_mortgage, self.first_pension, self.sum_pension,
        self.first_loan, self.sum_loan, self.first_tax, self.sum_tax,
        self.first_credit, self.sum_credit, self.first_security,
        self.sum_security, self.first_home, self.sum_home,
        self.first_nompayroll, self.sum_nompayroll, self.first_nompension,
        self.sum_nompension, self.first_debit, self.sum_debit]

class CustomerBuilder(Customer):
    # def init():
    #     self.ind_employee = []
    #     self.resident_country = []
    #     self.sex = []
    #     self.customer_type = []
    #     self.empl_spouse = []
    #     self.join_channel = []
    #     self.province = []
    #     self.months_inactive = []
    #     self.income = []
    #     self.segmentation = []
    #     super.__init__()

    def __init__(self, custo, first_cust_start_date):
        Customer.__init__(self)

        self.custo = custo
        self.first_cust_start_date = first_cust_start_date

        self.ind_employee = []
        self.resident_country = []
        self.sex = []
        self.customer_type = []
        self.empl_spouse = []
        self.join_channel = []
        self.province = []
        self.months_inactive = []
        self.income = []
        self.segmentation = []

    def update_response(self, row):
        row = cleanData(row)
        ind_ahor_fin_ult1 = int(row[25])
        ind_aval_fin_ult1 = int(row[26])
        ind_cco_fin_ult1 = int(row[27])
        ind_cder_fin_ult1 = int(row[28])
        ind_cno_fin_ult1 = int(row[29])
        ind_ctju_fin_ult1 = int(row[30])
        ind_ctma_fin_ult1 = int(row[31])
        ind_ctop_fin_ult1 = int(row[32])
        ind_ctpp_fin_ult1 = int(row[33])
        ind_deco_fin_ult1 = int(row[34])
        ind_deme_fin_ult1 = int(row[35])
        ind_dela_fin_ult1 = int(row[36])
        ind_ecue_fin_ult1 = int(row[37])
        ind_fond_fin_ult1 = int(row[38])
        ind_hip_fin_ult1 = int(row[39])
        ind_plan_fin_ult1 = int(row[40])
        ind_pres_fin_ult1 = int(row[41])
        ind_reca_fin_ult1 = int(row[42])
        ind_tjcr_fin_ult1 = int(row[43])
        ind_valo_fin_ult1 = int(row[44])
        ind_viv_fin_ult1 = int(row[45])
        ind_nomina_ult1 = int(row[46])
        ind_nom_pens_ult1 = int(row[47])
        ind_recibo_ult1 = int(row[48])

        #Response Variables
        self.ind_ahor_fin_ult1 = ind_ahor_fin_ult1
        self.ind_aval_fin_ult1 = ind_aval_fin_ult1
        self.ind_cco_fin_ult1 = ind_cco_fin_ult1
        self.ind_cder_fin_ult1 = ind_cder_fin_ult1
        self.ind_cno_fin_ult1 = ind_cno_fin_ult1
        self.ind_ctju_fin_ult1 = ind_ctju_fin_ult1
        self.ind_ctma_fin_ult1 = ind_ctma_fin_ult1
        self.ind_ctop_fin_ult1 = ind_ctop_fin_ult1
        self.ind_ctpp_fin_ult1 = ind_ctpp_fin_ult1
        self.ind_deco_fin_ult1 = ind_deco_fin_ult1
        self.ind_deme_fin_ult1 = ind_deme_fin_ult1
        self.ind_dela_fin_ult1 = ind_dela_fin_ult1
        self.ind_ecue_fin_ult1 = ind_ecue_fin_ult1
        self.ind_fond_fin_ult1 = ind_fond_fin_ult1
        self.ind_hip_fin_ult1 = ind_hip_fin_ult1
        self.ind_plan_fin_ult1 = ind_plan_fin_ult1
        self.ind_pres_fin_ult1 = ind_pres_fin_ult1
        self.ind_reca_fin_ult1 = ind_reca_fin_ult1
        self.ind_tjcr_fin_ult1 = ind_tjcr_fin_ult1
        self.ind_valo_fin_ult1 = ind_valo_fin_ult1
        self.ind_viv_fin_ult1 = ind_viv_fin_ult1
        self.ind_nomina_ult1 = ind_nomina_ult1
        self.ind_nom_pens_ult1 = ind_nom_pens_ult1
        self.ind_recibo_ult1 = ind_recibo_ult1

    def update(self, row):
        row = cleanData(row)

        curDat = date_to_month(row[1])
        ncodpers = int(row[2])
        #ind_empleado = row[3]
        pais_residencia = row[4]
        sexo = row[5]
        age = row[6]
        #fecha_alta = row[7]
        #ind_nuevo = row[8]
        #antiguedad = row[9]
        #indrel = row[10]
        #ult_fec_cli_1t = row[11]
        indrel_1mes = row[12]
        #tiprel_1mes = row[13]
        #indresi = row[14]
        #indext = row[15]
        #conyuemp = row[16]
        #canal_entrada = row[17]
        #indfall = row[18]
        #tipodom = row[19]
        cod_prov = row[20]
        #nomprov = row[21]
        ind_actividad_cliente = row[22]
        renta = float(row[23])
        segmento = row[24]
        ind_ahor_fin_ult1 = int(row[25])
        ind_aval_fin_ult1 = int(row[26])
        ind_cco_fin_ult1 = int(row[27])
        ind_cder_fin_ult1 = int(row[28])
        ind_cno_fin_ult1 = int(row[29])
        ind_ctju_fin_ult1 = int(row[30])
        ind_ctma_fin_ult1 = int(row[31])
        ind_ctop_fin_ult1 = int(row[32])
        ind_ctpp_fin_ult1 = int(row[33])
        ind_deco_fin_ult1 = int(row[34])
        ind_deme_fin_ult1 = int(row[35])
        ind_dela_fin_ult1 = int(row[36])
        ind_ecue_fin_ult1 = int(row[37])
        ind_fond_fin_ult1 = int(row[38])
        ind_hip_fin_ult1 = int(row[39])
        ind_plan_fin_ult1 = int(row[40])
        ind_pres_fin_ult1 = int(row[41])
        ind_reca_fin_ult1 = int(row[42])
        ind_tjcr_fin_ult1 = int(row[43])
        ind_valo_fin_ult1 = int(row[44])
        ind_viv_fin_ult1 = int(row[45])
        ind_nomina_ult1 = int(row[46])
        ind_nom_pens_ult1 = int(row[47])
        ind_recibo_ult1 = int(row[48])

        #self.ind_employee.append(ind_empleado)
        self.resident_country.append(pais_residencia)
        self.sex.append(sexo)
        self.customer_type.append(indrel_1mes)
        #self.empl_spouse.append(conyuemp)
        #self.join_channel.append(canal_entrada)
        self.province.append(cod_prov)
        self.months_inactive.append(ind_actividad_cliente)
        self.income.append(renta)
        self.segmentation.append(segmento)

        #Demographic
        ##self.mode_ind_employee = mode(self.ind_employee)
        #self.mode_resident_country = mode(self.resident_country)
        #self.mode_sex = mode(self.sex)
        self.final_age = age
        #self.mode_customer_type = mode(self.customer_type)
        ##self.mode_empl_spouse = mode(self.empl_spouse)
        ##self.mode_join_channel = mode(self.join_channel)
        #self.mode_province = mode(self.province)
        #self.last_inactive = last_inactive_period(self.months_inactive)
        #self.months_last_inactive = months_last_inactive_period(self.months_inactive)
        #self.mean_income = mean(self.income)
        #self.mode_segmentation = mode(self.segmentation)
        self.final_segmentation = segmento

        #Behavioral
        if (-1 == self.first_saving and 1 == ind_ahor_fin_ult1):
            self.first_saving = curDat - self.first_cust_start_date
        self.sum_saving += ind_ahor_fin_ult1
        if (-1 == self.first_guarantee and 1 == ind_aval_fin_ult1):
            self.first_guarantee = curDat - self.first_cust_start_date
        self.sum_guarantee += ind_aval_fin_ult1
        if (-1 == self.first_current and 1 == ind_cco_fin_ult1):
            self.first_current = curDat - self.first_cust_start_date
        self.sum_current += ind_cco_fin_ult1
        if (-1 == self.first_derivada and 1 == ind_cder_fin_ult1):
            self.first_derivada = curDat - self.first_cust_start_date
        self.sum_derivada += ind_cder_fin_ult1
        if (-1 == self.first_payroll and 1 == ind_cno_fin_ult1):
            self.first_payroll = curDat - self.first_cust_start_date
        self.sum_payroll += ind_cno_fin_ult1
        if (-1 == self.first_junior and 1 == ind_ctju_fin_ult1):
            self.first_junior = curDat - self.first_cust_start_date
        self.sum_junior += ind_ctju_fin_ult1
        if (-1 == self.first_maspart and 1 == ind_ctma_fin_ult1):
            self.first_maspart = curDat - self.first_cust_start_date
        self.sum_maspart += ind_ctma_fin_ult1
        if (-1 == self.first_part and 1 == ind_ctop_fin_ult1):
            self.first_part = curDat - self.first_cust_start_date
        self.sum_part += ind_ctop_fin_ult1
        if (-1 == self.first_partplus and 1 == ind_ctpp_fin_ult1):
            self.first_partplus = curDat - self.first_cust_start_date
        self.sum_partplus += ind_ctpp_fin_ult1
        if (-1 == self.first_stdep and 1 == ind_deco_fin_ult1):
            self.first_stdep = curDat - self.first_cust_start_date
        self.sum_stdep += ind_deco_fin_ult1
        if (-1 == self.first_mtdep and 1 == ind_deme_fin_ult1):
            self.first_mtdep = curDat - self.first_cust_start_date
        self.sum_mtdep += ind_deme_fin_ult1
        if (-1 == self.first_ltdep and 1 == ind_dela_fin_ult1):
            self.first_ltdep = curDat - self.first_cust_start_date
        self.sum_ltdep += ind_dela_fin_ult1
        if (-1 == self.first_eacct and 1 == ind_ecue_fin_ult1):
            self.first_eacct = curDat - self.first_cust_start_date
        self.sum_eacct += ind_ecue_fin_ult1
        if (-1 == self.first_fund and 1 == ind_fond_fin_ult1):
            self.first_fund = curDat - self.first_cust_start_date
        self.sum_fund += ind_fond_fin_ult1
        if (-1 == self.first_mortgage and 1 == ind_hip_fin_ult1):
            self.first_mortgage = curDat - self.first_cust_start_date
        self.sum_mortgage += ind_hip_fin_ult1
        if (-1 == self.first_pension and 1 == ind_plan_fin_ult1):
            self.first_pension = curDat - self.first_cust_start_date
        self.sum_pension += ind_plan_fin_ult1
        if (-1 == self.first_loan and 1 == ind_pres_fin_ult1):
            self.first_loan = curDat - self.first_cust_start_date
        self.sum_loan += ind_pres_fin_ult1
        if (-1 == self.first_tax and 1 == ind_reca_fin_ult1):
            self.first_tax = curDat - self.first_cust_start_date
        self.sum_tax += ind_reca_fin_ult1
        if (-1 == self.first_credit and 1 == ind_tjcr_fin_ult1):
            self.first_credit = curDat - self.first_cust_start_date
        self.sum_credit += ind_tjcr_fin_ult1
        if (-1 == self.first_security and 1 == ind_valo_fin_ult1):
            self.first_security = curDat - self.first_cust_start_date
        self.sum_security += ind_valo_fin_ult1
        if (-1 == self.first_home and 1 == ind_viv_fin_ult1):
            self.first_home = curDat - self.first_cust_start_date
        self.sum_home += ind_viv_fin_ult1
        if (-1 == self.first_nompayroll and 1 == ind_nomina_ult1):
            self.first_nompayroll = curDat - self.first_cust_start_date
        self.sum_nompayroll += ind_nomina_ult1
        if (-1 == self.first_nompension and 1 == ind_nom_pens_ult1):
            self.first_nompension = curDat - self.first_cust_start_date
        self.sum_nompension += ind_nom_pens_ult1
        if (-1 == self.first_debit and 1 == ind_recibo_ult1):
            self.first_debit = curDat - self.first_cust_start_date
        self.sum_debit += ind_recibo_ult1

def mean(arr):
    arrSum = 0
    for thing in arr:
        arrSum += thing
    if(len(arr) > 0):
        return arrSum / len(arr)
    else:
        return 0

def mode(arr):
    freq = {}
    for thing in arr:
        if thing in freq:
            freq[thing] += 1
        else:
            freq[thing] = 1
    arrMaxFreq = 0
    arrMax = "0"
    for thing in freq:
        if (freq[thing] > arrMaxFreq):
            arrMaxFreq = freq[thing]
            arrMax = thing
    return arrMax

def last_inactive_period(inactive):
    if 0 in inactive:
        rinact = inactive[::-1]
        return rinact.index(0) + 1
    return 0

def months_last_inactive_period(inactive):
    if 0 in inactive:
        rinact = inactive[::-1]
        beforeEndInactive = rinact[rinact.index(0):]
        if 1 in beforeEndInactive:
            return beforeEndInactive.index(1) + 1
        return len(beforeEndInactive)
    return 0

def cleanData(row):
    newRow = []
    for thing in row:
        if thing == "NA" or thing == "" or thing == '0.0':
            newRow.append("0")
        elif thing == '1.0':
            newRow.append('1')
        else:
            newRow.append(thing)
    return newRow

def date_to_month(date):
    fdate = time.strptime(date,'%Y-%m-%d')
    monthFromJan1970 = (fdate.tm_year - 1970) * 12 + fdate.tm_mon
    return monthFromJan1970

"""
COL HEADER
0	fecha_dato
1	ncodpers
2	ind_empleado
3	pais_residencia
4	sexo
5	age
6	fecha_alta
7	ind_nuevo
8	antiguedad
9	indrel
10	ult_fec_cli_1t
11	indrel_1mes
12	tiprel_1mes
13	indresi
14	indext
15	conyuemp
16	canal_entrada
17	indfall
18	tipodom
19	cod_prov
20	nomprov
21	ind_actividad_cliente
22	renta
23	segmento
24	ind_ahor_fin_ult1
25	ind_aval_fin_ult1
26	ind_cco_fin_ult1
27	ind_cder_fin_ult1
28	ind_cno_fin_ult1
29	ind_ctju_fin_ult1
30	ind_ctma_fin_ult1
31	ind_ctop_fin_ult1
32	ind_ctpp_fin_ult1
33	ind_deco_fin_ult1
34	ind_deme_fin_ult1
35	ind_dela_fin_ult1
36	ind_ecue_fin_ult1
37	ind_fond_fin_ult1
38	ind_hip_fin_ult1
39	ind_plan_fin_ult1
40	ind_pres_fin_ult1
41	ind_reca_fin_ult1
42	ind_tjcr_fin_ult1
43	ind_valo_fin_ult1
44	ind_viv_fin_ult1
45	ind_nomina_ult1
46	ind_nom_pens_ult1
47	ind_recibo_ult1
"""


firstLastRowNum = 1 #Row index currently processing, until see "2016-5-28"
customers = {}

with open(TRAIN_DATA_FILE, 'r') as csvf:
    reader = csv.reader(csvf)
    curDat = 0 #Date block currently processing
    firstDat = 0 #Date data begins
    for row in reader:
        if firstLastRowNum == 1: #Column header
            firstLastRowNum += 1
        else: #Not column header
            #ind_empleado = row[3]
            #indfall = row[18]
            #renta = row[23]
            if row[3] == "" or row[23] == "": #Skip blank rows
                continue
            #
            # row = fill_NA(row) #Set NA to 0

            ncodpers = int(row[2])

            if (ncodpers not in customers): #New customer
                startDate = date_to_month(row[7])
                customers[ncodpers] = CustomerBuilder(ncodpers, startDate)

            if date_to_month(row[1]) == date_to_month("2016-5-28"): #Last date in time series. Only change the response variables.
                customers[ncodpers].update_response(row)
            else: #Update features.
                customers[ncodpers].update(row)
                firstLastRowNum += 1

print("done train reading")

with open(TRAIN_OUTPUT_FILE, 'w') as csvo:
    writer = csv.writer(csvo)
    writer.writerow(['custo','mode_resident_country',
    'mode_sex','final_age','first_cust_start_date','mode_customer_type',
    'mode_province','last_inactive',
    'months_last_inactive','mean_income','mode_segmentation',
    'final_segmentation','first_saving','sum_saving','first_guarantee',
    'sum_guarantee','first_current','sum_current','first_derivada',
    'sum_derivada','first_payroll','sum_payroll','first_junior',
    'sum_junior','first_maspart','sum_maspart','first_part','sum_part',
    'first_partplus','sum_partplus','first_stdep','sum_stdep','first_mtdep',
    'sum_mtdep','first_ltdep','sum_ltdep','first_eacct','sum_eacct',
    'first_fund','sum_fund','first_mortgage','sum_mortgage','first_pension',
    'sum_pension','first_loan','sum_loan','first_tax','sum_tax',
    'first_credit','sum_credit','first_security','sum_security',
    'first_home','sum_home','first_nompayroll','sum_nompayroll',
    'first_nompension','sum_nompension','first_debit','sum_debit',
    'ind_ahor_fin_ult1','ind_aval_fin_ult1','ind_cco_fin_ult1',
    'ind_cder_fin_ult1','ind_cno_fin_ult1','ind_ctju_fin_ult1',
    'ind_ctma_fin_ult1','ind_ctop_fin_ult1','ind_ctpp_fin_ult1',
    'ind_deco_fin_ult1','ind_deme_fin_ult1','ind_dela_fin_ult1',
    'ind_ecue_fin_ult1','ind_fond_fin_ult1','ind_hip_fin_ult1',
    'ind_plan_fin_ult1','ind_pres_fin_ult1','ind_reca_fin_ult1',
    'ind_tjcr_fin_ult1','ind_valo_fin_ult1','ind_viv_fin_ult1',
    'ind_nomina_ult1','ind_nom_pens_ult1','ind_recibo_ult1'])
    for cust in customers:
        thingy = customers[cust].getTrainRow()
        if not thingy[-1] == -1: #Last row is a response var. If it wasn't
        #changed from -1, then customer was't represented in 2016-5-28
            writer.writerow( thingy )

print("done train writing")

with open(TRAIN_DATA_FILE, 'r') as csvf:
    reader = csv.reader(csvf)
    rowNum = 0
    curDat = 0 #Date block currently processing
    firstDat = 0 #Date data begins
    for row in reader:
        rowNum += 1
        if rowNum >= firstLastRowNum: #"2016-5-28"
            if row[3] == "" or row[23] == "": #Skip blank rows
                continue
            #
            # row = fill_NA(row) #Set NA to 0

            ncodpers = int(row[2])

            if (ncodpers not in customers): #New customer
                startDate = date_to_month(row[7])
                customers[ncodpers] = CustomerBuilder(ncodpers, startDate)

            customers[ncodpers].update(row)

testCustomers = [] #array of all the customers in the test set

with open(TEST_DATA_FILE, 'r') as csvf:
    reader = csv.reader(csvf)
    row1 = True
    for row in reader:
        if row1:
            row1 = False
            continue
        ncodpers = int(row[2])
            
        if (ncodpers not in customers): #New customer
            startDate = date_to_month(row[7])
            customers[ncodpers] = CustomerBuilder(ncodpers, startDate)
            customers[ncodpers].update(row) #Only take behavioral data if its a new customer

        testCustomers.append(ncodpers)

print("done test reading")

with open(TEST_OUTPUT_FILE, 'w') as csvo:
    writer = csv.writer(csvo)
    writer.writerow(['custo','mode_resident_country',
    'mode_sex','final_age','first_cust_start_date','mode_customer_type',
    'mode_province','last_inactive',
    'months_last_inactive','mean_income','mode_segmentation',
    'final_segmentation','first_saving','sum_saving','first_guarantee',
    'sum_guarantee','first_current','sum_current','first_derivada',
    'sum_derivada','first_payroll','sum_payroll','first_junior',
    'sum_junior','first_maspart','sum_maspart','first_part','sum_part',
    'first_partplus','sum_partplus','first_stdep','sum_stdep','first_mtdep',
    'sum_mtdep','first_ltdep','sum_ltdep','first_eacct','sum_eacct',
    'first_fund','sum_fund','first_mortgage','sum_mortgage','first_pension',
    'sum_pension','first_loan','sum_loan','first_tax','sum_tax',
    'first_credit','sum_credit','first_security','sum_security',
    'first_home','sum_home','first_nompayroll','sum_nompayroll',
    'first_nompension','sum_nompension','first_debit','sum_debit'])
    for cust in testCustomers:
        thing = customers[cust].getTestRow()
        writer.writerow( thing )

print("done test writing")
