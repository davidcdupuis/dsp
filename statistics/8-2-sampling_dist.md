[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

```
%matplotlib inline

import thinkstats2
import thinkplot
import matplotlib.pyplot
import math
import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError

def SimulateExponentialDistribution(n = 10, lmbda = 2, m = 1000, num = 0, prnt = True, plt = True):
    estimates = []
    for i in range(m):
        xs = np.random.exponential(1.0/lmbda, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)
    
    stderr = RMSE(estimates, lmbda)
    
        
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    
    if(prnt):
        print('standard error', stderr)
        print('confidence interval', ci)
    
    thinkplot.Plot([ci[0], ci[0]], [0, 1], color='0.8', linewidth=3)
    thinkplot.Plot([ci[1], ci[1]], [0, 1], color='0.8', linewidth=3)
    
     # plot the CDF
    if(plt):
        thinkplot.Cdf(cdf)
        rootValue = 'data/estimation'+ str(num)
        thinkplot.Save(root=rootValue,
                       xlabel='estimate',
                       ylabel='CDF',
                       title='Sampling distribution with n: ' + str(n))

    return stderr
    
    pos = 1
for i in [10, 100, 500, 1000]:
    SimulateExponentialDistribution(i,2,1000,pos)
    pos += 1
```

>>('standard error', 0.8677685686750071)

>>('confidence interval', (1.2723321422494542, 3.8212293470235741))

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c8e2g1.png "Logo Title Text 1")

>>('standard error', 0.19864352421169715)

>>('confidence interval', (1.7214016917260477, 2.3711198477637674))

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c8e2g2.png "Logo Title Text 1")

>> ('standard error', 0.08907069370255942)

>> ('confidence interval', (1.8627164907043039, 2.154570174967271))

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c8e2g3.png "Logo Title Text 1")

>> ('standard error', 0.0647839339641324)

>>('confidence interval', (1.9017730900590279, 2.1109749633093))

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c8e2g4.png "Logo Title Text 1")

>> The `n` vs standard error chart gives us:

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c8e2g5.png "Logo Title Text 1")

>> We thus notice that when `n` increases the `standard error` decreases and the confidence interval gets smaller. The last chart has its slope strongly decrease when `n` has its values between: 10 and 150
