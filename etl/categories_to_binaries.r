# Turn dates into POSIX dates.
# Turn categorical features into multiple binary features.
# Exclude features in OMIT_COLS_O.
#
# For this script, you should:
#
# 	load('D_minus_rows.rda')
# 	source('../constants.r')

# Start with customer identifier col
ncodpers = D$ncodpers
x = data.frame(ncodpers)

# Add date cols
for (feature in DATE_COLS_0) {
	x[[feature]] = as.POSIXct(D[[feature]])
}
# Add keeper real stat cols
for (feature in REAL_COLS_0) {
	x[[feature]] = D[[feature]]
}
# Add keeper cat stat cols
for (feature in CATEGORICAL_COLS_0) {
	for (value in unique(D[[feature]])) {
		new_col_name = sprintf('%s_%s', feature, value)
		values = as.numeric(D[[feature]] == value) # make column of {0,1}
		x[[new_col_name]] = values
	}
}
# Add all prod cols
for (feature in PROD_COLS_0) {
	x[[feature]] = D[[feature]]
}

D = x
save(D, file='D_no_cats.rda')

# 1002.673 sec elapsed (on hpc1)
