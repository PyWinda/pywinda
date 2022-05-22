import pandas as pd
import pwploter #only for documentation and for gitub
# from PyWinda import pwploter # for default (for checking pytest) and for pypi compilation
from PyWinda import pywinda #for default (for checking pytest) and for pypi compilation
import numpy as np
from numpy.random import default_rng
from time import perf_counter_ns
from matplotlib import pyplot as plt

pgreen1='#009C86'
pgreen2='#0397A1'
pblue='#05354B'
pred='#96394E'
ppink='#ECA48E'
pyellow='#ECD384'


def number_of_simsulaions(standard_error_of_mean,confidence_level,standard_normal_statistics,standard_deviaton_of_the_output):
    """
    """


def pdf_normal(mean,sd,num=1000,plot=False,seed=None,bins=100):
    """
        This function generates the normal (Gaussian) distribution, for a given mean value and standard deviation.

        :param mean: [*req*] the mean of the distribution
        :param sd: [*req*]  the standard deviation of the distribution
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,counts,bins, fig: s is the 1D-array of generated samples, counts is the 1D-array of corresponding probability values to different bins, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> samples,pr,bins,fig=pdf_normal(mean=20,sd=2,plot=True,seed=12)
                    >>> print(samples) #doctest:+ELLIPSIS
                    [19.98634644 22.09228658 21.48317684 21.44791308 ...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    rng=default_rng(seed) #the default random number generator
    y=rng.normal(loc=mean, scale=sd, size=num)
    counts1,bins_array1=np.histogram(y,bins=bins,density=True)
    if plot:
        figure, ax, counts, bins_array = pwploter.hist(y,density=True, bins=bins, title="Normal Distribution", xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'mean': mean, 'Standard deviation': sd,
                                                             'Number of samples': num, 'Bins': bins})
        ax.plot(bins_array, 1 / (sd * np.sqrt(2 * np.pi)) *
             np.exp(- (bins_array - mean) ** 2 / (2 * sd ** 2)),
             linewidth=2, color=pred)
        return y,counts,bins_array, figure # returns samples counts in bins, bins array and the figure.
    else:
        return y, counts1, bins_array1
def cdf_normal(mean,sd,x=None,num=1000,plot=False,seed=None,bins=100):
    """
        This function generates the cumulative distribution function of the normal distributin function with the given parameters.

        :param mean: [*req*] the mean of the distribution
        :param sd: [*req*]  the standard deviation of the distribution
        :param x: [*optional*]  if any value is given the cdf will be generated only upto x.
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,cumSum,bins, fig: s is the 1D-array of generated values, cumSum is the 1D-array of calculated cumulative probability values, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> s,cdf,bins,fig=cdf_normal(mean=0,sd=1,x=1,plot=True,seed=145)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [0.001      0.001      0.001      0.001      0.001      0.001...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng = default_rng(seed)  # the default random number generator
    y = rng.normal(loc=mean, scale=sd, size=num)
    hist, bin_edges = np.histogram(y, bins=bins, density=True) #outputs all the number of outputs in every bin in density form.
    dx = bin_edges[-1] - bin_edges[-2] #dx is constant always
    cumSum = np.cumsum(abs(hist))
    cumSum = cumSum * abs(dx)
    if x!=None and x>=bin_edges.min() and x<=bin_edges.max(): #checks whether the requested cdf from 0 to x is within the considered range of normal distribution.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(bin_edges):
            if val>=x:
                loc=ind
                break
        xs=bin_edges[0:loc] #truncates only the portion of bin_edges less than x. element at loc is not included.
        xs=np.array(xs)
        final_xs=np.append(xs,x) #x is added to the end of interval
        cumSum_temp=cumSum[0:loc] #truncates only the potin of cumSum for all number less than x. element at loc is not inlcuded.
        lastelement=cumSum_temp[-1]+(bin_edges[loc]-x)* 1 / (sd * np.sqrt(2 * np.pi)) *np.exp(- (x - mean) ** 2 / (2 * sd ** 2))
        final_cumSum=np.append(cumSum_temp,lastelement)
        y_sorted=np.sort(y)
        loc_y=None
        for index,value in enumerate(y_sorted):
            if value>=x:
                loc_y=index
                break
        portion_of_y=y_sorted[:loc_y]
        if plot ==True:
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Normal Distribution CDF", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'mean': mean, 'Standard deviation': sd, 'Number of samples': num,
                                             'Bins': bins, 'x':x})
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return portion_of_y,final_cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(bin_edges[1:], cumSum, title="Normal Distribution CDF", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'mean': mean, 'Standard deviation': sd, 'Number of samples': num,
                                         'Bins': bins})
        return y,cumSum,bin_edges ,figure  # returns y and x and the final figure if plot

    elif x==None and plot==False:
        return y,cumSum,bin_edges
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range.")


