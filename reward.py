def reward_function(params):
    # Get relevant data from the environment
    progress = params['progress']
    steps = params['steps']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    
    # Set parameters for target time and laps
    target_time_per_lap = 60  # 1 minute per lap
    target_laps = 3
    
    # Calculate the completion time per lap
    completion_time_per_lap = steps / float(target_time_per_lap)
    
    # Reward for staying close to the centerline
    distance_from_center = params['distance_from_center']
    distance_reward = 1 - (distance_from_center / (track_width / 2))
    
    # Encourage faster lap completion
    lap_progress = progress / float(target_laps)
    time_reward = 1.0 - lap_progress
    
    # Combine distance and time rewards
    reward = (0.6 * distance_reward) + (0.4 * time_reward)
    
    # Penalize going off track
    if not all_wheels_on_track:
        reward = -1.0
    
    return float(reward)
