#Feb 2022

import numpy as np
import pandas as pd
from numpy.random import default_rng
#///////////////////// miscellaneous functions starts here
def cAngle(i):
   x=i % 360
   return x

def weib(x,A,k): #A is the scale and k is the shape factor
    return (k / A) * (x / A)**(k - 1) * np.exp(-(x / A)**k) #This function show the probabilty of occurence of a specific wind speed.
def weib_cumulative(x,A,k): #A is the scale and k is the shape factor
    return 1-np.exp(-1*(x/A)**k) #This function show the probabilty of occurence of a specific wind speed.
#///////////////////// miscellaneous functions ends here


class environment:
    """
       Creates the stand-alone environment and returns it with the given unique ID. By default, wind speeds from 0 m/s to 50 m/s with an increment of 0.5 m/s and also 360 degree with 1 degree increment are also added. The temperature of 25 degree Celsius and pressure of 101325 Pa is assumed. See example below:

       :param uniqueID: [*req*] the given unique ID.

       :Example:

           >>> Env = environment("C_Env")
           >>> #Creates an environment without assigning it to any wind farm.
           >>> print(Env.info.keys())
           dict_keys(['Wind directions', 'Sectors', 'Wind speeds', 'Pressure', 'Temperature', 'Wind probability', 'Scale parameter of wind distribution', 'Shape parameter of wind distribution'])
           >>> print(Env.info['Wind directions']) #doctest:+ELLIPSIS
           [0, 1, 2, 3, ...]
           >>> print(Env.info['Wind speeds']) # doctest:+ELLIPSIS
           [0.0, 0.5, 1.0, 1.5, 2.0, ...]

       \\----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    created_environments=[]

    def __init__(self, uniqueID):
        if uniqueID in environment.created_environments: #Checks if the environment ID is already taken
            raise Exception ("The environment unique ID [" + str(uniqueID) + "] is already taken.")
        else:
            if type(uniqueID) == str and len(uniqueID.split())==1:
                if uniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise Exception ("Another object with the same uniqe ID globally exists. New environment not created.")
                else:
                    globals()[uniqueID] = self    #environment is dynamicall created and referenced with the unique ID to the users assigned variable.
                    environment.created_environments.append(uniqueID) #we append the created environment to the list
                    self.uID=uniqueID
            else:
                raise Exception("Unique ID should be a string without spaces.")


        self.__conditionsDic={}
        self.__conditionsDic["Wind directions"]=[i for i in range(0,360)] #degrees
        self.__conditionsDic["Sectors"] = None
        self.__conditionsDic["Wind speeds"]=[i for i in np.arange(0,30.5,0.5)] #m/s
        self.__conditionsDic["Pressure"]= 101325 #pascals
        self.__conditionsDic["Air Density [kg/m^3]"]=1.225
        self.__conditionsDic["Temperature"]=25 #celcius
        self.__conditionsDic["Wind probability"]=[] #how often the wind blows in this sector
        self.__conditionsDic["Scale parameter of wind distribution"]=[] # the scale parameter of the wind distribution in the particular sector in m/s
        self.__conditionsDic["Shape parameter of wind distribution"]=[] # the shape parameter of the wind distribution in the particular sector

        self.windSectors=None

    @property
    def info(self):
        """
            Returns all the defined conditions of the environment.

           :param None:

           :Example:

               >>> dantysk=windfarm("DanTysk")
               >>> env=environment("D_Env")
               >>> print(env.info.keys())
               dict_keys(['Wind directions', 'Sectors', 'Wind speeds', 'Pressure', 'Temperature', 'Wind probability', 'Scale parameter of wind distribution', 'Shape parameter of wind distribution'])
               >>> print(env.info['Wind directions']) # doctest:+ELLIPSIS
               [0, 1, 2, 3, ...]
               >>> print(env.info['Wind speeds']) # doctest:+ELLIPSIS
               [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, ...]

           \----------------------------------------------------------------------------------------------------------------------------------------------------------

           """
        return self.__conditionsDic
    def windConditions(self,windProbability=[1/12 for i in range(12)], aParams=[7 for i in range(12)], kParams=[2.5 for i in range(12)]):
        """
                Creates and assigns the given wind conditions to the related environment. Returns the result as a data frame.
                Divides the 360 degrees to given number of sectors. By default it divides to 12 sectors and assigns the 12 standard names for every sector e.g. N_0 starts from 346 degrees and ends at 15 degrees.

                :param windProbability: [*opt*] the probabiliyt of wind presence in each sector, by default equal to 1/12.
                :param aParams: [*opt*] the scale factor of the weibull distribution of the wind in the sector, by default equal to 7 m/s .
                :param kParams: [*opt*] the shape factor of the weibull distribution of the wind int the sector, by default equla to 2.5.

                :Example:

                    >>> from PyWinda import pywinda as pw
                    >>> Env=pw.environment("C_Env2")


        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

          """
        #TODO che the example of the windConditions purpose.

        self.__conditionsDic["Wind probability"]=windProbability
        self.__conditionsDic["Scale parameter of wind distribution"]=aParams
        self.__conditionsDic["Shape parameter of wind distribution"]=kParams


    def makeSectors(self,n=12,sectorNames=["N_0","NNE_30","NEN_60","E_90","ESE_120","SSE_150","S_180","SSW_210","WSW_240","W_270","WNW_300","NNW_330"]):#by default the function will divide the sector in 12 regions
        """
        Creates the given sectors to the related environment. Returns the result as a data frame.
        Divides the 360 degrees to given number of sectors. By default it divides to 12 sectors and assigns the 12 standard names for every sector e.g. N_0 starts from 346 degrees and ends at 15 degrees.

        :param n: [*opt*] the number of sectors.
        :param sectorNames: [*opt*] names of the sectors given by user or default names for n=12.

        :Example:

            >>> Env=environment("C_Env2")
            >>> print(Env.makeSectors())
                  N_0  NNE_30  NEN_60   E_90  ...  WSW_240  W_270  WNW_300  NNW_330
            0   346.0    16.0    46.0   76.0  ...    226.0  256.0    286.0    316.0
            1   347.0    17.0    47.0   77.0  ...    227.0  257.0    287.0    317.0
            2   348.0    18.0    48.0   78.0  ...    228.0  258.0    288.0    318.0
            3   349.0    19.0    49.0   79.0  ...    229.0  259.0    289.0    319.0
            4   350.0    20.0    50.0   80.0  ...    230.0  260.0    290.0    320.0
            5   351.0    21.0    51.0   81.0  ...    231.0  261.0    291.0    321.0
            6   352.0    22.0    52.0   82.0  ...    232.0  262.0    292.0    322.0
            7   353.0    23.0    53.0   83.0  ...    233.0  263.0    293.0    323.0
            8   354.0    24.0    54.0   84.0  ...    234.0  264.0    294.0    324.0
            9   355.0    25.0    55.0   85.0  ...    235.0  265.0    295.0    325.0
            10  356.0    26.0    56.0   86.0  ...    236.0  266.0    296.0    326.0
            11  357.0    27.0    57.0   87.0  ...    237.0  267.0    297.0    327.0
            12  358.0    28.0    58.0   88.0  ...    238.0  268.0    298.0    328.0
            13  359.0    29.0    59.0   89.0  ...    239.0  269.0    299.0    329.0
            14    0.0    30.0    60.0   90.0  ...    240.0  270.0    300.0    330.0
            15    1.0    31.0    61.0   91.0  ...    241.0  271.0    301.0    331.0
            16    2.0    32.0    62.0   92.0  ...    242.0  272.0    302.0    332.0
            17    3.0    33.0    63.0   93.0  ...    243.0  273.0    303.0    333.0
            18    4.0    34.0    64.0   94.0  ...    244.0  274.0    304.0    334.0
            19    5.0    35.0    65.0   95.0  ...    245.0  275.0    305.0    335.0
            20    6.0    36.0    66.0   96.0  ...    246.0  276.0    306.0    336.0
            21    7.0    37.0    67.0   97.0  ...    247.0  277.0    307.0    337.0
            22    8.0    38.0    68.0   98.0  ...    248.0  278.0    308.0    338.0
            23    9.0    39.0    69.0   99.0  ...    249.0  279.0    309.0    339.0
            24   10.0    40.0    70.0  100.0  ...    250.0  280.0    310.0    340.0
            25   11.0    41.0    71.0  101.0  ...    251.0  281.0    311.0    341.0
            26   12.0    42.0    72.0  102.0  ...    252.0  282.0    312.0    342.0
            27   13.0    43.0    73.0  103.0  ...    253.0  283.0    313.0    343.0
            28   14.0    44.0    74.0  104.0  ...    254.0  284.0    314.0    344.0
            29   15.0    45.0    75.0  105.0  ...    255.0  285.0    315.0    345.0
            <BLANKLINE>
            [30 rows x 12 columns]



        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

          """
        sectorSpan = 360 / n
        eachS2E=[i for i in np.arange(1 - sectorSpan / 2, 360, sectorSpan)] #this makes a set of starts to end of each sector such that first sector starts from 0+1-sectorSpan / 2 goes to 360 (excluding 360) and the distance between consecutive units is equal to sectorSpan. The +1 makes sure that the sector starts and ends in the correct place. For example sector E_90 with n=12 starts from 90-30+1=61 and ends at 90+30=120
        sectorsDic = {}
        sectorNamesToReturn=sectorNames #this by default, of course user can give his/her own names as well.
        if n!=12: #After user give n other than 12, user can either give sectorNames or leave it, if left the script makes names automatically by assigning half othe span of the sector as the name of the sector
            if len(sectorNames)==12:
                sectorNamesToReturn = [str(i) for i in np.arange(0,360,sectorSpan)]
            elif len(sectorNames)!=12:
                sectorNamesToReturn=sectorNames
        if n == len(sectorNamesToReturn) and type(n) == int and n > 0: #this makes sure n is an integer and that the number of given sectors is equal to n if defined by user.
            for i in range(n):
                sectorsDic[sectorNamesToReturn[i]]=[cAngle(temp) for temp in np.arange(eachS2E[i],eachS2E[i+1],1)]
            self.windSectors=sectorsDic
            self.__conditionsDic["Sectors"]=sectorsDic
            return pd.DataFrame(sectorsDic)
        else:
            raise Exception("Number of sectors and proposed number of names are not equal.")

    def probabilityDistribution(self,aParams=[],kParams=[],probabs=[],avgWindSpeeds=[]):
       if len(aParams)|len(kParams)|len(probabs)|len(avgWindSpeeds)!=len(self.windSectors):
            raise Exception("Number of given parameters and existing number of sectors are not equal")
       else:
            pdDic={}
            SectorNames=self.__conditionsDic["Sectors"].keys()
            for index,i in enumerate(SectorNames):
                pdDic[i]=[aParams[index],kParams[index],probabs[index],avgWindSpeeds[index]]
            self.__conditionsDic["probabilityDistribution"]=pdDic
            print(pdDic)
            # self.__conditionsDic["ProbabilityDistributions"]=pdDic
            # print(len(self.windSectors))



    def test(self):
        return self.uID

class windfarm:

    """
    Creates wind farm object with the given unique ID. Pywinda will also create an internal shallow copy of the same windfarm object.

    :param uniqueID: [*req*] Unique Id of the wind farm as a string.

    :Example:
        >>> from PyWinda import pywinda as pw
        >>> curslack = pw.windfarm("Curslack_uID")
        >>> print(pw.Curslack_uID==curslack)
        True

    \-----------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    created_windfarms=[]
    def __init__(self,uniqueID,lifetime=25*365*24*3600):
        if uniqueID in windfarm.created_windfarms: #Checks if the wind farm ID is already taken
            raise Exception ("The wind farm unique ID [" + str(uniqueID) + "] is already taken.")
        else:
            if type(uniqueID) == str and len(uniqueID.split())==1:
                if uniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise Exception ("Another object with the same uniqe ID globally exists. New wind farm not created.")
                else:
                    globals()[uniqueID] = self    #wind farm is dynamicall created and referenced with the unique ID to the users assigned variable.
                    windfarm.created_windfarms.append(uniqueID) #we append the created wind farm to the list
                    self.uID=uniqueID
            else:
                raise Exception("Unique ID should be a string without spaces.")

        self.createdSRTs=[] #This is the store dictionary. Stores the wind turbine reference names created in a particular wind farm
        self.createdMRTs=[]
        self.farmEnvironment=None #A wind farm will have only one environment
        self.__numOfSRT=len(self.createdSRTs)
        self.__numOfMRT=len(self.createdMRTs)
        self.__allDistances=pd.DataFrame()
        self.lifetime=lifetime #by default 25 years in seconds


    @property #This helps to protect the info from direct changes by user
    def info(self):

        """
        Returns a data frame containing all the information about the wind farm.

        :param None:

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> curslack=pw.windfarm("uID_Curslack")
            >>> WT1=curslack.addTurbine('uID_WT1',turbineType='SRT',hubHeigt=120, x_horizontal=100,y_vertical=100)
            >>> WT2=curslack.addTurbine('uID_WT2',turbineType='SRT',hubHeigt=120, x_horizontal=150,y_vertical=150)
            >>> WT3=curslack.addTurbine('uID_MWT3',turbineType='MRT',hubHeigt=200, x_horizontal=300,y_vertical=300)
            >>> print(curslack.info)
                     Property               Value
            0       Unique ID        uID_Curslack
            1    Created SRTs  [uID_WT1, uID_WT2]
            2    Created MRTs          [uID_MWT3]
            3  Number of SRTs                   2
            4  Number of MRTs                   1

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """


        statistics={"Property":["Unique ID","Created SRTs", "Created MRTs","Number of SRTs","Number of MRTs"],
                    "Value":[self.uID,self.createdSRTs,self.createdMRTs,self.__numOfSRT,self.__numOfMRT]}
        return pd.DataFrame(statistics)

    @property
    def assets(self):

        """
        Returns all the unique IDs of all the assets in the windfarm e.g. single rotor turbines, multirotor tubines, met masts, etc.

        :param None:

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> curslack=pw.windfarm("uID_Curslack2")
            >>> WT1=curslack.addTurbine('uID_WT11',turbineType='SRT',hubHeigt=120)
            >>> WT2=curslack.addTurbine('uID_WT12',turbineType='SRT',hubHeigt=120)
            >>> WT3=curslack.addTurbine('uID_MWT13',turbineType='MRT',hubHeigt=200)
            >>> print(curslack.assets)
            ['uID_WT11', 'uID_WT12', 'uID_MWT13']

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """
        self.allassets=self.createdSRTs+self.createdMRTs#keeps the record of all assets in the wind farm
        return self.allassets

    def addRefTurbine(self, uniqueID, reference='NREL'):  ##This function helps to create a reference wind turbine and keep internal (inside the class) track of its name. It is not a deep copy, rather a reference.

        """
        By default adds a single rotor turbine (SRT) rference turbine to the related windfarm. Returns the created wind turbine with the given unique ID.
        The wind turbine would be callable via its unique name and via the assigned variable by user. Note that the referenced unique id is stored in library. Thus when calling the turbine via unique id, it should be prefixed by library name pywinda. See example below.

        :param uniqueID: [*req*] Unique ID of the wind turbine as string
        :param reference: [*opt*] Choose among 'NREL-5MW' or 'DTU-10MW' reference turbines


        :Example:

            >>> from PyWinda import pywinda as pw
            >>> DanTysk=pw.windfarm('DanTysk01')
            >>> WT1=DanTysk.addRefTurbine('Turbine1',reference='NREL')
            >>> print(pw.Turbine1.info)
                   Property                                              Value
            0   Unique Name                                           Turbine1
            1  x_horizontal                                                NaN
            2    y_vertical                                                NaN
            3      Diameter                                                120
            4    Hub height                                                120
            5          Area                                       11309.733553
            6    Windspeeds  [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, ...
            7            CP  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.198, 0.313, 0...


        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """

        if uniqueID in self.createdSRTs:  # Checks if the given unique Id already exists in the wind farm
            raise Exception("A wind turbine with the same unique ID in wind farm [ "+str(self.uID) +
                            " ] already exists. New turbine not added.")
        else:
            if type(uniqueID) == str and len(uniqueID.split()) == 1:
                if uniqueID in globals().keys():  # Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise Exception("A wind turbine witht the same uniqe ID globally exists. New turbine not added.")
                else:

                    if reference == "NREL":
                        NRELPower = [
                            0.19800,
                            0.31300,
                            0.37712,
                            0.41525,
                            0.44068,
                            0.45700,
                            0.46716,
                            0.47458,
                            0.47775,
                            0.47775,
                            0.47775,
                            0.47775,
                            0.47775,
                            0.47775,
                            0.47564,
                            0.47564,
                            0.47246,
                            0.46822,
                            0.45551,
                            0.40148,
                            0.35487,
                            0.31568,
                            0.28178,
                            0.25318,
                            0.22775,
                            0.20551,
                            0.18538,
                            0.16949,
                            0.15466,
                            0.14089,
                            0.12924,
                            0.11864,
                            0.10911,
                            0.10064,
                            0.09322,
                            0.08686,

                        ]
                        ws = [3.0,
                              3.5,
                              4.0,
                              4.5,
                              5.0,
                              5.5,
                              6.0,
                              6.5,
                              7.0,
                              7.5,
                              8.0,
                              8.5,
                              9.0,
                              9.5,
                              10.0,
                              10.5,
                              11.0,
                              11.4,
                              11.5,
                              12.0,
                              12.5,
                              13.0,
                              13.5,
                              14.0,
                              14.5,
                              15.0,
                              15.5,
                              16.0,
                              16.5,
                              17.0,
                              17.5,
                              18.0,
                              18.5,
                              19.0,
                              19.5,
                              20.0,

                              ]
                        globals()[uniqueID] = toUserVariable = SRT(uniqueID, diameter=126, hubHeigt=120,
                                                                   ws=ws,
                                                                   cp=NRELPower)  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfSRT += 1
                        self.createdSRTs.append(uniqueID)
                    elif reference == "DTU":
                        globals()[uniqueID] = toUserVariable = SRT(uniqueID, diameter=150, hubHeigt=150,
                                                                  )  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfSRT += 1
                        self.createdSRTs.append(uniqueID)
                    else:
                        raise Exception("Turbine type not supported")

            else:
                raise Exception(
                    "Name should be a string without spaces. The assignment should be done via the UID and not the variable name.")

            return toUserVariable

    def addTurbine(self,uniqueID,turbineType="SRT",diameter=float("NaN"),hubHeigt=float("NaN"),x_horizontal=float("NaN"),y_vertical=float("NaN"),ws=[],cp=[]): ##This function helps to create a wind turbine and keep internal (inside the class) track of its name. It is not a deep copy, rather a reference.

        """
        By default adds a single rotor turbine (SRT) to the related windfarm. Returns the created wind turbine with the given unique ID.
        The wind turbine would be callable via its unique name and via the assigned variable by user. Note that the referenced unique id is stored in library. Thus when calling the turbine via unique id, it should be prefixed by library name pywinda. See example below.

        :param uniqueID: [*req*] Unique ID of the wind turbine as string
        :param turbineType: [*opt*] Type of turbine as string: 'SRT' or 'MRT'
        :param diameter: [*opt*] Diameter of the turbine as float
        :param hubHeigt: [*opt*] Hub height as a float
        :param x_horizontal: [*opt*] Horizontal coordinate of the turbine as float
        :param y_vertical: [*opt*] Vertical coordinate of the the turbine as float

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> curslack=pw.windfarm("uID_Curslack3")
            >>> WT1=curslack.addTurbine('uID_WT14',turbineType='SRT',hubHeigt=120 )
            >>> WT2=curslack.addTurbine('uID_WT15',turbineType='SRT',x_horizontal=150,y_vertical=150)
            >>> WT3=curslack.addTurbine('uID_WT16',turbineType='MRT',hubHeigt=200,x_horizontal=300,y_vertical=300)
            >>> WT3.diameter=150 #Assiging WT3 diameter after creation.
            >>> print(WT3==pw.uID_WT16)
            True
            >>> print(WT3.diameter)
            150
            >>> WT4=curslack.addTurbine('uID_WT16')
            Traceback (most recent call last):
            Exception: A wind turbine witht the same uniqe ID globally exists. New turbine not added.
            >>> WT5=curslack.addTurbine('uID WT16')
            Traceback (most recent call last):
            Exception: Name should be a string without spaces. The assignment should be done via the UID and not the variable name.



        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """

        if uniqueID in self.createdSRTs: #Checks if the given unique Id already exists in the wind farm
            raise  Exception ("A wind turbine with the same unique ID in wind farm [ "+str(self.uID)+" ] already exists. New turbine not added.")
        else:
            if type(uniqueID) == str and len(uniqueID.split())==1:
                if uniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise  Exception("A wind turbine witht the same uniqe ID globally exists. New turbine not added.")
                else:
                    if turbineType=="SRT":
                        globals()[uniqueID] = toUserVariable = SRT(uniqueID,diameter=diameter,hubHeigt=hubHeigt,x_horizontal=x_horizontal,y_vertical=y_vertical,ws=ws,cp=cp)  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfSRT += 1
                        self.createdSRTs.append(uniqueID)
                    elif turbineType=="MRT":
                        globals()[uniqueID] = toUserVariable = MRT(uniqueID,diameter=diameter,hubHeigt=hubHeigt,x_horizontal=x_horizontal,y_vertical=y_vertical,ws=ws,cp=cp)  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfMRT += 1
                        self.createdMRTs.append(uniqueID)
                    else:
                        raise  Exception ("Turbine type not supported")

            else:
                    raise Exception ("Name should be a string without spaces. The assignment should be done via the UID and not the variable name.")

            return toUserVariable

    def assignEnvironment(self,envName):

        """
        Assigns an already created environment to the referenced wind farm. Parameters of the environment (e.g. temperature, pressure, wind regime etc.) can be assigned later.
        The environment would be callable via its unique name and the assigned variable by user. When using the unique Id, it should be prefixed witht he library name pywinda. See example.

        :param envName: [*req*] unique nvironment name

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> DanTysk=pw.windfarm("DanTysk2")
            >>> env=pw.environment('normal1')
            >>> print(env.info.keys()) #shows some of the conditions of the created environment
            dict_keys(['Wind directions', 'Sectors', 'Wind speeds', 'Pressure', 'Temperature', 'Wind probability', 'Scale parameter of wind distribution', 'Shape parameter of wind distribution'])
            >>> print(env.info['Pressure'])
            101325
            >>> DanTysk.assignEnvironment('normal1')
            >>> DanTysk.assignEnvironment('normal2')
            Traceback (most recent call last):
            Exception: The wind farm [DanTysk2] already has assigned environment [normal1]. New environment not added.
            >>> print(pw.normal1==env)
            True


        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """


        if self.farmEnvironment!=None: #Checks if the wind farm already have an associated environment
            raise Exception ("The wind farm ["+ str(self.uID)+"] already has assigned environment ["+str(self.farmEnvironment)+"]. New environment not added.")
        else:
            if type(envName) == str and len(envName.split())==1:
                if envName in environment.created_environments: #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    self.farmEnvironment=envName
                else:
                    raise Exception ("Environment doesn't exist. Please make sure you first create the environment and then assign it.")


                    # globals()[envName] = toUserVariable = environment(envName)  # environment is dynamicall created and referenced with the unique ID to the users assigned variable.
                    # self.farmEnvironment=envName


            else:
                    raise Exception ("Name should be a string without spaces. The assignment should be done via the UID and not the variable name.")

            # return toUserVariable #doesn't return any value, depricated

    def distances(self, assets=[]):#From this point there would be a global convention of naming the property which shares two turbines in a "from" to "to" convention. For example distanceWT1toWT2 means the distance from WT1 to WT2

        """
        Returns the data frame with all the distances between assets in the wind farm or between those given in the assets list.

        :param assets: [*opt*] Unique ID or object name of the assets

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> Curslack2 = pw.windfarm("Curslack_farm1")
            >>> WT1 = Curslack2.addTurbine("C_WT01", x_horizontal=480331, y_vertical=4925387)
            >>> WT2 = Curslack2.addTurbine("C_WT02", x_horizontal=480592, y_vertical=4925253)
            >>> WT3 = Curslack2.addTurbine("C_WT03", x_horizontal=480886, y_vertical=4925166)
            >>> WT4 = Curslack2.addTurbine("C_MWT04",x_horizontal=480573, y_vertical=4925712)
            >>> print(Curslack2.distances())
                Assets      C_WT01      C_WT02      C_WT03     C_MWT04
            0   C_WT01    0.000000  293.388821  597.382624  405.202419
            1   C_WT02  293.388821    0.000000  306.602348  459.393078
            2   C_WT03  597.382624  306.602348    0.000000  629.352842
            3  C_MWT04  405.202419  459.393078  629.352842    0.000000

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """
        if len(assets)==0: #The user should give the set of turbines here, if not the function will calculate and return all the distances between all the turbines in that wind farm.
            distancesDic={}
            distancesDic["Assets"]=self.assets

            for asset in self.assets:
                distancesDic[asset] = []
                for i in range(len(self.assets)):
                       deltax=globals()[asset].x_horizontal-globals()[self.assets[i]].x_horizontal
                       deltay=globals()[asset].y_vertical-globals()[self.assets[i]].y_vertical
                       distance=((deltax**2)+(deltay**2))**(0.5)
                       distancesDic[asset].append(distance)
            df=pd.DataFrame(distancesDic)
            return df

        else: #This part will work for the user's given set of turbines manually
            print("To be done for a given set of turbines' unique names")
            return "Under development"

    def coordinates(self, assets=[]):

        """
        Returns the data frame with all assets' x and y coordinates if the assets list is empty, otherwise only for the given set of assets.

        :param assets: [*opt*] Unique ID or object name of the assets

        :Example:

              >>> from PyWinda import pywinda as pw
              >>> Curslack = pw.windfarm("Curslack_farm01")
              >>> WT1 = Curslack.addTurbine("C_WT11", x_horizontal=480331, y_vertical=4925387)
              >>> WT2 = Curslack.addTurbine("C_WT2", x_horizontal=480592, y_vertical=4925253)
              >>> WT3 = Curslack.addTurbine("C_WT3", x_horizontal=480886, y_vertical=4925166)
              >>> WT4 = Curslack.addTurbine("C_MWT4",x_horizontal=480573, y_vertical=4925712)
              >>> print(Curslack.coordinates())
              Assets  x_coor   y_coor
              C_WT11  480331  4925387
              C_WT2   480592  4925253
              C_WT3   480886  4925166
              C_MWT4  480573  4925712

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

              """

        if len(assets) == 0:
            coordinatesDic={}
            coordinatesDic["Assets"]=["x_coor","y_coor"]
            for asset in self.assets:
                coordinatesDic[asset]=[globals()[asset].x_horizontal,globals()[asset].y_vertical]
            toReturn=pd.DataFrame(coordinatesDic)
            return toReturn.set_index('Assets').transpose()

        else:
            print("To be done for a given set of turbines' unique names")
            return "Under development"

    def run(self,wakeModel=None,randomWind=None):
        AEP = 0
        RunReport = {}
        if self.farmEnvironment==None:
            raise Exception ('The windfarm has no uniqe environment associated with it.')
        if len(self.assets)==0:
            raise Exception ('The wind farm has no turbine assigned to it.')
        else:
            if wakeModel==None and randomWind==None: #no information about the wake effects are considered thus calculating power without need of infomration about the turbine locations
                unique_env=globals()[self.farmEnvironment].info #the environemtn of the wind farm, running the info function here updates the list of all assets as well.
                if unique_env["Sectors"]!=None: #checks if the sectors are created
                    if len(unique_env["Sectors"])==len(unique_env["Wind probability"])==len(unique_env["Scale parameter of wind distribution"])==len(unique_env["Shape parameter of wind distribution"]): #checks if the wind conditions are declared correctly
                        for index,turbine in enumerate(self.allassets): #loops through all the available assets specifically only the SRTs and MRTs, pywinda currently doesn't support other assets like platforms and metmasts
                            statistics_dictionary = {}
                            sectors = []
                            directions = []
                            probab_any_wind = [] #defined foe each secotr
                            probab_specific_wind = []  #defined for every degree
                            total_probab = []
                            windspeeds = []
                            time_fraction = []
                            cp = []
                            energy = []
                            for ind,sectorname in enumerate(unique_env["Sectors"]):  # this all the sectors
                                probability_per_unit=unique_env["Wind probability"][ind]/len(unique_env["Sectors"][sectorname]) #divides further the probability assigned for one sector to all the degrees inside a sector.
                                afactor_persector=unique_env["Scale parameter of wind distribution"][ind]
                                kfactor_persector=unique_env["Shape parameter of wind distribution"][ind]
                                for index,unit in enumerate(unique_env["Sectors"][sectorname]):
                                    for indexx,windspeed in enumerate(unique_env['Wind speeds']):
                                        # maxsize=len(unique_env['Wind speeds'])-1
                                        # print(maxsize)
                                        sectors.append(sectorname)
                                        directions.append(unit) #unit is actually the degrees
                                        probab_any_wind.append(probability_per_unit)

                                        if indexx==0:
                                            probabperws=weib_cumulative(unique_env['Wind speeds'][indexx]+0.25,afactor_persector,kfactor_persector)-weib_cumulative(0,afactor_persector,kfactor_persector)
                                            probab_specific_wind.append(probabperws)
                                        else:
                                            probabperws=weib_cumulative(unique_env['Wind speeds'][indexx]+0.25,afactor_persector,kfactor_persector)-weib_cumulative(unique_env['Wind speeds'][indexx]-0.25,afactor_persector,kfactor_persector)
                                            probab_specific_wind.append(probabperws)

                                        total_probab_here = probability_per_unit*probabperws
                                        total_probab.append(total_probab_here)
                                        windspeeds.append(windspeed)
                                        time_fraction.append(total_probab_here*365*24*3600)
                                        cpLoop=globals()[str(turbine)].interp_cp[indexx]
                                        cp.append(cpLoop)
                                        energy.append(0.5*globals()[str(self.farmEnvironment)].info["Air Density [kg/m^3]"]*globals()[str(turbine)].area*windspeed**3*cpLoop*365*24*total_probab_here)

                            statistics_dictionary['Sectors'] = sectors
                            statistics_dictionary['Directions[degrees]']=directions
                            statistics_dictionary['Probability_of_any_windspeed']=probab_any_wind
                            statistics_dictionary['Probability_of_specific_windspeed']=probab_specific_wind
                            statistics_dictionary['Total_probability']=total_probab
                            statistics_dictionary['Wind_speeds[m/s]']=windspeeds
                            statistics_dictionary['Time_fraction[s]']=time_fraction
                            statistics_dictionary['CP']=cp
                            statistics_dictionary['Produced_energy[Wh]']=energy
                            print(np.sum(total_probab))

                            final_statistics = pd.DataFrame(statistics_dictionary)
                            RunReport[str(turbine)+'_statistics']=final_statistics
                            RunReport[str(turbine)+'_AEP[MWh]']=np.sum([energy])/1000000 #total AEP in MWh
                            AEP=AEP+np.sum([energy])/1000000
                        RunReport['Windfarm_AEP[MWh]']=AEP
                        return RunReport

                    else:
                        raise Exception ('The dimentions of wind conditions array does not match that of the introduced sectors')
                else:
                    raise Exception('The environment sectors are not declared. Use the function makeSectors() to implement the PyWinda default sectors definition.')

            if wakeModel==None and randomWind!=None: #no information about the wake effects are considered thus calculating power without need of infomration about the turbine locations
                rtg=default_rng()
                unique_env=globals()[self.farmEnvironment].info #the environemtn of the wind farm, running the info function here updates the list of all assets as well.
                bins_plan = [0] #0 is added from the begining to the bins
                for wsp in unique_env['Wind speeds']:
                    bins_plan.append(wsp + 0.25)
                bins_plan[-1] = unique_env['Wind speeds'][-1] #end of the bins_plan array is replaced back with the end of the possible wind speeds, size of the bins_plan is one more than the wind speeds
                if unique_env["Sectors"]!=None: #checks if the sectors are created
                    if len(unique_env["Sectors"])==len(unique_env["Wind probability"])==len(unique_env["Scale parameter of wind distribution"])==len(unique_env["Shape parameter of wind distribution"]): #checks if the wind conditions are declared correctly
                        for index,turbine in enumerate(self.allassets): #loops through all the available assets specifically only the SRTs and MRTs, pywinda currently doesn't support other assets like platforms and metmasts
                            statistics_dictionary = {}
                            sectors = []
                            directions = []
                            probab_any_wind = [] #defined foe each secotr
                            probab_specific_wind = []  #defined for every degree
                            total_probab = []
                            windspeeds = []
                            time_fraction = []
                            cp = []
                            energy = []
                            for ind,sectorname in enumerate(unique_env["Sectors"]):  # this all the sectors
                                probability_per_unit=unique_env["Wind probability"][ind]/len(unique_env["Sectors"][sectorname]) #divides further the probability assigned for one sector to all the degrees inside a sector.
                                afactor_persector=unique_env["Scale parameter of wind distribution"][ind]
                                kfactor_persector=unique_env["Shape parameter of wind distribution"][ind]
                                randomWinds=afactor_persector*rtg.weibull(kfactor_persector,randomWind) #creates the sample wind with a lot of numbers
                                all_probabilities,bins_ignored=np.histogram(randomWinds,bins=bins_plan,density=True)#splites the produced winds
                                all_probabilities=all_probabilities*0.5 #the probability density fucntion has a width of only 0.5 thus the area under one bar is calcualted here
                                # print(np.sum(all_probabilities))
                                # print()
                                for index,unit in enumerate(unique_env["Sectors"][sectorname]):
                                    for indexx,windspeed in enumerate(unique_env['Wind speeds']):
                                        sectors.append(sectorname)
                                        directions.append(unit) #unit is actually the degrees
                                        probab_any_wind.append(probability_per_unit)
                                        if indexx==0:
                                            probabperws = all_probabilities[indexx]
                                            probab_specific_wind.append(probabperws)
                                        else:
                                            probabperws = all_probabilities[indexx]
                                            probab_specific_wind.append(probabperws)
                                        total_probab_here = probability_per_unit*probabperws
                                        total_probab.append(total_probab_here)
                                        windspeeds.append(windspeed)
                                        time_fraction.append(total_probab_here*365*24*3600)
                                        cpLoop=globals()[str(turbine)].interp_cp[indexx]
                                        cp.append(cpLoop)
                                        energy.append(0.5*globals()[str(self.farmEnvironment)].info["Air Density [kg/m^3]"]*globals()[str(turbine)].area*windspeed**3*cpLoop*365*24*total_probab_here)

                            statistics_dictionary['Sectors'] = sectors
                            statistics_dictionary['Directions[degrees]']=directions
                            statistics_dictionary['Probability_of_any_windspeed']=probab_any_wind
                            statistics_dictionary['Probability_of_specific_windspeed']=probab_specific_wind
                            statistics_dictionary['Total_probability']=total_probab
                            statistics_dictionary['Wind_speeds[m/s]']=windspeeds
                            statistics_dictionary['Time_fraction[s]']=time_fraction
                            statistics_dictionary['CP']=cp
                            statistics_dictionary['Produced_energy[Wh]']=energy
                            # print(np.sum(total_probab))

                            final_statistics = pd.DataFrame(statistics_dictionary)
                            RunReport[str(turbine)+'_statistics']=final_statistics
                            RunReport[str(turbine)+'_AEP[MWh]']=np.sum([energy])/1000000 #total AEP in MWh
                            AEP=AEP+np.sum([energy])/1000000
                        RunReport['Windfarm_AEP[MWh]']=AEP
                        return RunReport

                    else:
                        raise Exception ('The dimentions of wind conditions array does not match that of the introduced sectors')
                else:
                    raise Exception('The environment sectors are not declared. Use the function makeSectors() to implement the PyWinda default sectors definition.')

            elif wakeModel=='Larsen':
                if self.__allDistances.empty:
                    self.__allDistances=self.distances() # checks if the allDistances data frame is already populated