def pdf_triangular(low,mode,high,num=1000,plot=False,seed=None,bins=100):
    """
            This function generates the triangular probabiliyt density function, for a given low, mode and high values.

            :param low: [*req*] the lowest number in triangular distribution.
            :param mode: [*req*]  the mode of the triangular distribution.
            :param high: [*req*] the highest number in triangular distribution.
            :param num: [*optional*] number of samples, by default 1000.
            :param plot: [*optional*] if True a figure will also be returned.
            :param seed: [*optional*] use the same seed number to produce the same distribution.
            :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
            :return s,counts,bins, fig: s is the 1D-array of generated samples, counts is the 1D-array of corresponding probability values to different bins, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

            :Example:

                        >>> from PyWinda import pywinda as pw
                        >>> samples,pr,bins,fig=pdf_triangular(low=1.9,mode=2,high=2.1,plot=True,seed=12)
                        >>> print(samples) #doctest:+ELLIPSIS
                        [1.97082718 2.06736656 1.96153379 ...]
                        >>> print(fig)
                        Figure(1000x800)


            \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng=default_rng(seed)
    samples=rng.triangular(low,mode,high,size=num)
    counts,bins_array=np.histogram(samples,bins=bins,density=True)
    if plot:
        figure, ax, counts_plot, bins_array_plot = pwploter.hist(samples, bins=bins, title="Triangular PDF",
                                                       xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'Lowest value': low, 'Mode': mode, 'Highes value': high,
                                                             'Number of samples': num, 'Bins': bins})
        atoc=[]
        ctob=[]
        for i in samples:
            if i<=mode:
                atoc.append(i)
            elif i>mode:
                ctob.append(i)

        atoc=np.array(atoc)
        ctob=np.array(ctob)

        ax.plot(atoc, 2*(atoc-low)/((high-low)*(mode-low)),linewidth=2, color=pred)
        ax.plot(ctob,2*(high-ctob)/((high-low)*(high-mode)),linewidth=2,color=pred)
        return samples, counts_plot, bins_array_plot, figure  # returns samples counts in bins, bins array and the figure.
    else:
        return samples, counts, bins_array
def cdf_triangular(low,mode,high,x=None,num=1000,plot=False,seed=None,bins=100):
    """
        This function generates the cumulative distribution function of the triangular distributin function with the given parameters.

        :param low: [*req*] the lowest number in triangular distribution.
        :param mode: [*req*]  the mode of the triangular distribution.
        :param high: [*req*] the highest number in triangular distribution.
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,cumSum,bins, fig: s is the 1D-array of generated values, cumSum is the 1D-array of calculated cumulative probability values, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> s,cdf,bins,fig=cdf_triangular(low=4,mode=8,high=12,x=6,plot=True,seed=148)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [0.001      0.001      0.001      0.002      0.003      0.005...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng = default_rng(seed)  # the default random number generator
    y = rng.triangular(low, mode,high, size=num)
    hist, bin_edges = np.histogram(y, bins=bins, density=True) #outputs all the number of samples in every bin in density form.
    dx = bin_edges[-1] - bin_edges[-2] #dx is constant always
    cumSum = np.cumsum(hist)
    cumSum = cumSum * dx
    if x!=None and x>=bin_edges.min() and x<=bin_edges.max(): #checks whether the requested cdf from lowest to x is within the considered range of normal distribution.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(bin_edges):
            if val>=x:
                loc=ind
                break
        xs=bin_edges[0:loc] #truncates only the portion of bin_edges less than x. element at index loc is not included.
        xs=np.array(xs)
        final_xs=np.append(xs,x) #x is added to the end of interval
        cumSum_temp=cumSum[0:loc] #truncates only the potin of cumSum for all number less than x. element at loc is not inlcuded.
        lastelement=0
        if x<=mode:
            lastelement=cumSum_temp[-1]+(bin_edges[loc]-x)*2*(x-low)/((high-low)*(mode-low))
        elif x>mode:
            lastelement=cumSum_temp[-1]+(bin_edges[loc]-x)*2*(high-x)/((high-low)*(high-mode)) #last element plus width of the intervel times the height of the probability.
        final_cumSum=np.append(cumSum_temp,lastelement)
        y_sorted=np.sort(y)
        loc_y=None
        for index,value in enumerate(y_sorted):
            if value>=x:
                loc_y=index
                break
        portion_of_y=y_sorted[:loc_y]
        if plot ==True:
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Triangular CDF", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'Low': low, 'Mode': mode,'High': high , 'Number of samples': num,
                                             'Bins': bins, 'x':x})
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return portion_of_y,cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(bin_edges[1:], cumSum, title="Triangular CDF", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'Low': low, 'Mode': mode,'High': high ,'Number of samples': num,
                                         'Bins': bins})
        return y,cumSum,bin_edges ,figure  # returns y and x and the final figure if plot
    elif x==None and plot==False:
        return y,cumSum,bin_edges
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range.")


