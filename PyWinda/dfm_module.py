import pwploter #only for documentation
# from PyWinda import pwploter # only for pytest
import numpy as np
import math
import matplotlib.pyplot as plt




def number_of_simsulaions(standard_error_of_mean,confidence_level,standard_normal_statistics,standard_deviaton_of_the_output):
    """
    """



def normal_dist(mean,sd,a=0,b=0,num=100,plot=False):
    """
        This function generates the normal (Gaussian) distribution, for a given mean value and standard distribution in an interval of a to b or a default of -5*standard deviation to 5*standard defiations.

        :param mean: [*req*] the mean of the distribution
        :param sd: [*req*]  the standard deviation of the distribution
        :param a: [*optional*] the start of the interval of the possible values
        :param b: [*optional*] the end of the interval of the possible values
        :param num: [*optional*] resolution of the interval.
        :return x,y, figure: x is the 1D-array of considered interval, y is the 1D-array of corresponding probability values, and if the plot option is set to True a figure will also be outputed.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> y,x,fig=normal_dist(mean=20,sd=2,plot=True)
                    >>> print(y) #doctest:+ELLIPSIS
                    [7.433597573671488e-07, 1.2255305214711653e-06, 1.999945186208313e-06, ...]
                    >>> print(x)
                    [10.         10.2020202  10.4040404  10.60606061 10.80808081 11.01010101
                     11.21212121 11.41414141 11.61616162 11.81818182 12.02020202 12.22222222
                     12.42424242 12.62626263 12.82828283 13.03030303 13.23232323 13.43434343
                     13.63636364 13.83838384 14.04040404 14.24242424 14.44444444 14.64646465
                     14.84848485 15.05050505 15.25252525 15.45454545 15.65656566 15.85858586
                     16.06060606 16.26262626 16.46464646 16.66666667 16.86868687 17.07070707
                     17.27272727 17.47474747 17.67676768 17.87878788 18.08080808 18.28282828
                     18.48484848 18.68686869 18.88888889 19.09090909 19.29292929 19.49494949
                     19.6969697  19.8989899  20.1010101  20.3030303  20.50505051 20.70707071
                     20.90909091 21.11111111 21.31313131 21.51515152 21.71717172 21.91919192
                     22.12121212 22.32323232 22.52525253 22.72727273 22.92929293 23.13131313
                     23.33333333 23.53535354 23.73737374 23.93939394 24.14141414 24.34343434
                     24.54545455 24.74747475 24.94949495 25.15151515 25.35353535 25.55555556
                     25.75757576 25.95959596 26.16161616 26.36363636 26.56565657 26.76767677
                     26.96969697 27.17171717 27.37373737 27.57575758 27.77777778 27.97979798
                     28.18181818 28.38383838 28.58585859 28.78787879 28.98989899 29.19191919
                     29.39393939 29.5959596  29.7979798  30.        ]
                     >>> print(fig)
                     Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    if a==0: a=mean-5*sd
    if b==0: b=mean+5*sd
    x=np.linspace(a,b,num) #creates the interval with the default number of seperation, here 100.
    y=[] #the normal distribution values
    for i in x:
        y.append((1/(sd*np.sqrt(2*np.pi)))*np.exp(-0.5*((i-mean)/sd)**2))
    if plot ==True:
        figure,ax=pwploter.plot(x,y,title="Normal Distribution",xlabel='Values [-]',ylabel='Probability [-]',text={'mean':mean,'Standard deviation':sd})
        return y, x, figure # returns y and x and the final figure if plot
    elif plot==False:
        return y,x  #returns y and x if not plot is done




def cdf_normal(mean, sd, x,a=0,b=0,plot=False):
    """
        This function generates the cumulative distribution function of the normal distributin function with the given parameters.

        :param mean: [*req*] the mean of the normal distribution
        :param sd: [*req*]  the standard deviation of the normal distribution
        :param x: [*req*]  any value within +/-5 times standard deviation.
        :param a: [*optional*] the start of the interval of the possible values
        :param b: [*optional*] the end of the interval of the possible values
        :param num: [*optional*] resolution of the interval.
        :return CDF,values, fig: values is the 1D-array of considered interval from 0 to x, CDF is the 1D-array of corresponding cumulative probability values, and if the plot option is set to True a figure will also be outputed.


        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> cdf,x,fig=cdf_normal(mean=0,sd=1,x=1,plot=True)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [2.8665157186802404e-07, 4.816529797224689e-07, ...]
                    >>> print(x)
                    [-5.         -4.8989899  -4.7979798  -4.6969697  -4.5959596  -4.49494949
                     -4.39393939 -4.29292929 -4.19191919 -4.09090909 -3.98989899 -3.88888889
                     -3.78787879 -3.68686869 -3.58585859 -3.48484848 -3.38383838 -3.28282828
                     -3.18181818 -3.08080808 -2.97979798 -2.87878788 -2.77777778 -2.67676768
                     -2.57575758 -2.47474747 -2.37373737 -2.27272727 -2.17171717 -2.07070707
                     -1.96969697 -1.86868687 -1.76767677 -1.66666667 -1.56565657 -1.46464646
                     -1.36363636 -1.26262626 -1.16161616 -1.06060606 -0.95959596 -0.85858586
                     -0.75757576 -0.65656566 -0.55555556 -0.45454545 -0.35353535 -0.25252525
                     -0.15151515 -0.05050505  0.05050505  0.15151515  0.25252525  0.35353535
                      0.45454545  0.55555556  0.65656566  0.75757576  0.85858586  0.95959596
                      1.        ]
                     >>> print(fig)
                     Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """





    ys,xs=normal_dist(mean,sd,a=a,b=b,num=100) #creates the normal distribution with the given mean and standard deviation.
    if x>=xs[0] and x<=xs[-1]: #checks whether the requested cdf from 0 to x is within the considered range of normal distribution. The normal distribution function of pywinda plots the distributino for +-5 times the standard deviation, more than 99.7% of all the values lie within this range.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(xs):
            if val>=x:
                loc=ind
                break
        cdf=[]
        for i in range(loc):
            cdf.append(0.5*(1+math.erf((xs[i]-mean)/(sd*math.sqrt(2))))) #used the error function from math module of python.
        cdf.append(0.5*(1+math.erf((x-mean)/(sd*math.sqrt(2)))))
        final_xs=xs[0:loc]
        final_xs=np.append(final_xs,x)
        if plot ==True:
            figure,ax=pwploter.plot(final_xs,cdf,title="Cumulative Distribution Function",xlabel='Values [-]',ylabel='Probability [-]',text={'mean':mean,'Standard deviation':sd})
            return cdf, final_xs, figure # returns y and x and the final figure if plot
        elif plot==False:
            return cdf,final_xs
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range of -+5 times the standard deviation.")









###################################
#####The drafts section ###########
# cdf,x=cdf_normal(0,1,5)
# cdf1,x=cdf_normal(0,1,-5)
# print(max(cdf1))
#######The drafts section ends here###########
##############################################