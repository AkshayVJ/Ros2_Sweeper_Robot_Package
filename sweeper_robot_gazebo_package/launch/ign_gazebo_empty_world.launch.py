import launch
import launch_ros
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():

    gazebo_launch_world = ExecuteProcess(
        cmd=['ign', 'gazebo'],
            output='screen'
    )
    return launch.LaunchDescription([
        gazebo_launch_world
        
    ])
    