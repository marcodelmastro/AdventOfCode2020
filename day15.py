#!/usr/bin/env python3

def MemoryGameFast(inputn,turns,doPrint=False):
    mem = {}
    lastspoken = -1
    spoken = -1

    if doPrint:
        print("---------------------------------------------------")
        print("Turns\t\t Memory size\t Last spoken number")
        print("---------------------------------------------------")

    for t in range(turns):
        
        if(t%1000000 == 0 and t!=0 and doPrint):
            print(t,"\t",len(mem.keys()),"\t",lastspoken)
        
        if t<len(inputn):
            spoken = inputn[t]
            mem[spoken] = [t]
        else:
            if lastspoken not in mem.keys(): # never spoken before
                spoken = 0
            else:
                if len(mem[lastspoken])==1: # only spoken once
                    spoken = 0
                else: # spoken more then once
                    lastspi = mem[lastspoken]
                    spoken = lastspi[1]-lastspi[0]

        if spoken in mem.keys():
            last = mem[spoken][-1]
            mem[spoken] = [last,t]
        else:
            mem[spoken] = [t]
        lastspoken = spoken

    if doPrint:
        print("---------------------------------------------------")
        print("*** Result =",lastspoken)
        print("---------------------------------------------------")
    
    return lastspoken

def main():
    from timeit import default_timer as timer
    part1 = MemoryGameFast([13,16,0,12,15,1],2020)
    print("Part 1 Result =",part1)
    print("Running Part 2...")
    start = timer()
    part2 = MemoryGameFast([13,16,0,12,15,1],30000000)
    stop = timer() 
    print("Part 2 Result =",part2)
    print("Time elapsed =", int(stop - start), "s")

if __name__ == "__main__":
    main()
