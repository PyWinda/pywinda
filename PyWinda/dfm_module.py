from PyWinda import pywinda as pw
from PyWinda import pwploter
import numpy as np
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

        \\----------------------------------------------------------------------------------------------------------------------------------------------------------

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

a,b,fig=normal_dist(0,1,plot=True)
fig.savefig("This.pdf")
plt.show()



#######The drafts section ends here###########
##############################################