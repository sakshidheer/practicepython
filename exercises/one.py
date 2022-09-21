def print_mutliply_table(num, till):
    print("\n".join(["{} * {} = {}".format(num, x, num * x)
          for x in range(1, till+1)]))


print_mutliply_table(5, 20)
