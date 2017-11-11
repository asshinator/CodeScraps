library(forecast)

# read Nasdaq data from file
NDAQ <- read.csv("C:/Users/calyha/Dropbox/Stock Prices/individual_stocks_5yr/NDAQ_data.csv")

# save close prices as time series
NDAQ_ts <- ts(NDAQ$Close)

# plot the ACF
Acf(NDAQ_ts)
Pacf(NDAQ_ts)
# appears that time series is non-stationary

# number of differences required to reach stationarity
d <- ndiffs(NDAQ_ts)
# d = 1

# plot the ACF / PACF of differenced time series
Acf(diff(NDAQ_ts, differences = d))
Pacf(diff(NDAQ_ts, differences = d))
# non-stationarity appears to be fixed

# can't really check seasonality for daily data
# unless we consolidate it per month (?)
# so skip that option

# split data into training and testing sets
training <- window(NDAQ_ts, end = 629)
testing <- window(NDAQ_ts, start = 630)

###
# ARIMA model
###
arima_model <- auto.arima(training)
predictions <- forecast(arima_model, 629) # forecast for test period
accuracy(predictions, testing)
plot(predictions)

###
# Exponential model
###

# Note: no Holt-Winters b/c no seasonality

expon_model <- ets(training)
predictions <- forecast(expon_model, 629)
accuracy(predictions, testing)
plot(predictions)
