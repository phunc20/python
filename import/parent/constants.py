import numpy as np


n_allowed_steps = 100

forest_energy = np.mean(np.arange(5,20))
forest_energy = np.random.randint(5,20+1)
forest_energy = 20

width = 21
height = 9
n_px = width*height

max_energy = 50

terrain_ids = {
    "land": 0,
    "forest": 1,
    "trap": 2,
    "swamp": 3,
}

terrain_names = {value: key for key, value in terrain_ids.items()}

up = 2
down = 3
left = 0
right = 1
rest = 4
dig = 5

available_actions = {
    "up": '2',
    "down": '3',
    "left": '0',
    "right": '1',
    "rest": '4',
    "dig": '5',
}

actionStr2ndarray = {
    "up": np.array([0, -1]),
    "down": np.array([0, 1]),
    "left": np.array([-1, 0]),
    "right": np.array([1, 0]),
}

code2action = {value: key for key, value in available_actions.items()}

punishments = {
    "land": 1,
    "gold": 4,
    "trap": 10,
    "forest": 20,
    "swamp": 40,
}


maps = {
    1: [
      [450,-2,0,-2,150,-1,0,0,0,0,-1,-2,-2,-2,0,0,0,0,150,-2,350],
      [-2,-2,-2,-2,-1,0,-1,-1,-1,-1,-3,50,-2,-2,-2,-2,-3,-3,50,-2,-1],
      [-2,-2,200,-2,0,-2,0,-2,-3,-3,-2,0,-3,-2,-2,150,-3,-3,0,0,50],
      [0,-3,-3,-2,0,0,-1,0,550,-3,-2,0,0,0,-1,0,0,-1,-1,-1,-2],
      [-2,0,0,0,-1,0,-1,50,300,-3,-2,0,-3,0,0,0,-1,-3,-3,-2,-1],
      [-1,-3,-1,-3,0,-2,0,0,-2,-1,100,-3,0,-2,300,-3,0,-2,-3,-2,0],
      [-2,-3,-1,-3,-1,500,-1,-3,-2,-1,0,-1,0,-1,0,-1,0,-2,-3,-3,-1],
      [0,-3,-1,-3,0,-2,-3,-3,0,0,0,0,-2,0,-2,-3,-3,-3,-3,200,-1],
      [1200,-3,-1,-3,-1,-1,-2,-2,0,-1,150,-2,0,-2,0,0,-2,-3,-3,1500,50],
    ],
    2: [
      [550,-1,-1,-2,-2,-2,-2,150,0,0,0,-3,-2,400,-3,650,-2,-1,0,0,0],
      [350,-1,-1,-2,0,0,-2,-2,-2,-1,0,-3,-3,-2,300,-2,-1,650,-2,-1,0],
      [-1,-1,450,-2,0,0,0,0,0,0,0,0,0,-3,-3,-3,-1,-1,-3,0,0],
      [-1,-1,-2,-2,0,-3,-2,0,0,-3,-3,-3,0,0,0,0,0,0,-3,0,150],
      [0,0,-2,0,-3,-3,-3,0,-1,-2,400,-3,-3,0,-2,0,-1,0,-3,0,0],
      [0,200,-2,0,-3,250,-1,0,0,-1,-2,-3,-2,0,-1,300,-1,0,-3,-1,0],
      [-3,-3,-2,0,-3,-3,-3,0,0,0,0,-3,-3,-3,-2,-2,-2,0,-2,-2,0],
      [-1,-3,-2,0,0,-2,0,0,-3,-3,-3,-3,150,-3,0,0,0,0,-2,200,0],
      [800,-3,-2,-3,450,-2,0,-3,-3,200,-1,250,-1,-3,0,-1,-1,0,0,0,0],
    ],
    3: [
      [200,-2,-2,250,-2,0,-2,-1,0,-3,500,-3,-3,0,0,0,0,0,-3,450,-3],
      [-2,-2,-1,-2,-1,0,-3,200,-2,0,-3,0,150,0,-2,-1,0,0,0,-3,0],
      [-3,-2,-1,-3,-1,0,0,-3,-2,0,0,0,-1,-2,450,-2,0,-2,150,-2,0],
      [300,-3,-3,300,-2,-2,-2,-2,300,-2,-2,0,0,0,-2,0,-3,-3,-3,-2,0],
      [-3,-3,0,-3,-1,350,-1,0,-2,-2,350,-2,0,-3,0,0,-3,300,-3,-2,250],
      [-3,0,0,0,-1,-1,-1,-1,-3,0,-2,0,-3,400,-3,0,-3,-3,-3,0,0],
      [450,-3,0,0,0,0,-1,400,-3,0,0,0,-2,-3,-2,0,0,0,0,0,0],
      [-3,0,-1,0,-1,0,-3,-3,-3,0,-1,0,0,0,250,-3,-3,-3,-1,-2,-2],
      [0,0,-1,200,-1,-3,500,-3,0,-1,200,-1,0,0,-2,-2,-2,-1,400,-1,-2],
    ],
    4: [
      [0,-1,0,0,0,0,0,-3,0,-1,0,-1,-3,150,500,200,-1,0,-2,-1,0],
      [-3,500,-3,-2,350,-1,0,0,0,0,0,0,-1,-1,50,-1,0,0,-2,350,-3],
      [-1,-3,-2,0,-1,-2,0,-1,0,0,0,0,0,0,-2,-1,0,0,-2,-1,-3],
      [0,-3,0,0,0,0,-2,600,-3,0,0,-2,-2,0,-2,0,0,0,0,0,0],
      [0,0,0,0,-1,-1,0,-3,0,-1,400,-3,-2,0,0,0,-1,-2,-1,-1,-1],
      [-1,0,0,-1,-3,-3,-1,-1,0,0,-3,-2,0,0,0,0,-1,700,-1,-1,-3],
      [350,-2,-1,-3,-2,-3,-3,-1,0,-3,0,0,0,0,-3,0,-1,-1,-1,-3,200],
      [0,-1,-3,-2,250,-2,-3,-1,0,0,0,0,-2,0,0,0,0,-1,-3,300,0],
      [0,-3,-2,300,1000,-2,-3,-1,0,-1,0,-2,100,-2,-1,0,-1,-3,400,0,800],
    ],
    5: [
      [0,0,0,0,0,0,0,-2,0,0,0,0,-2,0,0,0,0,-1,-1,800,-1],
      [100,-1,-3,-2,0,0,-1,200,-1,-2,250,-2,-2,250,-1,0,0,-1,-2,-1,-2],
      [-1,700,-1,-3,150,-1,-1,-3,-3,-2,-2,-1,-3,-2,-1,0,0,-3,0,-1,0],
      [0,-1,-3,0,-1,0,-3,-3,-1,-3,-1,600,-1,-3,-2,-1,-3,500,-1,0,0],
      [0,-3,0,0,0,0,-2,-1,350,-1,50,-1,-3,50,0,0,0,-1,0,0,-2],
      [0,0,0,-3,250,-3,-3,-3,-1,500,450,-1,-3,0,-1,0,0,0,0,-2,100],
      [0,-3,0,0,-3,0,0,0,-3,-1,-1,-3,0,0,-2,300,-2,-1,0,0,-2],
      [0,-1,-3,-2,0,0,0,-1,0,-3,-3,-3,-1,-2,-2,-1,-2,0,-1,0,0],
      [-1,500,-1,-3,-2,0,-1,450,-1,0,0,-1,500,-1,-2,-1,-2,0,50,0,0],
    ],
}


agent_state = (
    "PLAYing",
    "out_of_MAP",
    "no_more_ENERGY",
    "INVALID_action",
    "no_more_GOLD",
    "no_more_STEP",
)


#agent_state_id2str = {
#    0: "PLAYing",
#    1: "out_of_MAP",
#    2: "no_more_ENERGY",
#    3: "INVALID_action",
#    4: "no_more_GOLD",
#    5: "no_more_STEP",
#}

agent_state_id2str = (
    "PLAYing",
    "out_of_MAP",
    "no_more_ENERGY",
    "INVALID_action",
    "no_more_GOLD",
    "no_more_STEP",
)

agent_state_str2id = { agent_state_id2str[i]: i for i in range(len(agent_state_id2str)) }

maps_ndarray = np.array([maps[i] for i in range(1,5+1)])


def gold_total(map_):
    if not isinstance(map_, np.ndarray):
        map_ = np.array(map_)
    return map_[map_ > 0].sum()