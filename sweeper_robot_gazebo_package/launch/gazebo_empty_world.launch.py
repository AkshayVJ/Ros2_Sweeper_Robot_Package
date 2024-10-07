import launch
import launch_ros
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():

    gazebo_launch_world = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'], 
        output='screen'
    )

    return launch.LaunchDescription([
        gazebo_launch_world
        
    ])
    