def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']
    progress = params['progress']
    speed = params['speed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track
        
    if is_crashed or is_offtrack or is_reversed:
        reward = 1e-3
        
        
    reward *= progress

    reward *= speed*0.4

    return float(reward)
