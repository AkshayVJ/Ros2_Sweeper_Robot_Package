import launch
import launch_ros
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.descriptions import ParameterValue
from launch.actions import SetEnvironmentVariable
from ament_index_python.packages import get_package_prefix



def generate_launch_description():

    gazebo_pkg_share = FindPackageShare(package='sweeper_robot_gazebo_package').find('sweeper_robot_gazebo_package')
    world_path=os.path.join(gazebo_pkg_share, 'world/room2.sdf')

    pkg_share = FindPackageShare(package='sweeper_robot_description_package').find('sweeper_robot_description_package')
    model_path = os.path.join(pkg_share, 'urdf/sweeper_robot_description_package.urdf.xacro')

    gazebo_env = SetEnvironmentVariable("GAZEBO_MODEL_PATH", os.path.join(get_package_prefix("sweeper_robot_description_package"), "share"))

    gazebo_launch_world = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so',world_path], 
        output='screen'
    )

    model_arg = DeclareLaunchArgument(
        name='model', 
        default_value=model_path,
        description='Absolute path to robot urdf file'
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),value_type=str)}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    spawn_entity = Node(
    package='gazebo_ros',
    executable='spawn_entity.py',
    arguments=['-entity', 'sweeper_robot_description_package', '-topic', 'robot_description'],
    output='screen'
    )

    return launch.LaunchDescription([
        
        model_arg,
        gazebo_env,
        gazebo_launch_world,
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity
        
    ])
    