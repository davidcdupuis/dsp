[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
mu = 178
sigma = 7.7

dist = scipy.stats.norm(loc=mu, scale=sigma)
(dist.cdf(185.5) - dist.cdf(177.8)) * 100
```
>>34.533915076724

>> Approximately 35% of the population of men are betwen 5'10" and 6'1" and could apply to the Blue Man Group
