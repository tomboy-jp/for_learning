import numpy as np
import abtest_hist as abtest

A_mu, A_sigma = 50, 5
B_mu, B_sigma = 60, 8

np.random.seed()

A_data = A_mu + A_sigma * np.random.randn(20000)
B_data = B_mu + B_sigma * np.random.randn(20000)

a = np.random.randn(10)
a


abtest.make_AB_hist(A_data, B_data)
