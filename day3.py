# Day 3 - 2:
import numpy as np
from itertools import cycle

SIDE_LEN = 101
SEARCH_VAL = 277678

move_order = ["right", "up", "left", "down"] 

dir = {                                                     
     "up": [-1, 0],                                       
     "left": [0, -1],                   
     "down": [1, 0],                   
     "right": [0, 1]
}   

def clean_field(side_size):
    field = np.zeros((side_size, side_size))
    mid_idx = int(side_size / 2)
    field[mid_idx, mid_idx] = 1
    return field, [mid_idx, mid_idx]

field, mid_idx = clean_field(SIDE_LEN)
steps = np.repeat(np.arange(1, SIDE_LEN ** 2), 2) 

def get_next_insert_idx(cur_idx, prev_move_order, total):
    step_idx = 0
    cumsum = np.cumsum(steps)
    cur_dir = next(prev_move_order)
    while True:
        #print "step idx {}".format(step_idx)
        #print "total: {}".format(total)
        if total < cumsum[step_idx]:
            index_offset = dir[cur_dir]
        # get next insert idxs
        else:
            cur_dir = next(prev_move_order)
            index_offset = dir[cur_dir]
            # print index_offset
            step_idx += 1
        total += 1 
        cur_idx = (cur_idx[0] + index_offset[0], cur_idx[1] + index_offset[1])
        #print "new_index {}".format(cur_idx)
        yield cur_idx


idx_gen = get_next_insert_idx(mid_idx, cycle(move_order), 0)

for i in np.arange(SIDE_LEN):
    in_id = next(idx_gen)
    window = field[in_id[0] - 1: in_id[0] + 2, in_id[1] - 1: in_id[1] + 2]
    field[in_id] = np.sum(window)


print field[np.unravel_index(np.argmin(np.abs(field - SEARCH_VAL)), field.shape)]

