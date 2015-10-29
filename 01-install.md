# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

---

Did you install Python 2 or 3? Why? How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> I installed Anaconda 3.4 but seem to have Python 2.7 working on my computer. But none of the above commands seem to work correctly. I will have to sort things out. Installing the newest version of Python is good for using new tools. However having the older version is also good for running older scripts or tools. To check which version of Python is installed, I can write in the terminal: "python --version". Also executing the python application displays the application information. 
>> Using Anaconda requires to launch it, might have seemed obvious. But it works.

---


### Homebrew

If you use a Mac, install [Homebrew](http://brew.sh/) if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.
