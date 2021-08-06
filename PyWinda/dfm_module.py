from PyWinda import pywinda as pw
import numpy as np


###################################
#####The drafts section ###########
x=np.random.uniform(3,6,100,500)

y=np.random.triangular(3,6,100,500)
a=0
for x in y:
    if x==6:
        a=a+1
    else:
        print(x)
print(a)
# print(a/50)
# print(y)
def dummy(a,b):
    return a+b

import matplotlib.pyplot as plt
h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
             density=True)
plt.show()
#######The drafts section ends here###########
##############################################

def number_of_simsulaions(standard_error_of_mean,confidence_level,standard_normal_statistics,standard_deviaton_of_the_output):
    """
        This function estimates the recommended number of Monte Carlo Simulation given the parameters.

        :param standard_error_of_mean: [*req*] the given unique ID.
        :param confidence_level: [*req*] the given unique ID.
        :param standard_normal_statistics: [*req*] the given unique ID.
        :param standard_deviaton_of_the_output: [*req*] the given unique ID.
         \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    x=1
    return x