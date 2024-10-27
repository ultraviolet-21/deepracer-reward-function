# deepracer-reward-function

This is the reward function for an AWS Deepracer model. The reward depends on various input parameters, including the distance from the center, the speed, and the % of track completed. If the vehicle crashes or ends up off the track, the reward will be very low. 

During the Deepracer competition, I experimented with some of the factors, especially the speed. I didn't want to reward speed too much, because that would cause the vehicle to go too fast and end up off the track. This would end up increasing the time taken to complete a lap. I made the reward less dependent on speed and more on progress, and I heavily discouraged going off-track or backwards.
