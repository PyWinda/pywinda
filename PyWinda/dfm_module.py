from PyWinda import pywinda as pw
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



def normal_dist(mean,sd,a=0,b=0,num=1000):
    """
        This function generates the normal (Gaussian) distribution, for a given mean value and standard distribution in an interval of a to b or a default of -5*standard deviation to 5*standard defviations.

        :param mean: [*req*] the mean of the distribution
        :param sd: [*req*]  the standard deviation of the distribution
        :parm a: [*req*] the start of the interval
        :param b: [*req*] the end of the interval

    """
    a=mean-5*sd
    b=mean+5*sd
    interval=np.linspace(a,b,num) #creates the interval with the default number of seperation, here 100.
    y=[] #the normal distribution values
    for x in interval:
        y.append((1/(sd*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mean)/sd)**2))
    return y

###################################
#####The drafts section ###########
normal_dist(253,1)
print(np.exp(1))




# x=np.random.uniform(3,6,100)

# y=np.random.triangular(3,6,100,500)
# a=0
# for x in y:
#     if x==6:
#         a=a+1
#     else:
#         print(x)
# print(a)
# print(a/50)
# print(y)


# h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
#              density=True)
# plt.show()
#######The drafts section ends here###########
##############################################