def pdf_weibull(shape,scale=1,num=1000,plot=False,seed=None,bins=100):
    """
            This function generates the Weibull probabiliyt density function, for a given shape factor.

            :param shape: [*req*] shape of the weibull distribution.
            :param num: [*optional*] number of samples, by default 1000.
            :param plot: [*optional*] if True a figure will also be returned.
            :param seed: [*optional*] use the same seed number to produce the same distribution.
            :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
            :return s,counts,bins, fig: s is the 1D-array of generated samples, counts is the 1D-array of corresponding probability values to different bins, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

            :Example:

                        >>> from PyWinda import pywinda as pw
                        >>> samples,pr,bins,fig=pdf_weibull(shape=2,plot=True,seed=15)
                        >>> print(samples) #doctest:+ELLIPSIS
                        [1.58104874 1.23382765 0.53867083 0.20286241 1.24978154 0.49239706...]
                        >>> print(fig)
                        Figure(1000x800)


            \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng=default_rng(seed)
    samples=scale*rng.weibull(shape,size=num)
    counts,bins_array=np.histogram(samples,bins=bins,density=True)

    def weib(x, n, a):
        return (a / n) * (x / n) ** (a - 1) * np.exp(-(x / n) ** a)
    if plot:
        figure, ax, counts_plot, bins_array_plot = pwploter.hist(samples, bins=bins,title="Weibull PDF",
                                                       xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'Shape': shape,
                                                             'Number of samples': num, 'Bins': bins})
        # skale = counts_plot.max()/weib(bins_array_plot,n=scale,a=shape).max()

        ax.plot(bins_array_plot, weib(bins_array_plot,n=scale,a=shape),linewidth=2, color=pred) #TODO check the validity of the equation and add references
        return samples, counts_plot, bins_array_plot, figure  # returns samples counts in bins, bins array and the figure.
    else:
        return samples, counts, bins_array
def cdf_weibull(shape,scale=1,x=None,num=1000,plot=False,seed=None,bins=100):
    """
        This function generates the cumulative distribution function of the weibull distributin function with the given parameters.

        :param shape: [*req*] shape of the weibull distribution.
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,cumSum,bins, fig: s is the 1D-array of generated values, cumSum is the 1D-array of calculated cumulative probability values, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> s,cdf,bins,fig=cdf_weibull(shape=3,plot=True,seed=148)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [0.001 0.001 0.001 0.001 0.002 0.002 0.005 0.007 0.008 0.009 0.01  0.01...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng = default_rng(seed)  # the default random number generator
    y = scale*rng.weibull(shape, size=num)
    hist, bin_edges = np.histogram(y, bins=bins, density=True) #outputs all the number of samples in every bin in density form.
    dx = bin_edges[-1] - bin_edges[-2] #dx is constant always
    cumSum = np.cumsum(hist)
    cumSum = cumSum * dx
    if x!=None and x>=bin_edges.min() and x<=bin_edges.max(): #checks whether the requested cdf from lowest to x is within the considered range of normal distribution.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(bin_edges):
            if val>=x:
                loc=ind
                break
        xs=bin_edges[0:loc] #truncates only the portion of bin_edges less than x. element at index loc is not included.
        xs=np.array(xs)
        final_xs=np.append(xs,x) #x is added to the end of interval
        cumSum_temp=cumSum[0:loc] #truncates only the potin of cumSum for all number less than x. element at loc is not inlcuded.
        lastelement=cumSum_temp[-1]+(bin_edges[loc]-x)*shape/2*(x/2)**(shape-1)*np.exp((-1*(x)**shape)) #last element plus width of the intervel times the height of the probability.
        final_cumSum=np.append(cumSum_temp,lastelement)
        y_sorted=np.sort(y)
        loc_y=None
        for index,value in enumerate(y_sorted):
            if value>=x:
                loc_y=index
                break
        portion_of_y=y_sorted[:loc_y]
        if plot ==True:
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Weibull CDF", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'Shape':shape,'Number of samples': num,
                                             'Bins': bins, 'x':x})
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return portion_of_y,cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(bin_edges[1:], cumSum, title="Weibull CDF", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'Shape':shape,'Number of samples': num,
                                         'Bins': bins})
        return y,cumSum,bin_edges ,figure  # returns y and x and the final figure if plot
    elif x==None and plot==False:
        return y,cumSum,bin_edges
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range.")

