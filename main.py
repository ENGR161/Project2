import math
import sys

ENERGY_OUT = 10000000    #j
GRAVITY = 9.81           #m/s^2
WATER_DENSITY = 1000     #kg/m^3
PHOUSE_COST = 100000     #$
GPIPE_COST = 500         #$/pipe

 
def best_turb(turbine_data):
    tl = 10000000000000
    for x ,y in turbine_data.items():
            turb_loss = ((1/x)-1)*ENERGY_OUT
            if tl > turb_loss:
                tl = turb_loss
                cost = turbine_data

def best_zone():
    zones = []
    zones.append(zone(100000,None,None,None,1))
    zones.append(zone(100000,None,None,None,1))
    zones.append(zone(100000,None,None,None,1))

#function that calculates the cost and efficiency of filling the reservoir
def filling(vel):
    pass

#function that calculates the cost and efficiency of draining the reservoir
def draining(vel):
    
    pass

#function that calculates the overall efficiency of the hydropump system
def efficiency():
    pass

#function that calculates the overall cost of the hydropump system
def cost():
    pass

class zone:
    def __init__(self,num,area,zone_height, ideal_wall_height, pipe_l,pipe_l_r,raise_cost,road_cost,site_prep,tot_cost = 0): 
        self.num = num
        self.idealArea = area
        self.z_height = zone_height
        self.pipe_length = pipe_l
        self.pipe_length_r = pipe_l_r
        self.raise_cost = raise_cost
        self.road_cost = road_cost
        self.site_prep = site_prep
        self.add_height = ideal_wall_height
        self.add_cost
        self.tot_cost
        self.final_tot_height
    
    #getters
    def getZoneNum(self):
        return self.num

    def getPipeLengthR(self):
        return self.pipe_length_r

    def getRaiseCost(self):
        return self.raise_cost

    def getRoadCost(self):
        return self.road_cost                                                                

    def getSitePrep(self):
        return self.site_prep

    def getAddCost(self):
        return self.add_cost
    
    def getIdealArea(self):
        return self.idealArea

    def getZoneHeight(self):
        return self.z_height

    def getPipeLength(self):
        return self.pipe_length

    def getAddHeight(self):
        return self.addHeight

    def getTotalCost(self):
        return self.tot_cost

    def getFinalTotalHeight(self):
        return self.final_tot_height 

    #setters

    def setTotalCost(self,tot_cost):
        self.tot_cost = tot_cost

    #calcs
    def addTotalCost(self,costs):
        for cost in costs:
<<<<<<< HEAD
            self.tot_cost += cost
=======
            self.tot_cost += cost 
>>>>>>> 4a10c229ad98355152d9ced77252044886e93943

    def addWallHeight(self,add):
        self.add_height += add

    def FinalTotalHeight(self):
        self.final_tot_height = self.z_height + self.idealWallHeight() + self.add_height

    def perimeter(self, area_new):
        if self.num == 1:
            return 4 * math.sqrt(area_new)
        elif self.num ==2:
            return (15/4) * math.sqrt((16*area_new)/math.sqrt(105))
        else:
            return ((math.sqrt(area_new / math.pi)) * 2 * math.pi)

    def idealMass(self):
        return ((4.32*10 ** 11) / (GRAVITY * (self.z_height + (.5 * self.add_height))))

    def idealVolume(self):
        return self.idealMass() / 1000

    def idealWallHeight(self):
        volume = self.idealVolume()
        wallHeight = volume / self.idealArea
        return wallHeight

    def idealResHeight(self):
        return self.idealWallHeight() + self.z_height

    def finalVolume(self,height_tot):
        return (4.32 * 10 ** 11) / (GRAVITY * height_tot * 1000)

    def finalArea(self,height_tot,height_wall):
        return self.finalVolume(height_tot) / height_wall

    def finalPipeLength(self):
        #uses final res height to get additional pipe length and adds onto length_base
        pass
        
    def flowRateDown(self):
        return (ENERGY_OUT) / (GRAVITY / self.idealResHeight() / 1000)

    def flowVelocityDown(self):
        return math.sqrt(2 * GRAVITY * self.idealResHeight())
    
    def flowVelocityUp(self, up_flow):
        return 1.273 * up_flow / self.pipeDiameter() ** 2  

    def pipeDiameter(self):
        velocity = self.flowVelocityDown()
        volume = self.flowRateDown()
        return math.sqrt(1.273 * volume / velocity) 
                                 
    
