# Bootstrap 95% CI for median of data
library(boot)

# generate random data
num_observations = 1000
my_data <- rnorm(num_observations, mean = 5, sd = 3)
bootstrap_replications <- 100

# function to obtain median of data

med <- function(data, indices){
  rep_data <- data[indices] # bootstrap sample
  rep_median <- median(rep_data) # sample median
  return(rep_median)
}

# Generates bootstrap data using library.
boot_med <- boot(my_data, med, R = bootstrap_replications)
boot_med

# Generates bootstrap data using formulas.
bootstrap_output = c()
all_indices <- seq(1, num_observations)

for (b in 1:bootstrap_replications){
  choose_indices <- sample(all_indices, num_observations, replace = TRUE)
  bootstrap_output[b] <- med(my_data, choose_indices)
}

theta_hat <- med(my_data, all_indices)
theta_hat_dot <- mean(bootstrap_output)

bias_bs <- theta_hat_dot - theta_hat
var_bs <- sum((bootstrap_output- theta_hat_dot) ^ 2) / (bootstrap_replications - 1)
