from trc2arr import *


def main():
    
    #get np array
    dc, arr = trc_np('PyLibWalk2.trc')

    #print(arr[:,2:5])

    i, j, k = xyzcols(arr, dc, ['X60', 'X63', 'X62'])

    for q, r, s in zip(i,j,k):
        print(pyr(q,r,s))
        print('BREAK')
    

    llwrist = arr[:20, dc['X62']:dc['Z62']+1]

    lmwrist = arr[:20, dc['X63']:dc['Z63']+1]


    

if __name__ == "__main__":
    main()