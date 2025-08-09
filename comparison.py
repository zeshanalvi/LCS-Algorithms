import string, time, numpy as np, pandas as pd
from MLCS1992 import mlcs1992
from MLCS2011 import generateD_MLCS2011, lcs_back
from RAA2005 import RAA_2005
from RRDPLCS import generateD_IALCS
from TA1997 import TA_1997
from TBA import TBA
from data_generation import prep


d = 2  # Number of sequences
lenE=4
m = 5  # Minimum sequence length
n = 50  # Maximum sequence length
E=['A', 'C', 'G', 'T']
Sigma=E
iterations=10

results=np.zeros((d*lenE*n,6),np.float64)

print(E,len(E))

ds=[2,4,8,12,16,20,30,40,50,60,70,80,90,100]
Es=[4,10,100]
ns=[5,10,20,30,40,50,60,70,80,90,100]

for j,d in enumerate(ds):
    for k,lenE in enumerate(Es):
        for l,n in enumerate(ns):
            print("D:",d,"\tE:",lenE,"\tn:",n)
            #times=[0,0,0,0,0,0,0,0,0,0]
            for i in range(iterations):
                sequences,Sigma=prep(d,lenE,n,n,E)
                #print(d,lenE,m,n)
                #print("Sequences Generated")

                start=time.time()
                D=generateD_MLCS2011(sequences,Sigma)
                #print(len(D))
                #print("D final\t",D)
                lcs0=''.join(lcs_back(D,sequences))
                #times[0]+=(time.time()-start)
                results[j*len(Es)+k*len(ns)+l,0]+=(time.time()-start)
                #print("MLCS2011",len(lcs0))

                start=time.time()
                D=generateD_IALCS(sequences,Sigma)
                #print("D final\t",D)
                lcs1=''.join(lcs_back(D,sequences))
                results[j*len(Es)+k*len(ns)+l,1]+=(time.time()-start)
                #print("IALCS2024",len(lcs1))

                start=time.time()
                lcs2=TA_1997(sequences)
                #times[2]+=(time.time()-start)
                results[j*len(Es)+k*len(ns)+l,2]+=(time.time()-start)
                #print("TA1997",lcs2)

                start=time.time()
                #lcs3=DP_1992(sequences[0],sequences[1])
                if((d<=4 and n<=50) or (d<=8 and n<=30) or (d<=16 and n<=20)):
                    lcs3=mlcs1992(sequences)
                    results[j*len(Es)+k*len(ns)+l,3]+=(time.time()-start)
                else:
                    results[j*len(Es)+k*len(ns)+l,3]=10000000
                #print("MLCS1992")

                start=time.time()
                lcs4=TBA(sequences[0],sequences[1])
                results[j*len(Es)+k*len(ns)+l,4]+=(time.time()-start)
                #print("TBA",lcs4)

                start=time.time()
                lcs5=RAA_2005(sequences,Sigma)
                results[j*len(Es)+k*len(ns)+l,5]+=(time.time()-start)
                #print("RAA2005",len(lcs5))


                #print("MLCS2011 is\t",len(lcs0),lcs0)
                #print("IALCS is\t",len(lcs1),lcs1)
                #print("TA_1997 is\t",lcs2)
                #print("mlcs1992 is\t",lcs3)
                #print("TBA is\t",lcs4)
                #print("RAA_2005 is\t",lcs5)
            #print("D:",d,"\tE:",lenE,"\tn:",n)
            print(results[j*len(Es)+k*len(ns)+l,:])
            
            #print("MLSA-2011\t",times[0],"\tseconds")
            #print("IALCS-2024\t",times[1],"\tseconds")
            #print("TA-1997\t",times[2],"\tseconds")
            #print("DP-1992\t",times[3],"\tseconds")
            #print("TBA-Pair-2011\t",times[4],"\tseconds")
            #print("RAA-Pairwise-2005\t",times[5],"\tseconds")
        pd.DataFrame(results).to_csv("results"+str(d)+"_"+str(k)+".csv")
    pd.DataFrame(results).to_csv("results"+str(d)+".csv")

pd.DataFrame(results).to_csv("results.csv")
