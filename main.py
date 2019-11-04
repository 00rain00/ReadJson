import json
import os
import matplotlib.pyplot as plt
import numpy as np
dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir,"HPMode_JayBot_GM_NewHighlightmcts_2019.11.04-16.26.44.json")
with open(file) as json_file:
    jfile= json.load(json_file)
    d2p=[]  #data to plot
    rounds = jfile["rounds"]
    i=0
    for round in rounds:
        temp = []
        for frame in round:
            currentFrame=frame["current_frame"]
            #remainingFrames=frame["remaining_frames"]
            #p1D2C=frame["p1DistanceToCenter"]
            p1Energy=frame["p1Energy"]
            p2Energy=frame["p2Energy"]
            p2StartAddEnergy=frame["p2StartAddEnergy"]
          #  p1StartAddEnergy = frame["p1StartAddEnergy"]
            p1hitAddEnergy=frame["p1hitAddEnergy"]
            p2hitAddEnergy=frame["p2hitAddEnergy"]
            p2guardAddEnergy=frame["p2guardAddEnergy"]
            p1guardAddEnergy=frame["p1guardAddEnergy"]
            p1giveEnergy=frame["p1giveEnergy"]
            p2giveEnergy=frame["p2giveEnergy"]
            difDistance=frame["difDistance"]
           # temp.append([currentFrame,p1Energy,p2Energy])
            hlScore= (difDistance+p2Energy+p1Energy)/3
            temp.append(([hlScore]))
        ntemp =np.array(temp)
        d2p.append(ntemp)
    for data in d2p:
        i=i+1
        k=np.kaiser(np.size(data,0),14)
        plt.xlabel("frame #")
        plt.ylabel("energy")
        #plt.plot(data[:,0],data[:,2],"-")
        temp =[]
        for j in range(k.size):
            t = data[j] * k[j]
            temp.append(t)
       # sm=np.array(data[j]*k[j] for j in range(k.size))
        sm = np.array(temp)
        plt.plot(sm,"-")
        plt.savefig("plot"+str(i))


