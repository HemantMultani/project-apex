import gc

class Node:
    pass

gc.collect()

print("Initial:", gc.get_count())

objs = []
for _ in range(1000):
    objs.append(Node())

print("After allocations:", gc.get_count())

gc.collect()
print("After manual collect:", gc.get_count())