class pipe:
    def __init__(self, zone, pipe_l = 1, bends = []):
        self.friction
        self.diameter
        self.zone = zone
        self.length = pipe_l
        self.bends = bends
    
    def getFriction(self):
        return self.friction
    
    def getDiameter(self):
        return self.diameter
    
    def getLength(self):
        return self.length

    def getIsRaised(self):
        return self.is_raised

    def setFriction(self,friction):
        self.friction = friction

    def setDiameter(self,diameter):
        self.diameter = diameter

    def setLength(self,length):
        self.length = length

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setBends(self,bends):
        self.bends = bends

    def setZone(self,zone):
        self.zone = zone   

    def getBends(self):
        return self.bends
    
    def roundDiameter(self,diameter,pipe_id):
        for d in range(len(pipe_id)):
            if diameter <= pipe_id[d]:   
                return d
    
    def frictionHeight(self, pipe_data, pipe_id, vel, length):
        D = self.zone.pipeDiameter()
        V = vel
        L = length
        heights = [(x * (L * V ** 2) / (D * 2 * GRAVITY)) for x in pipe_data.keys()]
        
        indexD = self.roundDiameter(D,pipe_id)

        costs = []
        for x in range(0, len(heights)): #the jesus loop
            height_wall = heights[x]     #created by Hackerman himself
            height_wall += self.zone.getAddHeight()
            height_tot = height_wall / 2 + self.zone.getZoneHeight()
            area_new = self.zone.finalArea(height_tot, height_wall)
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
            cost += area_new * self.zone.site_prep
            cost += self.zone.getPipeLength() * pipe_data.get(pipe_data.keys()[x])[indexD]
            costs.append(cost)
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                lowest = cost
                index_low = costs.index(lowest)        

        final_h = heights[index_low]
        self.zone.addWallHeight(final_h)
        self.friction = final_h * (D * 2 * GRAVITY) / (L * V ** 2)
        self.zone.addTotalCost([lowest])
        
class bend:
    def __init__(self,zone, bend_num, bend_ang,bend_coe):
        self.bend_num = bend_num
        self.bend_ang = bend_ang
        self.bend_coe = bend_coe
        self.zone = zone

    def getBendNum(self):
        return self.bend_num

    def getBendAng(self):        
        return self.bend_ang

    def getBendCoe(self):
        return self.bend_coe       

    def bendLoss(self,vel,ang):
        for x in bend_data.keys():
            if ang == x:
                bcoe = bend_data[x][0]
        loss = bcoe * ((vel ** 2)/(2 * GRAVITY))
        self.zone.addWallHeight(loss) 
        return loss                 



class pump:
    def __init__(self,zone,pump_ef,pipe,elev):
        self.efficiency = pump_ef
        self.pipe = pipe
        self.elev = elev
        self.zone = zone
    
    def getEfficiency(self):
        return self.efficiency  
    
    def getPipe(self):
        return self.pipe  
    
    def getElev(self):
        return self.elev
        
    def pumpFlow(self,flow):
        D = self.zone.pipeDiameter()
        V = self.zone.flowVelocityUp(flow)
        EOut = EIn / n                
        flowUp = EOut / (GRAVITY / self.zone.add_height / 1000)
    