def pdf_poisson(mean=1,num=1000,plot=False,seed=None):
    """
            This function generates the Poisson probabiliyt mass function, for a given mean value.

            :param mean: [*req*] mean of the Poisson distribution.
            :param num: [*optional*] number of samples, by default 1000.
            :param plot: [*optional*] if True a figure will also be returned.
            :param seed: [*optional*] use the same seed number to produce the same distribution.
            :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
            :return s,counts,bins, fig: s is the 1D-array of generated samples, counts is the 1D-array of corresponding probability values to different bins, bins is the 1D-array of bins, and fig is to retrieve generated figure, only if plot is set to True.

            :Example:

                        >>> from PyWinda import pywinda as pw
                        >>> samples,pr,bins,fig=pdf_poisson(mean=2,plot=True,seed=15)
                        >>> print(samples) #doctest:+ELLIPSIS
                        [3 1 2...]
                        >>> print(fig)
                        Figure(1000x800)


            \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng=default_rng(seed)
    samples=rng.poisson(mean,size=num)
    bins = np.arange(min(samples), max(samples) + 1.5) - 0.5
    counts,bins_array=np.histogram(samples,bins=bins,density=True) #Done extra to return if plot is False.
    def poisson(x, mean):
        res=[]
        for i in x:
            res.append((int(mean) ** int(i)) * np.exp(-mean) / np.math.factorial(i))
        return res
    if plot:
        figure, ax, counts_plot, bins_array_plot = pwploter.hist(samples, bins=bins,title="Poisson PMF (discrete distribution)",
                                                       xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'Mean': mean,
                                                             'Number of samples': num})
        ax.plot(np.unique(samples), poisson(x=np.unique(samples),mean=mean),linewidth=2, color=pred,marker='o') #TODO check the validity of the equation and add references
        return samples, counts_plot, np.unique(samples), figure  # returns samples counts in bins, bins array and the figure.
    else:
        return samples, np.unique(samples), bins_array
def cdf_poisson(mean=1,x=None,num=1000,plot=False,seed=None):
    """
        This function generates the cumulative distribution function of the Poisson distributin function with the given parameters.

        :param mean: [*req*] mean of the Poisson distribution.
        :param x: [*optional*] any positive integer within the range of CDF, if given CDF will be calculated until this point.
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,cumSum,bins, fig: s is the 1D-array of generated values, cumSum is the 1D-array of calculated cumulative probability values, bins is the 1D-array of bins, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> s,cdf,bins,fig=cdf_poisson(mean=3,plot=True,seed=148)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [0.047 0.191 0.414 0.641 0.803...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng = default_rng(seed)  # the default random number generator
    y = rng.poisson(mean,size=num)
    bins = np.arange(min(y), max(y) + 1.5) - 0.5
    counts,bins_array=np.histogram(y,bins=bins,density=True) #in case no plot this will be returned
    def poisson(x, mean):
        res=[]
        for i in x:
            res.append((int(mean) ** int(i)) * np.exp(-mean) / np.math.factorial(i))
        return res
    hist, bin_edges = np.histogram(y, bins=bins, density=True) #outputs all the number of samples in every bin in density form.
    uniques=bin_edges[:-1]+0.5 #excludes last element of the bin and adds 0.5 to show middle of the bins
    dx = bin_edges[-1] - bin_edges[-2] #dx is constant always
    cumSum = np.cumsum(hist)
    cumSum = cumSum * dx
    if x!=None and type(x)==int and x>=min(uniques) and x<=max(uniques): #checks whether the requested cdf from lowest to x is within the considered range of normal distribution.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(uniques):
            if val>=x:
                loc=ind
                break
        xs=uniques[0:loc] #truncates only the portion of bin_edges less than x. element at index loc is not included.
        xs=np.array(xs)
        final_xs=np.append(xs,x) #x is added to the end of interval
        cumSum_temp=cumSum[0:loc] #truncates only the portin of cumSum for all number less than x. element at loc is not inlcuded.
        lastelement=cumSum_temp[-1]+poisson(x=[x],mean=mean) #last element plus width of the intervel times the height of the probability. For a Poisson distributio the width is always 1.
        final_cumSum=np.append(cumSum_temp,lastelement)
        y_sorted=np.sort(y)
        loc_y=None
        for index,value in enumerate(y_sorted):
            if value>x: #selects all the values from sample sapce which are less then and equal to x
                loc_y=index
                break
        portion_of_y=y_sorted[:loc_y] #selects all the values from sample sapce which are less then and equal to x
        if plot ==True:
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Weibull CDF", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'Mean':mean,'Number of samples': num,
                                             'x':x},style='o',axes_ticks='xy')
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return np.array(portion_of_y),cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(uniques, cumSum, title="Poisson CDF (Discrete distribution)", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'Shape':mean,'Number of samples': num},style='o',axes_ticks='x')
        return y,cumSum,uniques ,figure  # returns y and x and the final figure if plot
    elif x==None and plot==False:
        return y,cumSum,uniques
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is within the range and it is a positive integer.")


