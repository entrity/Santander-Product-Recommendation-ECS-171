THRESHOLD = 0.000001


mse <- function(x, y, w, a, g, lambda) {
	# Calc new weights
	w = w - a * g
	# Calc new error
	err = (y - (x %*% w))^2 + lambda * w %*% w
	# Return
	return(err[[1]])
}

find_right_bound <- function(x, y, w, errL, g, lambda) {
	a = 1
	count = 0
	repeat {
		count = count + 1
		print(sprintf('count %d\ta %f\n', count, a))
		errR = mse(x, y, w, a, g, lambda)
		print(errR)
		print(errL)
		if (errR > errL) {
			return(list(a, errR))
		}
		if (Inf == a) {
			warning('Reached infinite learning rate in looking for right bound for steepest descent')
			break
		}
		a = a * 2
	}
}


# Use SGD + L2-norm regularization + steepest descent
# Assumes use of X.rda and Y.rda
gradient_descent <- function (X, Y, lambda) {
	X = X[,-c(1,2)] # omit D.ncodpers and fecha_dato
	Y = Y[,-c(1,2)] # omit D.ncodpers and fecha_dato

	w = rep(0, 1+length(X))
	m = length(Y)

	for (i in 1:length(Y)) {
		print(i)
		# Pick random sample
		# row = sample.int(nrow(X), 1)
		row = i
		x = c(1, as.numeric(X[row,]))
		y = as.numeric(Y[row])
		# kludge - REPLACE THIS
		x[is.na(x)] <- 0
		# Calc current error
		aL = 0
		errL = ((y - (x %*% w))^2)[[1]]
		if (0 == errL) next;
		print('nonzero error')
		# Calc gradient
		g = x * errL + lambda * w
		# Make binary leaps to find right bound for minimum error
		rightBound = find_right_bound(x, y, w, errL, g, lambda)
		aR = rightBound[[1]]
		errR = rightBound[[2]]
		# Binary search for steepest descent
		for (j in 1:10000) {
			aM = mean(c(aL, aR))
			errM = mse(x, y, w, aM, g, lambda)[[1]]
			print(sprintf('j %d\n',j))
			if (errM < THRESHOLD)
			if (errL < errR) {
				errR = errM
				aR = aM
			} else {
				errL = errM
				aL = aM
			}
			if (abs(aL - aR) < 0.0001 && errL < 0.00001) {
				w = w - a * g
				break
			}
		}
		if (10000 == j)
			warning(sprintf('Reached end of iterations for a steepest descent (after %d samples). Error is %f %f %f', i, errL, errM, errR))
	}

























	return(w)
}
