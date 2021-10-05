Introduction
==============

In PyWinda library there are currently two modules which are maintained regularly. The pywinda ("written in lower case") is the main module which creates a windfarm. The second module is dfm_module, which does all the reliability calculations.

In pywinda, there are two types of supported wind turbines, the single rotor turbiens (SRT) and multirotor turbines (MRT). It is always necessary to make a wind farm in pywinda first. Later you can add more turbines and also add an environment to the already created wind farm. Note that you can not create an standalone wind turbine without assigning them to a wind farm. However, you can make several standalone environments and assign them to the wind farms one at a time.