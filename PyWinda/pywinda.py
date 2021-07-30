import numpy as np
import pandas as pd



# ///////////////////// miscellaneous functions
def cAngle(i):
   x=i % 360
   return x

def weib(x,A,k): #A is the scale and k is the shape factor
    return (k / A) * (x / A)**(k - 1) * np.exp(-(x / A)**k) #This function show the probabilty of occurence of a specific wind speed.

# ////////////////////




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class environment:
    """
       Creates the stand-alone environment with the given unique ID. Some generic conditions are added by default. See example below.

       :param uniqueID: [*req*] the given unique ID.

       :Example:

           >>> Env = environment("C_Env")
           >>> #Creates an environment without assigning it to any wind farm.
           >>> print(Env.conditions.keys())
           dict_keys(['Wind degrees', 'Wind speeds'])
           >>> print(Env.conditions['Wind degrees']) # doctest:+ELLIPSIS
           [0, 1, 2, 3, ...]
           >>> print(Env.conditions['Wind speeds']) # doctest:+ELLIPSIS
           [0.0, 0.5, 1.0, 1.5, 2.0, ...]

       \----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    created_environments=[]

    def __init__(self, uniqueID):
        self.uID = uniqueID
        environment.created_environments.append(uniqueID)
        self.__conditionsDic={}
        self.__conditionsDic["Wind degrees"]=[i for i in range(0,360)] #degrees
        self.__conditionsDic["Wind speeds"]=[i for i in np.arange(0,50.5,0.5)]#m/s
        self.windSectors=None

    @property
    def conditions(self):
        """
            Returns all the defined conditions of the environment.

           :param None:

           :Example:

               >>> dantysk=windFarm("DanTysk")
               >>> D_Env = dantysk.addEnvironment("D_Env")
               >>> print(D_Env.conditions.keys())
               dict_keys(['Wind degrees', 'Wind speeds'])
               >>> print(D_Env.conditions['Wind degrees'])
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
               >>> print(D_Env.conditions['Wind speeds'])
               [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0]

           \----------------------------------------------------------------------------------------------------------------------------------------------------------

           """
        return self.__conditionsDic

    def makeSectors(self,n=12,sectorNames=["N_0","NNE_30","NEN_60","E_90","ESE_120","SSE_150","S_180","SSW_210","WSW_240","W_270","WNW_300","NNW_330"]):#by default the function will divide the sector in 12 regions
        """
        Creates the given sectors to the related environment. Returns the result as a data frame.
        Divides the 360 degrees to given number of sectors. By default it divides to 12 sectors and assigns the 12 standard names for every sector e.g. N_0 starts from 346 degrees and ends at 15 degrees.

        :param n: [*opt*] the number of sectors.
        :param sectorNames: [*opt*] names of the sectors given by user or default names for n=12.

        :Example:
        
            >>> Env=environment("C_Env")
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
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





