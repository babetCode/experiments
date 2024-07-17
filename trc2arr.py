import numpy as np
import pandas as pd
import os
import sys
import math


##  function which takes openCap .trc marker data and outputs marker-->xyz no. dictionary, pandas arr

def trc_pd(trcfile):
    with open(trcfile) as fd:
        #read file into list
        lines = fd.readlines()
        #make dictionary
        markers = lines[3].rstrip().split('\t')[2::3]
        pos = lines[4].rstrip().split('\t')[2:]
        xyz = [pos[i:i+3] for i in range(0, len(pos), 3)]
        dct = dict(zip(markers, xyz))
        #make header for df
        header = 'Frame#'+'\t'+'Time'+'\t'+lines[4].lstrip()
        header = header.rstrip().split('\t')
        #make body of df
        lines = lines[6:]   
        lines2d = [l.rstrip().split('\t') for l in lines]
        df = pd.DataFrame(lines2d)
        #add header
        df.columns = header
        #returen tuple of dct, df
        return dct, df


##  function which takes openCap .trc marker data and outputs xyz no.-->array index dictionary, numpy arr

def trc_np(trcfile):
    with open(trcfile) as fd:
        #read file into list
        lines = fd.readlines()
        #make dictionary
        header = 'Frame'+'\t'+'Time'+'\t'+lines[4].lstrip()
        dct = dict(zip(header.rstrip().split('\t'), [i for i in range(len(header))]))
        #make array
        lines = lines[6:]
        lines2d = [l.rstrip().split('\t') for l in lines]
        linesfl = [[float(i) for i in l] for l in lines2d]
        arr = np.array(linesfl)
        return dct, arr

    
##  find midpoint of two points, returns [x,y,z] list
    
def midpt(a,b):
    return [(float(a[0])+float(b[0]))/2, (float(a[0])+float(b[0]))/2, (float(a[0])+float(b[0]))/2]


##  find the vector from a to b, returns [x,y,z] list

def vec(a,b):
    return[(float(b[0]))-float(a[0]), (float(b[1])-float(a[1])), (float(b[2])-float(a[2]))]


##  calculate pitch, yaw, roll from xyz pozitions of three points

def pyr(a,b,c):
    abm = midpt(a,b)
    v = vec(c, abm)
    y = math.atan(v[0]/v[2])
    x = math.atan(v[2]/v[1])
    z = math.atan(v[1]/v[0])
    return [x,y,z]
    

##  calculate distance between two points

def point_diff(a, b):
    dis = 0.0
    for i in range(3):
        dis += (float(b[i])-float(a[i]))**2
    distance = math.sqrt(dis)
    return distance

def main():
    
    #get header dictionary as dct and pandas data frame as df
    dct, df = trc_pd('PyLibWalk2.trc')

##    print(df.iloc[0,0])
##    print(df)

##    for x, y in df[['X4', 'Y4', 'Z4']]:
##        print(x, y)

##    for c, i in enumerate(df['Time']):
##        print(i)
##        if c > 10:
##            break
##
##    print(df[['Frame#', 'Time']])
##
    for a,b,c,d,e,f,g,h,i in zip(df['X62'], df['Y62'], df['Z62'], df['X63'], df['Y63'], df['Z63'], df['X60'], df['Y60'], df['Z60']):
        lat = [a,b,c]
        med = [d,e,f]
        elb = [g,h,i]
        print(pyr(lat,med,elb))
    print(pyr([0,0,0], [0,0,0], [9,9,9]))

##    for a,b,c in zip(df['X62'], df['Y62'], df['Z62']):
##        print(a)
##        #print('{}, {}'.format(i, j))

    #print(df[['X4', 'Y4', 'Z4']])


##    print(dct.keys())
##    print(df.loc[df['Frame#'] == '3'])
##    print(df.sort_values('Z4'))
    #for index, row in df.iterrows():
    #    print(row)

    
if __name__ == "__main__":
    main()
