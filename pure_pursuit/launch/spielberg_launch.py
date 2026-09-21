"""What the autograder runs on Spielberg (one lap):

    ros2 launch pure_pursuit spielberg_launch.py

Everything this track needs goes here: one node or several, Python or C++,
the waypoints to follow and the parameter values that suit this track
(levine_launch.py is Levine's). Start your own nodes only: the
simulator is already running.
"""
from launch import LaunchDescription
from launch_ros.actions import Node

# 'pure_pursuit_node.py' is scripts/pure_pursuit_node.py, 'pure_pursuit_node'
# is the C++ src/pure_pursuit_node.cpp: name the one you wrote
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
