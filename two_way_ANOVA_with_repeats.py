#two-way ANOVA with repeats along the 3rd axis

from pylab import *
from scipy.stats import f as F

#9.13
x = array([[[6,4,5,5,4],[5,7,4,6,8]], 
           [[10,8,7,7,9],[7,9,12,8,8]], 
           [[7,5,6,5,9],[9,7,5,4,6]],
           [[8,4,6,5,5],[5,7,9,7,10]]])

a, b, c = x.shape

# total variation
v = ((x - x.mean())**2).sum()

# variation between rows
vr = b * c * ((x.mean(2).mean(1) - x.mean())**2).sum()

# variation between columns
vc = a * c * ((x.mean(2).mean(0) - x.mean())**2).sum()

# "interaction" 
vi = c * ((x.mean(2) - x.mean(2).mean(0, keepdims=1) - x.mean(2).mean(1, keepdims=1) + x.mean())**2).sum() 

# residual (errors)
ve = v - vr - vc - vi

# mean squares (variation divided by degree of freedom)
ms_r = vr / (a - 1)
ms_c = vc / (b - 1)
ms_i = vi / ((a - 1) * (b - 1))
ms_e = ve / (a * b * (c - 1))
print([ms_r, ms_c, ms_i, ms_e])

#degree of freedom
df = [a - 1, b - 1, (a - 1) * (b - 1), (a * b * (c - 1))]
print(df)

# F statistics
F_statistic = [ms_r/ms_e, ms_c/ms_e, ms_i/ms_e]
print(F_statistic)

# p-values
print(1 - F([a-1, b-1, (a-1)*(b-1)], a*b*(c-1)).cdf(F_statistic))