class windFarm:
    """
    Creates wind farm object with the given unique ID. Pywinda will also create an internal shallow copy of the same windfarm object.

    :param uniqueID: [*req*] Unique Id of the wind farm as a string.

    :Example:

        >>> windFarmNameByUser = windFarm("Curslack")
         >>> print(windFarmNameByUser==Curslack)
        True


    \-----------------------------------------------------------------------------------------------------------------------------------------------------------

    """

    created_windfarms=[]
    def __init__(self,uniqueID):
        if uniqueID in windFarm.created_windfarms: #Checks if the wind farm ID is already taken
            raise Exception ("The wind farm unique ID [" + str(uniqueID) + "] is already taken.")
        else:
            if type(uniqueID) == str and len(uniqueID.split())==1:
                if uniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    raise Exception ("Another object with the same uniqe ID globally exists. New wind farm not created.")
                else:
                    globals()[uniqueID] = self    #wind farm is dynamicall created and referenced with the unique ID to the users assigned variable.
                    windFarm.created_windfarms.append(uniqueID) #we append the created wind farm to the list
                    self.uID=uniqueID
            else:
                raise Exception("Unique ID should be a string without spaces.")

        self.createdSRTs=[] #This is the store dictionary. Stores the wind turbine reference names created in a particular wind farm
        self.createdMRTs=[]
        self.farmEnvironment=None #A wind farm will have only one environment
        self.__numOfSRT=len(self.createdSRTs)
        self.__numOfMRT=len(self.createdMRTs)
        self.__allDistances=pd.DataFrame()












    @property #This helps to protect the info from direct changes by user
    def info(self):
        """
        Returns a data frame containing all the information about the wind farm.

        :param None:

        :Example:

            >>> #DanTysk=windFarm("USEr")
            >>> #print(DanTysk.info)
                     Property                  Value
            0       Unique ID                DanTysk
            1    Created SRTs  [D_WT1, D_WT2, D_WT3]
            2    Created MRTs               [D_MWT4]
            3  Number of SRTs                      3
            4  Number of MRTs                      1

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """


        statistics={"Property":["Unique ID","Created SRTs", "Created MRTs","Number of SRTs","Number of MRTs"],
                    "Value":[self.uID,self.createdSRTs,self.createdMRTs,self.__numOfSRT,self.__numOfMRT]}
        return pd.DataFrame(statistics)
    @property
    def assets(self):
        """
        Returns all the unique IDs of all the assets (e.g. single rotor turbines, multirotor tubines, met masts, etc.) in the wind farm.

        :param None:

        :Example:

            >>> #DanTysk.assets
            ['D_WT1', 'D_WT2', 'D_WT3', 'D_MWT4']

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """
        self.allassets=self.createdSRTs+self.createdMRTs#keeps the record of all assets in the wind farm
        return self.allassets



    def addTurbine(self,uniqueID,turbineType="SRT",diameter=float("NaN"),hubHeigt=float("NaN"),x_horizontal=float("NaN"),y_vertical=float("NaN")): ##This function helps to create a wind turbine and keep internal (inside the class) track of its name. It is not a deep copy, rather a reference.
        """
        By default adds a single rotor turbine (SRT) to the related windfarm. Returns the created wind turbine with the given unique ID.
        The wind turbine would be callable via its unique name and via the assigned variable by user. Note that the referenced unique id is temporarly stored in library. Thus when calling the turbine via unique id, it should be prefixed by library name pywinda. See example below.

        :param uniqueID: [*req*] Unique ID of the wind turbine as string
        :param turbineType: [*opt*] Type of turbine as string: 'SRT' or 'MRT'
        :param diameter: [*opt*] Diameter of the turbine as float
        :param hubHeigt: [*opt*] Hub height as a float
        :param x_horizontal: [*opt*] Horizontal coordinate of the turbine as float
        :param y_vertical: [*opt*] Vertical coordinate of the the turbine as float

        :Example:

            >>> #DanTysk=windFarm("TheDanTysk")
            >>> #WT1=DanTysk.addTurbine("D_WT1")
            >>> #WT2=DanTysk.addTurbine("D_WT2",diameter=120)
            >>> #WT3=DanTysk.addTurbine("D_WT3",x_horizontal=580592,y_vertical=5925253)
            >>> #WT3.diameter=150 #Assiging WT3 diameter after creation.
            >>> #print(WT1==D_WT1)
            True

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """

        if uniqueID in self.createdSRTs: #Checks if the given unique Id already exists in the wind farm
            print("A wind turbine with the same unique ID in wind farm [",str(self.uID), "] already exists. New turbine not added.")
        else:
            if type(uniqueID) == str and len(uniqueID.split())==1:
                if uniqueID in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    print("A wind turbine witht the same uniqe ID globally exists. New turbine not added.")
                else:
                    if turbineType=="SRT":
                        globals()[uniqueID] = toUserVariable = SRT(uniqueID,diameter=diameter,hubHeigt=hubHeigt,x_horizontal=x_horizontal,y_vertical=y_vertical)  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfSRT += 1
                        self.createdSRTs.append(uniqueID)
                    elif turbineType=="MRT":
                        globals()[uniqueID] = toUserVariable = MRT(uniqueID,diameter=diameter,hubHeigt=hubHeigt,x_horizontal=x_horizontal,y_vertical=y_vertical)  # windfarm class is dynamicall created and referenced with the unique ID to the users assigned variable.
                        self.__numOfMRT += 1
                        self.createdMRTs.append(uniqueID)
                    else:
                        print("Turbine type not supported")

            else:
                    print("Name should be a string without spaces.")

            return toUserVariable
    def addEnvironment(self,envName):
        """
        Creates environment for the referenced wind farm. Parameters of the environment (e.g. temperature, pressure, wind regime etc.) can be assigned later.
        The environment would be callable via its unique name and the assigned variable by user. When using the unique Id, it should be prefixed witht he library name pywinda. See example.

        :param envName: [*req*] Environment name

        :Example:

            # >>> DanTysk=windFarm("DanTysk")


        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """




        if self.farmEnvironment!=None: #Checks if the wind farm already have an associated environment
            print("The wind farm [", str(self.uID), "] already has assigned environment [",str(self.farmEnvironment),"]. New environment not added.")
        else:
            if type(envName) == str and len(envName.split())==1:
                if envName in globals().keys(): #Checks if the given unique Id is not in conflict with user's already assigned variables.
                    print("An environment with the same uniqe ID globally exists. New environment not added.")
                else:
                    globals()[envName] = toUserVariable = environment(envName)  # environment is dynamicall created and referenced with the unique ID to the users assigned variable.
                    self.farmEnvironment=envName


            else:
                    print("Name should be a string without spaces.")

            return toUserVariable
    def distances(self, assets=[]):#From this point there would be a global convention of naming the property which shares two turbines in a "from" to "to" convention. For example distanceWT1toWT2 means the distance from WT1 to WT2
        """
        Returns the data frame with all the distances between assets in the wind farm or between those given in the assets list.

        :param assets: [*opt*] Unique ID or object name of the assets

        :Example:

            >>> #Curslack = windFarm("Curslack_farm")
            >>> #WT1 = Curslack.addTurbine("C_WT1", x_horizontal=480331, y_vertical=4925387)
            >>> #WT2 = Curslack.addTurbine("C_WT2", x_horizontal=480592, y_vertical=4925253)
            >>> #WT3 = Curslack.addTurbine("C_WT3", x_horizontal=480886, y_vertical=4925166)
            >>> #WT4 = Curslack.addTurbine("C_MWT4",x_horizontal=480573, y_vertical=4925712)
            >>> #print(Curslack.distances())
                   Assets       C_WT1       C_WT2       C_WT3      C_MWT4      C_MWT5
                0   C_WT1    0.000000  293.388821  597.382624  405.202419  551.515186
                1   C_WT2  293.388821    0.000000  306.602348  459.393078  421.808013
                2   C_WT3  597.382624  306.602348    0.000000  629.352842  428.164688
                3  C_MWT4  405.202419  459.393078  629.352842    0.000000  295.465734
                4  C_MWT5  551.515186  421.808013  428.164688  295.465734    0.000000

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

              >>> #Curslack = windFarm("Curslack_farm")
              >>> #WT1 = Curslack.addTurbine("C_WT1", x_horizontal=480331, y_vertical=4925387)
              >>> #WT2 = Curslack.addTurbine("C_WT2", x_horizontal=480592, y_vertical=4925253)
              >>> #WT3 = Curslack.addTurbine("C_WT3", x_horizontal=480886, y_vertical=4925166)
              >>> #WT4 = Curslack.addTurbine("C_MWT4",x_horizontal=480573, y_vertical=4925712)
              >>> #print(Curslack.coordinates())
                    Assets  x_coor   y_coor
                    C_WT1   480331  4925387
                    C_WT2   480592  4925253
                    C_WT3   480886  4925166
                    C_MWT4  480573  4925712
                    C_MWT5  480843  4925592

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

class SRT:
    """
        Creates a single rotor turbine (SRT) object with the given unique name.

        :param srtUniqueID: [*req*] Unique Id of the wind farm as a string.
        :param diameter: [*opt*] diameter of the SRT.
        :param hubHeight: [*opt*] hub height of the SRT.
        :param x_horizontal: [*opt*] x coordinate of the SRT.
        :param y_vertical: [*opt*] y coordinate of the SRT.

        :Example:

            >>> WT1=SRT("TheWT1",diameter=150)
            >>> print(WT1.info)
                  Property    Value
            0  Unique Name   TheWT1
            1     Diameter      150
            2         Area  17671.5

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    created_SRTs=[]
    def __init__(self,srtUniqueID,diameter=float("NaN"),hubHeigt=float("NaN"),x_horizontal=float("NaN"),y_vertical=float("NaN")):
        SRT.created_SRTs.append(srtUniqueID)
        self.uID = srtUniqueID
        self.diameter=diameter
        self.hubHeight=hubHeigt
        self.x_horizontal=x_horizontal
        self.y_vertical=y_vertical
        self.area=0.25*np.pi*self.diameter**2
        self.lifeTime=None

    @property
    def info(self):
        """
        Returns a data frame containing information about the wind turbine.

        :param None:

        :Example:

            >>> Curslack = windFarm("Curslack_farm")
            >>> WT1 = Curslack.addTurbine("C_WT1", hubHeigt=120, diameter=120)
            >>> print(WT1.info)
                  Property    Value
            0  Unique Name    C_WT1
            1     Diameter      120
            2         Area  11309.7

        \-----------------------------------------------------------------------------------------------------------------------------------------------------------

        """

        infoDic={"Property":["Unique Name", "Diameter", "Area"],"Value":[self.uID, self.diameter, self.area]}
        return pd.DataFrame(infoDic)


class MRT(SRT):
    """
    Under development
    """
    pass



if __name__=='__main__': ##This section is made for tests. A more comprehensive test strategy will be developed later. Here the test can only check for syntax error, but to ensure script gives true resutls test mechanism should be developed.
    print("Notin")
    windFarmNameByUser = windFarm("Curslack")
    print(windFarmNameByUser==Curslack)


