import random


dataset=[5,-1,19,2,21,0,-2,22] 
d1=random.sample(dataset, 2) 
for i in dataset: 
 c1=[] 
 c2=[] 
 for i in dataset: 
  if(abs(d1[0])-i<= abs(d1[1]-i)): 
   c1.append(i) 
 else: 
  c2.append(i) 
  sum=0 
 for i in c1: 
  sum=sum+i 
 d1[0]=sum/len(c1) 
 sum1=0 
 for i in c2: 
  sum1=sum1+i 
 d1[1]=sum/len(c2) 
 if(d1[1]==d1[0]): 
  break 
print("First Cluster is :",c1) 
print("Second Cluster is :",c2)