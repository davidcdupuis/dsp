[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```
%matplotlib inline

import thinkstats2
import thinkplot
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Cohen's d for totalwgt_lb
wgtEffect = thinkstats2.CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)
 
#Cohen's d for prglngth
lngthEffect = thinkstats2.CohenEffectSize(firsts.prglngth,others.prglngth)
```

| Variable  |  Total weight in pounds (totalwgt_lb)  |  Pregnancy length (prglngth)  |
|-----------|:--------------------------------------:|:-----------------------------:|
| Cohen's d | -0.0886                                |0.0288                         |

|  Effect size | r      |
|:------------:|:------:|
|small         | 0.10   |
|medium        | 0.30   |
|large         | 0.50   |

>> Thus we observe that since it is negative for total weight it indicates that the mean of `firsts.totalwgt_lb` is smaller than the mean of `others.totalwgt_lb`

>> As for the pregnancy length, Cohen's d is very small which indicates that there isn't a lot of difference 
