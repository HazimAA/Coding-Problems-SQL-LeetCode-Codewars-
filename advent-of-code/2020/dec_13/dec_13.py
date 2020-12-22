from itertools import count

with open("adventofcode_day13.txt") as file:
    timestamp = int(file.readline())
    bus_entries = file.readline().strip().split(',')
bus_timings = list(map(int, filter(lambda x: x != 'x' , bus_entries)))

best = float('inf')
potential_bus = None
for bus in bus_timings:
    potential_best = (timestamp-(timestamp%bus) + bus)
    if potential_best < best:
        best = potential_best
        potential_bus = bus
print("Bus:", potential_bus, "& Arrival Time:", best)
print("Part 1:", potential_bus * (best-timestamp))

buses = []
for index, timing in enumerate(bus_entries):
    if timing != 'x':
        timing = int(timing)
        buses.append((index,timing))

start,step = buses[0]
for t, timing in buses[1:]:
    for start in count(start, step):
        if (start + t) % timing == 0:
            break
    step = (step * timing)
print("My Part 2:", start)
