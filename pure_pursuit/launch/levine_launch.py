"""This is the launch file used by the autograder to run on Levine (levine_blocked, three laps):

    ros2 launch pure_pursuit levine_launch.py

Use this to launch the nodes you need for your pure-pursuit implementation and pass in any parameters specified
for this track (spielberg_launch.py is Spielberg's). Do NOT run the simulator here as the autograder will 
launch it separately
"""
from launch import LaunchDescription
from launch_ros.actions import Node

# 'pure_pursuit_node.py' is scripts/pure_pursuit_node.py, 'pure_pursuit_node'
# is the C++ src/pure_pursuit_node.cpp: name the one you wrote
EXECUTABLE = 'pure_pursuit_node.py'

# this map's values for the parameters your node declares
# e.g. {'max_speed': 6.0} or give it a full .yaml config file
PARAMETERS = {'track': 'levine'}


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pure_pursuit',
            executable=EXECUTABLE,
            output='screen',
            parameters=[PARAMETERS],
        ),
    ])
