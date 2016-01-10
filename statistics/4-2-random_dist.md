[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
%matplotlib inline

import thinkstats2
import thinkplot
import random
randomValues = [random.random() for x in range(1000)]
pmf = thinkstats2.Pmf(randomValues)
thinkplot.Pmf(pmf,label='pmf of random values')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c4e2g1.png "Logo Title Text 1")
```
cdf = thinkstats2.Cdf(randomValues)
thinkplot.Cdf(cdf,label='cdf of random values')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c4e2g2.png "Logo Title Text 1")
```
randomValues2 = [random.random() for x in range(100)]
cdf2 = thinkstats2.Cdf(randomValues2)
thinkplot.Cdf(cdf,label='cdf of 100 random values')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c4e2g3.png "Logo Title Text 1")
```
randomValues3 = [random.random() for x in range(10)]
cdf3 = thinkstats2.Cdf(randomValues3)
thinkplot.Cdf(cdf,label='cdf of 100 random values')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c4e2g4.png "Logo Title Text 1")
```
randomValues4 = [random.random() for x in range(10000)]
cdf3 = thinkstats2.Cdf(randomValues4)
thinkplot.Cdf(cdf,label='cdf of 10000 random values')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c4e2g5.png "Logo Title Text 1")

>> Clearly the distribution is uniform for random generated numbers