def pdf_exponential(rate,num=1000,plot=False,seed=None,bins=100):
    """
            This function generates the exponential probabiliyt density function, for a given mean value.

            :param shape: [*req*] rate of the exponenetial distribution which is mean (arriavl rate) of its Poisson distribution.
            :param num: [*optional*] number of samples, by default 1000.
            :param plot: [*optional*] if True a figure will also be returned.
            :param seed: [*optional*] use the same seed number to produce the same distribution.
            :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
            :return s,counts,bins, fig: s is the 1D-array of generated samples, counts is the 1D-array of corresponding probability values to different bins, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

            :Example:

                        >>> from PyWinda import pywinda as pw
                        >>> samples,pr,bins,fig=pdf_exponential(rate=2,plot=True,seed=15)
                        >>> print(samples) #doctest:+ELLIPSIS
                        [1.24985756e+00 7.61165330e-01 1.45083129e-01 2.05765792e-02...]
                        >>> print(fig)
                        Figure(1000x800)


            \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng=default_rng(seed)
    samples=rng.exponential(1/rate,size=num)
    counts,bins_array=np.histogram(samples,bins=bins,density=True)

    def expon(x, rate):
        return rate * np.exp(-(x *rate))
    if plot:
        figure, ax, counts_plot, bins_array_plot = pwploter.hist(samples, bins=bins,title="Exponential distribution PDF",
                                                       xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'Rate [mean of Poisson counter part]': rate,
                                                             'Number of samples': num, 'Bins': bins})
        ax.plot(bins_array_plot, expon(bins_array_plot,rate=rate),linewidth=2, color=pred)
        return samples, counts_plot, bins_array_plot, figure  # returns samples counts in bins, bins array and the figure.
    else:
        return samples, counts, bins_array
def cdf_exponential(rate,scale=1,x=None,num=1000,plot=False,seed=None,bins=100): #TODO needs more work and approval
    """
        This function generates the cumulative distribution function of the exponential distributin function with the given parameters.

        :param shape: [*req*] rate of the exponenetial distribution which is mean (arriavl rate) of its Poisson distribution.
        :param x: [*optional*] any positive real number within the range of CDF, if given the CDF will be calculated until this point.
        :param num: [*optional*] number of samples, by default 1000.
        :param plot: [*optional*] if True a figure will also be returned.
        :param seed: [*optional*] use the same seed number to produce the same distribution.
        :param bins: [*optional*] number of bins to divide the number of samples to. Default value is 100.
        :return s,cumSum,bins, fig: s is the 1D-array of generated values, cumSum is the 1D-array of calculated cumulative probability values, bins is the 1D-array of bins edges, and fig is to retrieve generated figure, only if plot is set to True.

        :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> s,cdf,bins,fig=cdf_exponential(rate=3,plot=True,seed=148)
                    >>> print(cdf) #doctest:+ELLIPSIS
                    [0.059 0.117 0.172 0.235 0.292 0.334 0.392 0.443 0.473...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    rng = default_rng(seed)  # the default random number generator
    y=rng.exponential(1/rate,size=num)
    hist, bin_edges = np.histogram(y, bins=bins, density=True) #outputs all the number of samples in every bin in density form.
    dx = bin_edges[-1] - bin_edges[-2] #dx is constant always
    cumSum = np.cumsum(hist)
    cumSum = cumSum * dx

    if x!=None and x>=bin_edges.min() and x<=bin_edges.max(): #checks whether the requested cdf from lowest to x is within the considered range of normal distribution.
        loc=None #location of the xs greater than or equal to x, finds where the x is located in the given range
        for ind,val in enumerate(bin_edges):
            if val>=x:
                loc=ind
                break
        xs=bin_edges[0:loc] #truncates only the portion of bin_edges less than x. element at index loc is not included.
        xs=np.array(xs)
        final_xs=np.append(xs,x) #x is added to the end of interval
        cumSum_temp=cumSum[0:loc] #truncates only the potin of cumSum for all number less than x. element at loc is not inlcuded.
        lastelement=cumSum_temp[-1]+(bin_edges[loc]-x)*rate * np.exp(-(x *rate)) #last element plus width of the intervel times the height of the probability.
        final_cumSum=np.append(cumSum_temp,lastelement)
        y_sorted=np.sort(y)
        loc_y=None
        for index,value in enumerate(y_sorted):
            if value>=x:
                loc_y=index
                break
        portion_of_y=y_sorted[:loc_y]
        if plot ==True:
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Exponential CDF", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'Rate':rate,'Number of samples': num,
                                             'Bins': bins, 'x':x})
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return portion_of_y,cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(bin_edges[1:], cumSum, title="Weibull CDF", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'Rate':rate,'Number of samples': num,
                                         'Bins': bins})
        return y,cumSum,bin_edges ,figure  # returns y and x and the final figure if plot
    elif x==None and plot==False:
        return y,cumSum,bin_edges
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range.")


