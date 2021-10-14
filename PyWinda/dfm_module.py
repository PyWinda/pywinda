import pwploter #only for documentation
# from PyWinda import pwploter # for default and for pypi
import numpy as np
from numpy.random import default_rng
import math
import matplotlib.pyplot as plt


pgreen1='#009C86'
pgreen2='#0397A1'
pblue='#05354B'
pred='#96394E'
ppink='#ECA48E'
pyellow='#ECD384'


def number_of_simsulaions(standard_error_of_mean,confidence_level,standard_normal_statistics,standard_deviaton_of_the_output):
    """
    """



def normal_dist(mean,sd,num=1000,plot=False,seed=None,bins=100):
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
                    >>> samples,pr,bins,fig=normal_dist(mean=20,sd=2,plot=True,seed=12)
                    >>> print(samples) #doctest:+ELLIPSIS
                    [19.98634644 22.09228658 21.48317684 21.44791308 ...]
                    >>> print(fig)
                    Figure(1000x800)


        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    rng=default_rng(seed) #the default random number generator
    y=rng.normal(loc=mean, scale=sd, size=num)
    figure, ax, counts, bins_array = pwploter.hist(y, bins=bins, title="Normal Distribution", xlabel='Values [-]',
                                                   ylabel='Probability [-]',
                                                   text={'mean': mean, 'Standard deviation': sd,
                                                         'Number of samples': num, 'Bins': bins})
    if plot:
        ax.plot(bins_array, 1 / (sd * np.sqrt(2 * np.pi)) *
             np.exp(- (bins_array - mean) ** 2 / (2 * sd ** 2)),
             linewidth=2, color=pred)
        return y,counts,bins_array, figure # returns samples counts in bins, bins array and the figure.
    else:
        return y, counts, bins_array


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
    cumSum = np.cumsum(hist)
    cumSum = cumSum * dx
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
            figure, ax = pwploter.plot(final_xs, final_cumSum, title="Normal Distribution", xlabel='Values [-]',ylabel='Probability [-]',
                                       text={'mean': mean, 'Standard deviation': sd, 'Number of samples': num,
                                             'Bins': bins, 'x':x})
            return portion_of_y,final_cumSum,final_xs, figure  # returns y and x and the final figure if plot
        elif plot==False:
            return portion_of_y,cumSum,bin_edges  #returns y and x if not plot is done
    elif x==None and plot==True:
        figure, ax = pwploter.plot(bin_edges[:-1], cumSum, title="Normal Distribution", xlabel='Values [-]',
                                   ylabel='Probability [-]',
                                   text={'mean': mean, 'Standard deviation': sd, 'Number of samples': num,
                                         'Bins': bins})
        return y,cumSum,bin_edges ,figure  # returns y and x and the final figure if plot

    elif x==None and plot==False:
        return y,cumSum,bin_edges
    else: # if the x is outside the +-5 times the standard deviation.
        raise Exception ("Out of range, please make sure that the point of interest x is with the range of -+5 times the standard deviation.")










###################################
#####The drafts section ###########

#######The drafts section ends here###########
##############################################