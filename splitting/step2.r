# This script does not take more than a few seconds to run.
# Feel free to change TEST_RATIO if you want a different number
# of test samples.
#
# This script takes X% of each bin (1-16) to be in the testSet.
# The bins are numbered 1-16. The number indicates how many ordered
# pairs of months exist for the customer in the bin.
#
# For example, in bin 1, all of the customers have only 2 adjacent 
# months of data (i.e. one ordered pair). That means that exactly
# one month of data can be used to predict exactly one (following)
# month of data.
#
# If a customer has X ordered pairs, that does not mean that the customer
# has X+1 months in a row. For example a customer in bin 2 may have data
# for January, February, June, July; that's 4 months, but there are only
# 2 opportunities to learn or make predictions.

load('Step1.RData')

bins = vector(mode='list')

testSet = vector(mode='numeric')
trainSet = vector(mode='numeric')

TEST_RATIO = 0.3

for (i in 1:16) {
	bins[[i]] = df[df$counts == i,]
	# random sample
	n = nrow(bins[[i]])
	test_n = round( n * TEST_RATIO )
	test_indices = sample.int(n, test_n)
	# update testSet, trainSet	
	testSet = append( bins[[i]][test_indices,]$cids, testSet )
	trainSet = append( bins[[i]][-(test_indices),]$cids, trainSet )
}

save.image('Step2.RData')
print('testSet is a vector of customer ids')
print('trainSet is a vector of customer ids')

