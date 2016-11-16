set.seed(393) # err repeater
set.seed(16)

load('Xhead.rda')
load('Yhead.rda')

X = X[,-c(1,2)]
# for (col in 1:length(X))
#   X[,col] <- as.numeric(X[,col])
X[is.na(X)] <- 0
Y = Y[,-c(1,2)]
for (col in 1:length(Y))
  Y[,col] <- as.numeric(X[,col])
Y = Y[, 5]

samplect = length(Y)
testRows = sample.int(samplect, round(samplect * .2))

lambda = 0.1


train <- function (X, Y, lambda) {
  MSE_THRESHOLD = 0.000001
  Y = as.numeric(Y)
  m = length(Y) # numer of samples
  n = 1 + length(X) # number of features, including bias

  w = rep(0, n)
  epocherrors = rep(0, m)
  prevmserrs = rep(0, 4)

  for (epoch in 1:1000) {
    order = sample.int(m, m)
    for (row in order) {
      x = c(1, as.numeric(X[row,]))
      y = Y[row]

      err0 = y - 1/(1 + exp(w %*% x)) + lambda * w %*% w
      gra = err0 * x
      a = 0.1
      sqerr0 = err0^2

      if (sqerr0 < MSE_THRESHOLD) {
        epocherrors[row] <- sqerr0
        next
      }
      
      # Search for a that yields error less than 'err'
      for (i in 1:100) {
        w1 = w + a * gra
        err1 = y - 1/(1 + exp(w1 %*% x)) + lambda * w1 %*% w1
        sqerr1 = err1^2
        if (sqerr1 <= sqerr0) {
          w = w1
          break
        }
        a = a / 2
      }
      if (100 == i) warning(sprintf('i == 100; didn\'t get good error. epoch %d\t%f vs %f', epoch, err1, err))
      # Save error for calculating mse across samples
      epocherrors[row] <- sqerr1
      if (any(is.na(epocherrors))) {
        stop('na err')
      }
    } # end of epoch
    # Calc current error
    mserr = epocherrors[row] / m
    print(sprintf('epoch %3d    error %f', epoch, mserr))
    # Check satisfaction conditions
    if (mserr < MSE_THRESHOLD)
      return(w)
    if (epoch > length(prevmserrs) && all(prevmserrs == mserr))
      return(w)
    prevmserrs[1 + epoch %% length(prevmserrs)] = mserr
  }
  warning(sprintf('performed max epochs (%d) on regression', epoch))
  return (w)
}

test <- function (X, Y, w) {
  X     = cbind(rep(1, nrow(X)), X)
  h     = 1/(1 + exp( X %*% w ))
  errs  = h - Y
  mserr = mean(errs^2)
  print(mserr)
}

w = train(X[-testRows,], Y[-testRows], lambda)
Xt = data.matrix(X[testRows,])
Yt = Y[testRows]
test(Xt, Yt, w)
