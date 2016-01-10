[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```
%matplotlib inline

import nsfg
import math
import thinkstats2
import thinkplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1] # select only live births
live = live.dropna(subset = ['agepreg', 'totalwgt_lb']) # drop na values
wgt = live.totalwgt_lb 
age = live.agepreg

plt.scatter(age, wgt, alpha = 0.2)
plt.xlabel('age of mother')
plt.ylabel('birth weight in lbs')
plt.title('Age of mother vs. Birth Weight in lbs')
plt.show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c7e1g1.png "Logo Title Text 1")
```
bins = np.arange(10, 50, 2) # bin age data between 10 yrs and 50 yrs, with interval of 2 yrs
indices = np.digitize(age, bins) # index age data to age bins
groups = live.groupby(indices) # group by age indices

ages = [group.agepreg.mean() for i, group in groups][1:-1] # calculate mean age in each age index
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

for percentage in [25, 50, 75]:
    weights = [cdf.Percentile(percentage) for cdf in cdfs]
    label = '%dth Percentile' % percentage
    plt.plot(ages, weights, label=label)
    
plt.xlabel('Mother\'s Age')
plt.ylabel('Birth Weight (lbs)')
plt.title('Mother\'s Age vs. Percentiles of Birth Weight in Lbs')
plt.legend(loc=3)
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c7e1g2.png "Logo Title Text 1")
```
p_corr = thinkstats2.Corr(age, wgt)
"Pearson's correlation : " + str(p_corr)
```
>> Pearson's correlation : 0.0688339703541
```
s_corr = thinkstats2.SpearmanCorr(age, wgt)
"Spearman's correlation : " + str(s_corr)
```
>> Spearman's correlation : 0.0946100410966

>> This shows that there is a very slight positive correlation between mother's age and birth weight. 
