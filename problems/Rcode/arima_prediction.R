library(forecast)

# read stock data from file
STOCKS <- read.csv("C:/Users/calyha/Dropbox/Stock Prices/all_stocks_5yr.csv")

# list of all stocks for iteration
stock_names <- unique(STOCKS$Name)

# save current stock price at close
# used for comparison to predictors
# using all but most recent 5 days
# i.e., true price at t = 5
future_price <- c()

# save stock price 5 days ago at close
# i.e., true price at t = 0
current_price <- c()

# save predicted stock price in 5 trading days
# i.e., predicted price for t = 5 using data
# through t = 0
predicted_price <- c()

# save predicted lo-80 / hi-80 / lo-95 / hi-95
# stock price in 5 trading days (one week)
lo_80_price <- c()
hi_80_price <- c()
lo_95_price <- c()
hi_95_price <- c()


for(which_stock in stock_names){
  # slice of data frame referring to this stock
  stock_data <- STOCKS[STOCKS$Name == which_stock,]
  
  # save close data as time series
  stock_ts <- ts(stock_data$Close)

  # save most recent close price (for comparison to prediction)
  future_price <- append(future_price, stock_ts[length(stock_ts)])
  
  # delete 5 trading days of information
  save_observations <- length(stock_ts) - 5
  stock_ts <- stock_ts[1:save_observations]
  
  # save most recent close price
  current_price <- append(current_price, stock_ts[length(stock_ts)])
  
  # fit ARIMA model to time series data
  stock_model <- auto.arima(stock_ts)
  
  # use ARIMA model to predict 5 trading days (1 week) into the future
  stock_forecast <- forecast(stock_model, 5)
  
  # predicted values
  stock_pred <- stock_forecast$mean[5]
  stock_lo_80 <- as.numeric(stock_forecast$lower[5,1])
  stock_lo_95 <- as.numeric(stock_forecast$lower[5,2])
  stock_hi_80 <- as.numeric(stock_forecast$upper[5,1])
  stock_hi_95 <- as.numeric(stock_forecast$upper[5,2])
  
  # save predicted values to vectors
  predicted_price <- append(predicted_price, stock_pred)
  lo_80_price <- append(lo_80_price, stock_lo_80)
  hi_80_price <- append(hi_80_price, stock_hi_80)
  lo_95_price <- append(lo_95_price, stock_lo_95)
  hi_95_price <- append(hi_95_price, stock_hi_95)
}

prediction_data <- data.frame(stock_names, current_price, lo_95_price, lo_80_price, predicted_price, hi_80_price, hi_95_price, future_price)
prediction_data$lo_95_change <- 100 * (prediction_data$lo_95_price - prediction_data$current_price) / prediction_data$current_price
prediction_data$lo_80_change <- 100 * (prediction_data$lo_80_price - prediction_data$current_price) / prediction_data$current_price
prediction_data$predicted_change <- 100 * (prediction_data$predicted_price - prediction_data$current_price) / prediction_data$current_price
prediction_data$hi_80_change <- 100 * (prediction_data$hi_80_price - prediction_data$current_price) / prediction_data$current_price
prediction_data$hi_95_change <- 100 * (prediction_data$hi_95_price - prediction_data$current_price) / prediction_data$current_price
prediction_data$true_change <- 100 * (prediction_data$future_price - prediction_data$current_price) / prediction_data$current_price

prediction_data$absolute_error <- abs(prediction_data$predicted_change - prediction_data$true_change)
prediction_data$abs_perc_error <- abs(prediction_data$predicted_change - prediction_data$true_change) / prediction_data$true_change

mean_absolute_error <- mean(prediction_data$absolute_error)
mape <- mean(prediction_data$abs_perc_error)

prediction_data$above_95 <- sign(prediction_data$future_price - prediction_data$hi_95_price)
prediction_data$below_95 <- sign(prediction_data$lo_95_price - prediction_data$future_price)
prediction_data$outside_95 <- max(prediction_data$above_95, prediction_data$below_95)



