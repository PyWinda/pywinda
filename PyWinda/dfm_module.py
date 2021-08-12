from PyWinda import pywinda as pw
from PyWinda import pwploter
import numpy as np
import matplotlib.pyplot as plt





def number_of_simsulaions(standard_error_of_mean,confidence_level,standard_normal_statistics,standard_deviaton_of_the_output):
    """
        This function estimates the recommended number of Monte Carlo Simulations for the given following set of parameters.

        :param standard_error_of_mean: [*req*] standard error of the mean.
        :param confidence_level: [*req*] the confidence level.
        :param standard_normal_statistics: [*req*] the standard cumulative normal distribution vale.
        :param standard_deviaton_of_the_output: [*req*] standard deviation of the output.

        :Example:

                   >>> Env = environment("C_Env")
                   # None


         \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """



def normal_dist(mean,sd,a=0,b=0,num=100,plot=False):
    """
        This function generates the normal (Gaussian) distribution, for a given mean value and standard distribution in an interval of a to b or a default of -5*standard deviation to 5*standard defviations.

        :param mean: [*req*] the mean of the distribution
        :param sd: [*req*]  the standard deviation of the distribution
        :parm a: [*req*] the start of the interval
        :param b: [*req*] the end of the interval
        :param num: [*optional*] resolution of the interval.
        :return x,y, plot: x the 1D-array of considered interval, and y the 1D-array of corresponding probability values.

    """

    a=mean-5*sd
    b=mean+5*sd
    x=np.linspace(a,b,num) #creates the interval with the default number of seperation, here 100.
    y=[] #the normal distribution values
    for i in x:
        y.append((1/(sd*np.sqrt(2*np.pi)))*np.exp(-0.5*((i-mean)/sd)**2))

    if plot ==True:
        figure,ax=pwploter.plotg(x,y,title="Normal Distribution",xlabel='Values [-]',ylabel='Probability [-]',text={'mean':mean,'Standard deviation':sd})
        return y, x, figure # returns y and x and the final figure if plot

    return y,x  #returns y and x if not plot is done




###################################
#####The drafts section ###########

a,b,fig=normal_dist(15,1,plot=True)
plt.show()



#######The drafts section ends here###########
##############################################