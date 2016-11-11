COLS_0 = c(
	'fecha_dato',
	'ncodpers',
	'ind_empleado',
	'pais_residencia',
	'sexo',
	'age',
	'fecha_alta',
	'ind_nuevo',
	'antiguedad',
	'indrel',
	'ult_fec_cli_1t',
	'indrel_1mes',
	'tiprel_1mes',
	'indresi',
	'indext',
	'conyuemp',
	'canal_entrada',
	'indfall',
	'tipodom',
	'cod_prov',
	'nomprov',
	'ind_actividad_cliente',
	'renta',
	'segmento',
	'ind_ahor_fin_ult1',
	'ind_aval_fin_ult1',
	'ind_cco_fin_ult1',
	'ind_cder_fin_ult1',
	'ind_cno_fin_ult1',
	'ind_ctju_fin_ult1',
	'ind_ctma_fin_ult1',
	'ind_ctop_fin_ult1',
	'ind_ctpp_fin_ult1',
	'ind_deco_fin_ult1',
	'ind_deme_fin_ult1',
	'ind_dela_fin_ult1',
	'ind_ecue_fin_ult1',
	'ind_fond_fin_ult1',
	'ind_hip_fin_ult1',
	'ind_plan_fin_ult1',
	'ind_pres_fin_ult1',
	'ind_reca_fin_ult1',
	'ind_tjcr_fin_ult1',
	'ind_valo_fin_ult1',
	'ind_viv_fin_ult1',
	'ind_nomina_ult1',
	'ind_nom_pens_ult1',
	'ind_recibo_ult1'
)

# NUMBER OF DIFFERENT VALUES IN EACH FEATURE COLUMN:
# ===================================================
# 17     fecha_dato
# 949614 ncodpers
# 5      ind_empleado
# 118    pais_residencia
# 3      sexo
# 120    age
# 6756   fecha_alta
# 2      ind_nuevo
# 258    antiguedad
# 2      indrel
# 224    ult_fec_cli_1t
# 10     indrel_1mes
# 6      tiprel_1mes
# 2      indresi
# 2      indext
# 3      conyuemp
# 163    canal_entrada
# 2      indfall
# 2      tipodom
# 53     cod_prov
# 53     nomprov
# 2      ind_actividad_cliente
# 520995 renta
# 4      segmento
# 2      ind_ahor_fin_ult1
# 2      ind_aval_fin_ult1
# 2      ind_cco_fin_ult1
# 2      ind_cder_fin_ult1
# 2      ind_cno_fin_ult1
# 2      ind_ctju_fin_ult1
# 2      ind_ctma_fin_ult1
# 2      ind_ctop_fin_ult1
# 2      ind_ctpp_fin_ult1
# 2      ind_deco_fin_ult1
# 2      ind_deme_fin_ult1
# 2      ind_dela_fin_ult1
# 2      ind_ecue_fin_ult1
# 2      ind_fond_fin_ult1
# 2      ind_hip_fin_ult1
# 2      ind_plan_fin_ult1
# 2      ind_pres_fin_ult1
# 2      ind_reca_fin_ult1
# 2      ind_tjcr_fin_ult1
# 2      ind_valo_fin_ult1
# 2      ind_viv_fin_ult1
# 3      ind_nomina_ult1
# 3      ind_nom_pens_ult1
# 2      ind_recibo_ult1


STAT_COLS_0 = COLS_0[1:24]
PROD_COLS_0 = COLS_0[-(1:24)]

# Categorical columns
# Cols that we wish to split into binary cols
# Excludes throw-aways like 'tipodom'
CATEGORICAL_COLS_0 = c(
	# 'ncodpers', # 969614
	'ind_empleado', # 5
	'pais_residencia', # 119
	'sexo', # 3
	'ind_nuevo', # 2
	'indrel', # 2
	'indrel_1mes', # 10
	'tiprel_1mes', # 6
	'indresi', # 2
	'indext', # 2
	'conyuemp', # 3
	'canal_entrada', # 163
	'indfall', # 2
	# 'tipodom', # 2
	'cod_prov', # 53
	# 'nomprov', # 53
	'ind_actividad_cliente', # 2
	'segmento' # 4
)

# Real-valued or integer-valued columns (ordinal)
# Non-categorical, non-date columns
REAL_COLS_0 = c('age', 'antiguedad', 'renta')

DATE_COLS_0 = c('fecha_dato', 'fecha_alta')

OMIT_COLS_O = setdiff(setdiff(setdiff(STAT_COLS_0, CATEGORICAL_COLS_0), REAL_COLS_0), DATE_COLS_0)
