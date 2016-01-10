[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> NUMKDHH: "Number of biological/adopted/related/legal children under age 18 in household"

```
%matplotlib inline

import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)
thinkplot.Pmf(pmf,label='numkdhh')
thinkplot.Show()
```
![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c3e1g1.png "Logo Title Text 1")

```
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
biasPmf = BiasPmf(pmf,label='pmf')
thinkplot.Pmf(biasPmf,label='biasPmf',color='red')
thinkplot.Pmf(pmf,label='numkdhh')
thinkplot.Show()
```

![alt text](https://github.com/davidcdupuis/dsp/blob/master/img/c3e1g2.png "Logo Title Text 1")

```
pmf.Mean()
```

>> 1.0242051550438309

```
biasPmf.Mean()
```

>> 2.4036791006642821

>> One explanation to the difference in means could be in the clarity of who are the children in the family but it is also due to the fact that in families without children we cannot ask them how many children they think there are... 