def monte_carlo(performance_Func,condition=None,report=False,plot=False):
    start=perf_counter_ns()
    result=performance_Func
    number_of_samples = len(result)
    histValues,bin_edges=np.histogram(result,density=True,bins=number_of_samples)
    dx=bin_edges[-1]-bin_edges[-2]

    product=histValues*dx
    a=0
    cumSum=[]
    for i in product:
        a=a+i
        cumSum.append(a)
    # print(cumSum)
    # plt.show()
    P90=np.interp(0.1,cumSum,bin_edges[1:],left=None,right=None)  #P90 means 90% of the estimates exceed the P90 estimate. The Cumulative sum of 10% at x, tells us that the 10% of the values are x or less than x, meaning 90 of the rest is greater than x. P90 is here x.
    P75=np.interp(0.25,cumSum,bin_edges[1:],left=None,right=None)
    P50=np.interp(0.5,cumSum,bin_edges[1:],left=None,right=None)
    P25=np.interp(0.75,cumSum,bin_edges[1:],left=None,right=None)
    P10=np.interp(0.9,cumSum,bin_edges[1:],left=None,right=None)


    # print(hadaf)
    percentage_over='No conditions given'
    percentage_below='No conditions given'
    if plot==True:
        figure, ax, counts, bins_array = pwploter.hist(result, density=True, nrows=2,ncols=1,bins=100, title="Simulation Results",
                                                       xlabel='Values [-]',
                                                       ylabel='Probability [-]',
                                                       text={'Number of simulations': number_of_samples})

        #      np.exp(- (bins_array - mean) ** 2 / (2 * sd ** 2)),
        #      linewidth=2, color=pred)
        # return y,counts,bins_array, figure # returns samples counts in bins, bins array and the figure.

        figure2,ax2=plt.subplots()
        ax2.plot(bin_edges[1:], cumSum)

    if condition != None:
        lower = []
        higher = []
        for i in result:
            if i <= condition:
                lower.append(i)
            elif i > condition:
                higher.append(i)
        number_of_lower = len(lower)
        number_of_higher = len(higher)
        percentage_over=number_of_higher / number_of_samples * 100
        percentage_over=f'{round(percentage_over,2):.2f} %'
        percentage_below=number_of_lower / number_of_samples * 100
        percentage_below=f'{round(percentage_below,2):.2f} %'



    end = perf_counter_ns()
    duration=(end-start)/1000000 #convert the duration to milli seconds.
    reports_Dic={'Property':['Duration of Monte Carlo Simulation','Percentage over '+ str(condition),'Percentage below '+ str(condition), 'Number of Simulations', 'mean value','Standard deviation','Variance', 'P90','P75','P50','P25','P10'],
                 'Value':[f'{round(duration,2)} ms', percentage_over,percentage_below,number_of_samples,f'{round(result.mean(),3):.3f}',f'{round(result.std(),3):.3f}',f'{round(result.var(),3):.3f}',f'{round(P90,3):.3f}',f'{round(P75,3):.3f}',f'{round(P50,3):.3f}',f'{round(P25,3):.3f}',f'{round(P10,3):.3f}']}
    report_dataframe=pd.DataFrame(reports_Dic)

    print(report_dataframe)


