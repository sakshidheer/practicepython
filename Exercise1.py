def printMutliplyTable(num, till):
    print("\n".join(["{} * {} = {}".format(num, x, num * x)
          for x in range(1, till+1)]))


printMutliplyTable(5, 20)
