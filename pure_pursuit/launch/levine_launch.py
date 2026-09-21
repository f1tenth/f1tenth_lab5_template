"""What the autograder runs on Levine (levine_blocked, three laps):

    ros2 launch pure_pursuit levine_launch.py

Everything this track needs goes here: one node or several, Python or C++,
the waypoints to follow and the parameter values that suit this track
(spielberg_launch.py is Spielberg's). Start your own nodes only: the
simulator is already running.
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
