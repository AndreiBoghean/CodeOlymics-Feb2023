exec("stages = " + input("stages?\n"))

"""
stages = [
    [1,3,2,4,1],
    [3,1,2,4,3],
    [2,3,4,1,2],
    [2,1,4,3,1],
    [4,1,2,3,4]
]
"""

"""
stages = [
    [1,3,2,4,2],
    [3,4,2,1,1],
    [3,3,3,1,3],
    [2,1,4,2,4],
    [4,1,2,3,3]
]
"""

stages_actions = [
    [
        lambda stage, stage_buttons: 1,
        lambda stage, stage_buttons: 1,
        lambda stage, stage_buttons: 2,
        lambda stage, stage_buttons: 3
    ],
    [
        lambda stage, stage_buttons: stage.index(4),
        lambda stage, stage_buttons: stage_buttons[0],
        lambda stage, stage_buttons: 0,
        lambda stage, stage_buttons: stage_buttons[0]
    ],
    [
        lambda stage, stage_buttons: stage.index(stages[1][stage_buttons[1]]),
        lambda stage, stage_buttons: stage.index(stages[0][stage_buttons[0]]),
        lambda stage, stage_buttons: 2,
        lambda stage, stage_buttons: stage.index(4)
    ],
    [
        lambda stage, stage_buttons: stage_buttons[0],
        lambda stage, stage_buttons: 0,
        lambda stage, stage_buttons: stage_buttons[1],
        lambda stage, stage_buttons: stage_buttons[1]
    ],
    [
        lambda stage, stage_buttons: stage_buttons[0],
        lambda stage, stage_buttons: stage_buttons[1],
        lambda stage, stage_buttons: stage_buttons[2],
        lambda stage, stage_buttons: stage_buttons[3]
    ]
]

chosen_buttons = [None]*len(stages)
for i, stage in enumerate(stages):
    chosen_buttons[i] = stages_actions[i][stage[-1]-1](stage, chosen_buttons)

print("the pin for today is: ")
for i, button in enumerate(chosen_buttons):
    #print(f"the button in stage {i} at index {button} is {stages[i][button]}")
    print(stages[i][button], end="")
print()