#
if __name__=='__main__':
    ###################################
    # #####The drafts section ###########
    #
    # def performance(a,b,f):
    #
    #     p=f/a/b
    #     return p

    # a=pdf_triangular(0.019,0.02,0.021,num=10000,plot=False,bins=100,seed=1500)[0]
    # b=pdf_triangular(0.0285,0.03,0.0315,num=10000)[0]
    # f=pdf_weibull(2.5,scale=11300,num=10000,plot=False)[0]
    # g=cdf_weibull(2.5,scale=11300,num=1000, plot=True)
    # print(a)
    # monte_carlo(performance(a,b,f), 7699789,plot=True)
    turbines=[]
    CurslackFarm=pywinda.windfarm('Curslack')
    for i in range(200): CurslackFarm.addTurbine(uniqueID='WT'+str(i))
    # print(CurslackFarm.info)
    # print(pywinda.WT0.TFR)

    dist={}
    for i in range (200):
        dist['DistWT'+str(i+1)]=pdf_poisson(mean=5,num=10000000)[0]
    # print(dist['DistWT1'])
    res=[0 for i in range(10000000)]
    for i in range(200):
        res=res+dist['DistWT'+str(i+1)]
    data=monte_carlo(res,plot=True)
    # print(res)
    # plt.hist(res,bins=100)
    plt.show()
    # print(dist['DistWT1'])
    # print(dist['DistWT2'])

    # print(len(res))
    # a=[1,2,3]
    # b=[1,2,3]
    # c=a+b
    # print(c)
    # value,counts=np.unique(res,return_counts=True)
    #
    # inds=[]
    # for indx,i in enumerate(res):
    #     # print(indx)
    #     if i==107:
    #         inds.append(indx)
    #         # print(res[indx])
    # print('Lenght of inds',len(inds))
    # forms={}
    # for index in inds:
    #     temp=[]
    #     for i in range(20):
    #         temp.append(dist['DistWT' + str(i + 1)] [index])
    #     forms[str(index)]=temp
    # # print(forms)
    # now=np.unique(forms)
    # full=[]
    # for key in forms:
    #     full.append(tuple(forms[str(key)]))
    # # full=[set(i) for i in full]
    # print(len(full))
    # print(len(set(full)))
    # print('start of the for loop')
    # matches=0
    # for indx,i in enumerate(full):
    #     # print('Now it is: ',indx)
    #     for nxindex in np.arange(indx+1,len(full),1):
    #         # print('Next is: ',nxindex)
    #
    #         if i==full[nxindex]:
    #             # print('match')
    #             matches=matches+1
    #
    #
    #

        # print(i)
    #
    # print('There are matches: ',matches)
    # a=[1,2,3]
    # b=[1,2,3]
    # if a==b:
    #     print('worked')
    #
    # print(np.unique(full))

    # print(value)
    # print(np.where(res==59)[0])
    # print(count)
    # print(index)
    # print(value*count)
    # print(np.cumsum(count*value))

    # print('statis')
    # print(np.mean(res))
    # print(np.std(res))
    # pwploter.plot(value,counts)
    # cdf_normal(mean=50,sd=7,plot=True,num=100000)
    # WT1=pywinda.SRT('Windturbin')
    # print(WT1.TFR)
    #
    # samples,cdf,x=pdf_poisson(mean=WT1.TFR,plot=False,num=100000)
    # monte_carlo(res,condition=25)
    # print(max(np.cumsum(samples))/100000)
    # plt.show()
    # #######The drafts section ends here###########
    ##############################################