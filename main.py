import math

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
                tl = turbloss
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
    def __init__(self,area,zone_height,pipe_l,pipe_l_r,raise_cost,road_cost,site_prep,add_cost): 
        self.area = area
        self.z_height = zone_height
        self.pipe_length = pipe_l
        self.pipe_length_r = pipe_l_r
        self.raise_cost
        self.road_cost
        self.site_prep
        self.add_cost
    
    def getArea(self):
        return self.depth


    def setStuff....

    def mass(self):
        return ((4.32*10 ** 11) / (GRAVITY * self.z_height))

    def volume(self):
        return self.mass() / 1000

    def idealResHeight(self):
        volume = self.volume()
        wallHeight = volume / self.area
        return wallHeight + self.z_height

    def finalResHeight(self,add_height):
        return idealResHeight() + add_height

    def finalPipeLength(self):
        #uses final res height to get additional pipe length and adds onto length_base
        
    def flowRateDown(self):
        return (ENERGY_OUT) / (GRAVITY / self.idealResHeight() / 1000)

    def flowVelocityDown(self):
        return math.sqrt(2 * GRAVITY * self.idealResHeight())
    
    def flowVelocityUp(self, up_flow):
        return 1.273 * up_flow / self.pipeDiameter() ** 2  

    def pipeDiameter(self):
        velocity = self.flowVelocity()
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
        return self.pipe_fr
    
    def getDiameter(self):
        return self.diameter
    
    def getLength():
        return self.length

    def getIsRaised(self):
        return self.is_raised

    def setLength(self,length):
        self.length = length

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setBends(self,bends):
        self.bends = bends

    def setZone(self,zone):
        self.zone = zone   

    def getBends(self):
        return self.bends
    
    def frictionHeight(self, pipe_data, pipe_id, vel, length):
        D = self.zone.pipeDiameter()
        V = vel
        L = length
        heights = [(x * (L * V ** 2) / (D * 2 * GRAVITY)) for x in pipe_data.keys()]
        # for x in pipe_data.keys():
        #     effH =  x * (L * V ** 2) / (D * 2 * GRAVITY) 
        #     heights.append(effH)
        
        indexD = pipe_id.index(D)
        costs = [cost[indexD] for cost in pipe_data.values()]
        # for cost in pipe_data.values():                                                       
        #     costs.append(cost[indexD])

        compare = [(cost[x] * heights[x]) for x in range(0, len(heights))]
        # for x in range(0, len(heights))
        #     compare.append(cost[x] * heights[x])

        temp = compare.sort()

        final_h = heights[compare.index(temp[0])]

        self.friction = final_h * (D * 2 * GRAVITY) / (L * V ** 2)

        return final_h     
        
                                            
    
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

    def bendLoss(self,vel,ang):
        for x in bend_data.keys()
            if ang == x
            bcoe = bend_data[x][0]
        loss = bcoe * ((vel ** 2)/(2 * GRAVITY)) 
        return loss                 



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
        return 


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

    def heightTurbine(self, n):
        EIn = (ENERGY_OUT) / n
        dE = EIn - (ENERGY_OUT)
        return dE / (GRAVITY * self.zone.mass())
    
    def 



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
        20: [.1,[1.00,1.49,4.93,14,32,62,107,169,252,359,492,654,849]],
        30: [.15[1.05,1.57,5.17,15,34,65,112,178,265,377,516,687,892]],
        45: [.2[1.10,1.64,5.43,16,36,69,118,187,278,396,542,721,936]],
        60: [.22[1.16,1.73,5.70,16,38,72,124,196,292,415,569,757,983]],
        75: [.27[1.22,1.81,5.99,17,39,76,130,206,307,436,598,795,1032]],
        90: [.3[1.28,1.90,7,18,41,80,137,216,322,458,628,835,1084]]
    }
    bend_id = [.1,.25,.5]

    turbine_data = {
        .83: [360,396,436,479,527,580,638,702,772,849,934],
        .86: [432,475,523,575,632,696,765,842,926,1019,1120],
        .89: [518,570,627,690,759,835,918,1010,1111,1222,1345],
        .92: [622,684,753,828,911,1002,1102,1212,1333,1467,1614],
        .94: [746,821,903,994,1093,1202,1322,1455,1600,1760,1936]
    }
    turbine_epr = [.1,.25,.5]

    pipe_test = pipe()

    
    

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



'''  <chat>
- Cisco: scott found out the diameter for pipes is 0.5m for zone 1
- Zach: okay sounds good, do you want me to factor that in?

- Cisco: we can use this info to find the most ideal pipe for zone 1 
- Zach: okay so are we sure then that the radius is set?? so the only factor is the friction coef?

- Cisco: yes, we wil test it for each friction coefficient to find best efficiency v cost #
- Zach: okay, so are we gonna have loop that find both the best cost and efficiency at the 
same time (this would be kinds difficult), or should we go at it by finding the couple 
best efficiencies and then find a good cost based on those or what???

- Scott: this is scott, the cost is super easily calculated by hand, so we just need to find the efficiency based of
that one long equation-- so we find the efficiency and costs and divide them to get 
that comparison value we talked about. If you want to do it all in the program,
the costs are in that array that cisco typed in. Yeah, I think we can find the best ratio
for all the parts and then just use those? 
Yeah

- Zach: ohhhhhh, so we find the ratio for each and picj the best ratio then. Okay so
then we can do 2 separeate loops. one for efficiency and one for cost. and we'll put those into arrays,
and then create a new ratio array using those two. sound good?

- Scott: yeah, but hold on. just fyi, the values in that grid array that cisco typed in are
$ per m, so we need to mulitly all those cost values by the length, 67.08 m.
So the cost loop will just be those dict values * the length, and the 
efficiency loop will be that one long equation with v = 24.24, D = .5, l = 67.08,
and f is the variable changed (the dict keys)

If you really feel like it, you could generalize it so the v, d, and l are inputted
/ calculated for each zone so that we could easily check this for each zone. That
might be best. I can help code too rn if you need me too. Ok I'll work on the eff loop
- Zach: yeah I am kinda caught up here but hopefully i am leaving very soon

- Cisco: hey we found out our diameter thingy is wrong. its cisco again btw
- Zach: 

- Cisco: 
- Zach: 

- Cisco: 
- Zach: 

'''