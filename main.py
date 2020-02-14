#import serial
import lightcontrol
import time
#from random import randrange
import veh_det

state = [0,0,0,0]
vehicles = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
timeWeights = [0, 0, 0, 0]
j=0
ways = 4
maxlim = 120
while j<2:
    j=j+1  
    for i in range(0,ways):
         
        waydata=veh_det.getVehs()
        timeWeights[0] = waydata[0][0] + (waydata[0][1]*3) + waydata[0][2]
        timeWeights[1] = waydata[1][0] + (waydata[1][1]*3) + waydata[1][2]
        timeWeights[2] = waydata[2][0] + (waydata[2][1]*3) + waydata[2][2]
        timeWeights[3] = waydata[3][0] + (waydata[3][1]*3) + waydata[3][2]
        
        totveh = waydata[4]
        totwei = waydata[5]
        #[0]=veh_det.getVehs()
        #print("cars in image yo: " + str(cars[0]))
        #cars[0]=cars[1]+randrange(5)
        #vehicles[0]=veh_det.getVehs()
        #vehicles[1][3]=vehicles[1][3]+randrange(14)
        #vehicles[1][4]=vehicles[1][3]
        #vehicles[2][3]=vehicles[2][3]+randrange(12)
        #vehicles[2][4]=vehicles[2][3]
        #vehicles[3][3]=vehicles[3][3]+randrange(24)
        #vehicles[3][4]=vehicles[3][3]
        
        #totveh = vehicles[0][3] + vehicles[1][3] + vehicles[2][3] + vehicles[3][3]
        #totwei = vehicles[0][4] + vehicles[1][4] + vehicles[2][4] + vehicles[3][4]
        print("totveh = " + str(totveh))
        print("totwei = " + str(totwei))
        if(totwei < 30):
             maxlim = 30
        elif(totwei < 60):
             maxlim=60
        else:
             maxlim=120
        print("maxlim =" + str(maxlim))
        #timeWeights[0] = vehicles[0][4]
        #timeWeights[0] = 5    #CHANGE!!!!!!!
        #timeWeights[1] = vehicles[1][4]
        #timeWeights[2] = vehicles[2][4]
        #timeWeights[3] = vehicles[3][4]
        
        if(totveh > 0):
             print("timeweights : " + str(timeWeights))
             retime = lightcontrol.control(timeWeights, totwei, maxlim)
             #print(retime)
             state[i] = 2
             lightcontrol.light(state)
             time.sleep(retime[i])
             timeWeights[i]=timeWeights[i]-(retime[i]*totwei/maxlim)
             state[i] = 1
             lightcontrol.light(state)
             if retime[i] == 0:
                 time.sleep(0)
             else:
                 time.sleep(3)
             state[i] = 0
             lightcontrol.light(state)     
        else:
             state = [3, 3, 3, 3]
             lightcontrol.light(state)

        #retime = lightcontrol.control([randrange(5),randrange(5),randrange(5),randrange(5)])
      
