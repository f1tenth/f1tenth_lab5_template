"""This is the launch file used by the autograder to run on Spielberg (one lap):

    ros2 launch pure_pursuit levine_launch.py

Use this to launch the nodes you need for your pure-pursuit implementation and pass in any parameters specified
for this track (levine_launch.py is Levine's). Do NOT run the simulator here as the autograder will 
launch it separately
"""
from launch import LaunchDescription
from launch_ros.actions import Node

# 'pure_pursuit_node.py' is scripts/pure_pursuit_node.py, 'pure_pursuit_node'
# is the C++ src/pure_pursuit_node.cpp: chose the one you used
EXECUTABLE = 'pure_pursuit_node.py'

# `track` tells the skeleton which waypoints to load; add this track's values
# for the other parameters your node declares, e.g. 'lookahead': 1.5
PARAMETERS = {'track': 'spielberg'}


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pure_pursuit',
            executable=EXECUTABLE,
            output='screen',
            parameters=[PARAMETERS],
        ),
    ])
