import launch
import launch_ros
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    pkg_share = FindPackageShare(package='sweeper_robot_gazebo_package').find('sweeper_robot_gazebo_package')
    world_path=os.path.join(pkg_share, 'world/room2.sdf')


    gazebo_launch_world = ExecuteProcess(
        cmd=['ign', 'gazebo', world_path],
            output='screen'
    )

    return launch.LaunchDescription([
        gazebo_launch_world
        
    ])
    