class turbine:
    def __init__(self,zone,turbine_ef,pipe,elev):
        self.efficiency = turbine_ef
        self.pipe = pipe
        self.elev = elev
        self.zone = zone

    def getEfficiency(self):
        return self.efficiency

    def getPipe(self):
        return self.pipe  

    def getElev(self):
        return self.elev

    def heightTurbine(self, n):
        EIn = (ENERGY_OUT) / n
        dE = EIn - (ENERGY_OUT)
        return (dE) / (GRAVITY * self.zone.mass())

    def roundEPR(self,epr,turbine_epr):
        for e in range(len(turbine_epr)):
            if epr <= pipe_id[e]:   
                return e

    def turbineCanal(self, turbine_data, turbine_epr):
        # heights = []
        # for x in turbine_data.keys():
        #     app = self.heightTurbine(x)
        #     heights.append(app) 
        heights = [self.heightTurbine(x) for x in turbine_data.keys()]

        costs = []

        for x in range(0, len(heights)): #the jesus loop 
            height_wall = heights[x]     
            height_wall += self.zone.getAddHeight() #changed to running total height
            height_tot = height_wall / 2 + self.zone.getZoneHeight()
            area_new = self.zone.finalArea(height_tot, height_wall)
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
            cost += area_new * self.zone.site_prep

            index = self.roundEPR(height_tot,turbine_epr)

            cost += self.zone.flowRateDown() * turbine_data.get(turbine_data.keys()[x])[index] #flow rate x unit cost at epr and height
            costs.append(cost)
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                lowest = cost
                index_low = costs.index(lowest)        

        final_h = heights[index_low]
        self.zone.addWallHeight(final_h)
        self.zone.addTotalCost([lowest])

if __name__ == '__main__':
    pump_data = {
        .8: [200,220,242,266,293,322,354,390,429,472,519],
        .83: [240,264,290,319,351,387,425,468,514,566,622],
        .86: [288,317,348,383,422,464,510,561,617,679,747],
        .89: [346,380,418,460,506,557,612,673,741,815,896],
        .92: [415,456,502,552,607,668,735,808,889,978,1076]
    }
    pump_epr = [20,30,40,50,60,70,80,90,100,110,120]

    pipe_data = {
        .05: [1.00,1.20,2.57,6.30,14,26,43,68,102,144,197,262,340],
        .03: [1.20,1.44,3.08,7.56,16,31,52,82,122,173,237,315,408],
        .02: [1.44,1.72,3.70,9.07,20,37,63,98,146,208,284,378,490],
        .01: [2.16,2.58,5.55,14,29,55,94,148,219,311,426,567,735],
        .005: [2.70,3.23,6.94,17,37,69,117,185,274,389,533,708,919],
        .002: [2.97,3.55,7.64,19,40,76,129,203,302,428,586,779,1011]
    }
    pipe_id = [.1,.25,.5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    bend_data = {
        20: [.1,1.00,1.49,4.93,14,32,62,107,169,252,359,492,654,849],
        30: [.15,1.05,1.57,5.17,15,34,65,112,178,265,377,516,687,892],
        45: [.2,1.10,1.64,5.43,16,36,69,118,187,278,396,542,721,936],
        60: [.22,1.16,1.73,5.70,16,38,72,124,196,292,415,569,757,983],
        75: [.27,1.22,1.81,5.99,17,39,76,130,206,307,436,598,795,1032],
        90: [.3,1.28,1.90,7,18,41,80,137,216,322,458,628,835,1084]
    }
    bend_id = [.1,.25,.5]

    turbine_data = {
        .83: [360,396,436,479,527,580,638,702,772,849,934],
        .86: [432,475,523,575,632,696,765,842,926,1019,1120],
        .89: [518,570,627,690,759,835,918,1010,1111,1222,1345],
        .92: [622,684,753,828,911,1002,1102,1212,1333,1467,1614],
        .94: [746,821,903,994,1093,1202,1322,1455,1600,1760,1936]
    }
    turbine_epr = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


    #zone 1 bends: 30 deg
    #zone 2 bends: 60 deg 