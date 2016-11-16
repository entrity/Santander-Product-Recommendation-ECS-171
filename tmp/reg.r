
load('Xhead.rda')
load('Yhead.rda')

Y = Y[, 4]
X = X[,-c(1,2)]
X[is.na(X)] <- 0

lambda = 0.1

set.seed(39)
MSE_THRESHOLD = 0.000001


  X = X[,-c(1,2)]
  m = length(Y)
  n = length(X)

  w = rep(0, n)
  epocherrors = rep(0, m)
  prevmserr = Inf

  for (epoch in 1:1000) {
    order = sample.int(m, m)
    for (row in order) {
      
      x = as.numeric(X[row,])
      y = as.numeric(Y[row])
      
      errors = y - 1/(1 + exp(w %*% x)) + lambda * w %*% w
      gra = errors * x
      a = 0.1
      err = sum(errors^2)
  
      if (err < MSE_THRESHOLD) {
        epocherrors[row] <- err
        next
      }
      
      # Search for a that yields error less than 'err'
      for (i in 1:100) {
        w1 = w + a * gra
        errors1 = y - 1/(1 + exp(w1 %*% x)) + lambda * w1 %*% w1
        err1 = sum(errors1^2)
        if (err1 <= err) {
          w = w1
          break
        }
        a = a / 2
      }
      if (100 == i) warning(sprintf('i == 100; didn\'t get good error. epoch %d\t%f vs %f', epoch, err1, err))
      # Save error for calculating mse across samples
      epocherrors[row] <- err1
      if (any(is.na(epocherrors))) {
        stop('na err')
      }
    } # end of epoch
    # Calc current error
    mserr = sum(errors^2)
    print(sprintf('epoch %d    error %f', epoch, mserr))
    # Check satisfaction conditions
    if (mserr < MSE_THRESHOLD || prevmserr == mserr)
      return(w)
    prevmserr = mserr
  }
  warning(sprintf('performed max epochs (%d) on regression', epoch))
