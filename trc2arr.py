import numpy as np
import pandas as pd
import os
import sys

#function which takes openCap .tc marker data and outputs tuple with (header dictionary, pandas arr)
def trc_pd(trcfile):
    with open(trcfile) as fd:
        #read file into list
        lines = fd.readlines()
        #make dictionary
        markers = lines[3].rstrip().split('\t')[2::3]
        pos = lines[4].rstrip().split('\t')[2:]
        xyz = [pos[i:i+3] for i in range(0, len(pos), 3)]
        dct = dict(zip(markers, xyz))
        #make array
        header = 'Frame'+'\t'+'Time'+'\t'+lines[4].lstrip()
        lines = [header]+lines[6:]  
        lines2d = [l.rstrip().split('\t') for l in lines]
        print(lines2d[0])
        df = pd.DataFrame(lines2d)
        return dct, df

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


def main():
    #get header dictionary as dct and pandas data frame as df
    dct, arr = trc_np('libraryWalk2.trc')

    for ct, i in enumerate(arr[:,:2]):
        if ct >=10:
            break
        print(ct, i*2)


   
if __name__ == "__main__":
    main()
