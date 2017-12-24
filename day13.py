import numpy as np
import re

# depth: range

# read data
# depth: range
reg = re.compile("(\d+): (\d+)")

init_str = """0: 3
1: 2
2: 4
4: 4
6: 5
8: 6
10: 8
12: 8
14: 6
16: 6
18: 8
20: 8
22: 6
24: 12
26: 9
28: 12
30: 8
32: 14
34: 12
36: 8
38: 14
40: 12
42: 12
44: 12
46: 14
48: 12
50: 14
52: 12
54: 10
56: 14
58: 12
60: 14
62: 14
66: 10
68: 14
74: 14
76: 12
78: 14
80: 20
86: 18
92: 14
94: 20
96: 18
98: 17""".split("\n")

#init_str = """0: 3
#1: 2
#4: 4
#6: 4""".split("\n")

steps = int(init_str[-1].split(":")[0]) + 1

depths = np.zeros(steps, dtype=bool)
ranges = np.zeros(steps, dtype=np.int)

# assign depths and ranges
for cur in init_str:
    cur_idx, cur_range = reg.findall(cur)[0]
    depths[int(cur_idx)] = True
    ranges[int(cur_idx)] = int(cur_range)


def move_sensor(sensor_pos, move_down, ranges):
    #print "sensor_pos: {}".format(sensor_pos)

    sensor_pos[move_down] += 1
    sensor_pos[~move_down] -= 1

    move_down[sensor_pos == ranges - 1] = False
    move_down[sensor_pos == 0] = True



def reset(init_str):

    sensor_pos = np.zeros(steps, dtype=np.int)

    # move through firewall
    move_down = np.ones(steps, dtype=bool)

    return sensor_pos, move_down

def run_through(sensor_pos, ranges, move_down):
    caught_at = []
    for i in np.arange(steps, dtype=np.int):

        # check if caught
        caught = sensor_pos[i] == 0
        if caught:
            caught_at.append(i)

        # move sensor
        move_sensor(sensor_pos, move_down, ranges)


    trip_severity = np.dot(np.array(caught_at), ranges[caught_at])
    #print "TRIP SEVERITY: {}".format(trip_severity)
    return int(trip_severity)


# part 1
sensor_pos, move_down = reset(init_str)
print "13-1: {}".format(run_through(sensor_pos, ranges, move_down))


# part 2

delay = 0
while True:
    sensor_pos, move_down = reset(init_str)

    for _ in range(delay):
        move_sensor(sensor_pos, move_down, ranges)
    
    if sensor_pos[0] == 0:
        delay += 1
        continue        

    trip_severity = run_through(sensor_pos, ranges, move_down)

    if trip_severity == 0:
        print "finished for delay: {}".format(delay)
        break
    delay += 1
