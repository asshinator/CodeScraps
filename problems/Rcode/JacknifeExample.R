# Bootstrap 95% CI for median of data
library(boot)

# generate random data
num_observations = 1000
my_data <- rnorm(num_observations, mean = 5, sd = 3)

# function to obtain median of data

med <- function(data, indices){
  rep_data <- data[indices] # bootstrap sample
  rep_median <- median(rep_data) # sample median
  return(rep_median)
}

# Generates jacknife data using formulas.
jacknife_output = c()
all_indices <- seq(1, num_observations)

for (j in 1:num_observations){
  choose_indices <- all_indices
  choose_indices <- choose_indices[-j]
  
  # saves jth jacknife replication of theta_hat
  jacknife_output[j] <- med(my_data, choose_indices)
}

theta_hat <- med(my_data, all_indices)

# eta[j] = jth pseudovalue
eta <- num_observations * theta_hat - (num_observations - 1) * jacknife_output

theta_hat_dot <- mean(jacknife_output)

# jacknife estimate of theta
theta_jk <- num_observations * theta_hat - (num_observations - 1) * theta_hat_dot

# jacknife estimate of bias
bias_jk <- (num_observations - 1) * (theta_hat_dot - theta_hat)

# jacknife estimate of variance
var_jk <- sum((jacknife_output- theta_hat_dot) ^ 2) * ((num_observations - 1) / num_observations)