ENERGY_OUT = 120     #KWh
GRAVITY = 9.81       #m/s^2
WATER_DENSITY = 1000 #kg/m^3
PHOUSE_COST = 100000 #$
GPIPE_COST = 500     #$


import math


#function that calculates the cost and efficiency of filling the reservoir
def filling(vel):
    
#function that calculates the cost and efficiency of draining the reservoir
def draining(vel):

#function that calculates the overall efficiency of the hydropump system
def efficiency():

def best_pipe(pipe_data):
    pipes = []
    for f in pipe_data.keys():
        for d in f:
            pipes.append(pipe(f,d))

def best_zone():
    zones = []
    zones.append(zone(100000,None,None,None,1))
    zones.append(zone(100000,None,None,None,1))
    zones.append(zone(100000,None,None,None,1))


    

#function that calculates the overall cost of the hydropump system
def cost():

class zone:
    def __init__(self,zone_sa,pipes,pump,turbine,zone_depth): 
        self.depth = zone_depth
        self.elev = pump.getElev()
        self.sa = zone_sa
        self.pipes = pipes
        self.pump = pump
        self.turbine = turbine
    
    def getDepth(self):
        return self.depth

    def getElev(self):
        return self.elev

    def getSurfaceArea(self):
        return self.sa
    
    def getPipes(self):
        return self.pipes
    
    def getPump(self):
        return self.pump

    def getTurbine(self):
        return self.turbine
    



class pipe:
    def __init__(self,pipe_fr,pipe_d,pipe_l = 1,is_raised = False, bends = []):
        self.friction = pipe_fr
        self.diameter = pipe_d
        self.length = pipe_l
        self.is_raised = is_raised
        self.bends = bends
    
    def getFriction(self):
        return self.pipe_fr
    
    def getDiameter(self):
        return self.diameter
    
    def getLength():
        return self.length

    def getIsRaised(self):
        return self.is_raised

    def getBends(self):
        return self.bends

    def setLength(self,length):
        self.length = length

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setBends(self,bends):
        self.bends = bends
    
    def frictionLoss():


class bend:
    def __init__(self,bend_num, bend_ang,bend_coe):
        self.bend_num = bend_num
        self.bend_ang = bend_ang
        self.bend_coe = bend_coe

    def getDepth(self):
        return depth

    def getBendAng(self):        
        return bend_ang

    def getBendCoe(self):
        return bend_coe                           
          
        

class pump:
    def __init__(self,pump_ef,pipe,elev):
        self.efficiency = pump_ef
        self.pipe = pipe
        self.elev = elev
    
    def getEfficiency(self):
        return self.efficiency  
    
    def getPipe(self):
        return self.pipe  
    
    def getElev(self):
        return self.elev
        
    def pumpFlow(self,vel):
        return ((self.pipe.getDiameter() ** 2) * vel)/1.273 #from engineering toolbox


class turbine:
    def __init__(self,turbine_ef,pipe,elev):
        self.efficiency = turbine_ef
        self.pipe = pipe
        self.elev = elev

    def getEfficiency(self):
        return self.efficiency

    def getPipe(self):
        return self.pipe  

    def getElev(self):
        return self.elev

    def turbFlow(self,vel):
        return ((self.pipe.getDiameter() ** 2) * vel)/1.273 #from engineering toolbox
    



if __name__ == '__main__':
    pump_data = {
        .8: [200,220,242,266,293,322,354,390,429,472,519],
        .83: [240,264,290,319,351,387,425,468,514,566,622],
        .86: [288,317,348,383,422,464,510,561,617,679,747],
        .89: [346,380,418,460,506,557,612,673,741,815,896],
        .92: [415,456,502,552,607,668,735,808,889,978,1076]
    }
    pipe_data = {
        .05: [1.00,1.20,2.57,6.30,14,26,43,68,102,144,197,262,340],
        .03: [1.20,1.44,3.08,7.56,16,31,52,82,122,173,237,315,408],
        .02: [1.44,1.72,3.70,9.07,20,37,63,98,146,208,284,378,490],
        .01: [2.16,2.58,5.55,14,29,55,94,148,219,311,426,567,735],
        .005: [2.70,3.23,6.94,17,37,69,117,185,274,389,533,708,919],
        .002: [2.97,3.55,7.64,19,40,76,129,203,302,428,586,779,1011]
    }
    bend_data = {
        20: [.1,[1.00,1.49,4.93,14,32,62,107,169,252,359,492,654,849]],
        30: [.15[1.05,1.57,5.17,15,34,65,112,178,265,377,516,687,892]],
        45: [.2[1.10,1.64,5.43,16,36,69,118,187,278,396,542,721,936]],
        60: [.22[1.16,1.73,5.70,16,38,72,124,196,292,415,569,757,983]],
        75: [.27[1.22,1.81,5.99,17,39,76,130,206,307,436,598,795,1032]],
        90: [.3[1.28,1.90,7,18,41,80,137,216,322,458,628,835,1084]]
    }
    turbine_data = {
        .83: [360,396,436,479,527,580,638,702,772,849,934],
        .86: [432,475,523,575,632,696,765,842,926,1019,1120],
        .89: [518,570,627,690,759,835,918,1010,1111,1222,1345],
        .92: [622,684,753,828,911,1002,1102,1212,1333,1467,1614],
        .94: [746,821,903,994,1093,1202,1322,1455,1600,1760,1936]
    }

    best_pipe(pipe_data)
    


    '''
    pipe
    bend1
    bend2
    bend3
    bend4
    turbine
    pumphouse
    road
    site_prep
    perimeter_qall
    pipe_install_cost
    raised_pipe_cost
    other_costs
    '''