class SRT:

    """
        Creates single rotor turbine (SRT) object and returns it with the given unique name.

        :param srtUniqueID: [*req*] Unique Id of the wind turbine as a string.
        :param diameter: [*opt*] diameter of the SRT.
        :param hubHeight: [*opt*] hub height of the SRT.
        :param x_horizontal: [*opt*] x coordinate of the SRT.
        :param y_vertical: [*opt*] y coordinate of the SRT.

        :Example:

            >>> WT1=SRT("TheWT1",diameter=150)
            >>> print(WT1.info)
                   Property                                              Value
            0   Unique Name                                             TheWT1
            1  x_horizontal                                                NaN
            2    y_vertical                                                NaN
            3      Diameter                                                150
            4    Hub height                                                NaN
            5          Area                                       17671.458676
            6    Windspeeds  [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, ...
            7            CP                                                 []

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    def __init__(self,srtUniqueID,diameter=float("NaN"),hubHeigt=float("NaN"),x_horizontal=float("NaN"),y_vertical=float("NaN"),ws=[],cp=[]):
        self.created_SRTs = []
        self.uID = srtUniqueID
        self.diameter=diameter
        self.hubHeight=hubHeigt
        self.x_horizontal=x_horizontal
        self.y_vertical=y_vertical
        self.area=0.25*np.pi*self.diameter**2
        self.lifeTime=None

        self.windspeeds=[i for i in np.arange(0,50.5,0.5)] #m/s
        self.interp_cp=[]
        if len(ws)==len(cp) and len(ws)!=0:
            for index,i in enumerate(self.windspeeds):
                self.interp_cp.append(np.interp(i, ws, cp, left=0, right=0))

        elif len(ws)!=len(cp):
            raise Exception ("The dimensions of windspeed and power coeficinet arrays should same.")


        if srtUniqueID in self.created_SRTs: #Checks if the SRT ID is already taken
            raise Exception ("The SRT unique ID [" + str(srtUniqueID) + "] is already taken.")
        else:
            if type(srtUniqueID) == str and len(srtUniqueID.split())==1:
                if srtUniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise Exception ("Another object with the same uniqe ID globally exists. New SRT not created.")
                else:
                    globals()[srtUniqueID] = self    #SRT is dynamicall created and referenced with the unique ID to the users assigned variable.
                    self.created_SRTs.append(srtUniqueID) #we append the created SRT to the list
                    self.uID=srtUniqueID
            else:
                raise Exception("Unique ID should be a string without spaces.")


    @property
    def info(self):

        """
        Returns a data frame containing information about the wind turbine.

        :param None:

        :Example:

            >>> from PyWinda import pywinda as pw
            >>> Curslack = pw.windfarm("Curslack_farm")
            >>> WT1 = Curslack.addTurbine("C_WT1", hubHeigt=120, diameter=120)
            >>> print(WT1.info)
                   Property                                              Value
            0   Unique Name                                              C_WT1
            1  x_horizontal                                                NaN
            2    y_vertical                                                NaN
            3      Diameter                                                120
            4    Hub height                                                120
            5          Area                                       11309.733553
            6    Windspeeds  [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, ...
            7            CP                                                 []


        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """

        infoDic={"Property":["Unique Name","x_horizontal","y_vertical", "Diameter", 'Hub height',"Area",'Windspeeds','CP'],"Value":[self.uID,self.x_horizontal,self.y_vertical, self.diameter, self.hubHeight,self.area,self.windspeeds,self.interp_cp]}
        return pd.DataFrame(infoDic)

class MRT(SRT):
    """
    Inherited from the class SRT, all the methods of a SRT is available for the MRT as well. The part is under development.
    """
    pass



if __name__=='__main__':
    print("Noting")
    cur=windfarm('Curslack')
    cur.addRefTurbine('WT1')
    cur.addRefTurbine('WT2')
    cur.addRefTurbine('WT3')

#---------------
    cur_env=environment('normal1')
    cur_env.makeSectors(n=12,sectorNames=[f'sector{i}' for i in range(12)])
    cur_env.windConditions(windProbability=[1/12 for i in range(12)],aParams=[5 for i in range(12)],kParams=[2.5 for i in range(12)])
#-----------
    cur.assignEnvironment('normal1')

    for i in range(100):
        report = cur.run(randomWind=1000)['WT1_AEP[MWh]']
        print(report)
    # print(report['Windfarm_AEP[MWh]'])

    # print(cur.lifetime)



