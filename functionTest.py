from trc2arr import *


def main():
    
    #get np array
    dc, arr = trc_np('PyLibWalk2.trc')

    #print(arr[:,2:5])
    print(xyzcols([62, 63]))
    print(type(dc['X62']))

    for i in arr[:10, dc['X62']:dc['Z62']+1]:
        print(i)
    

if __name__ == "__main__":
    main()