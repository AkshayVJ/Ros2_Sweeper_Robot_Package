
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os
from launch_ros.descriptions import ParameterValue
#from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    #pkg_share = get_package_share_directory('sweeper_robot_description_package')
    pkg_share = FindPackageShare(package='sweeper_robot_description_package').find('sweeper_robot_description_package')
    model_path = os.path.join(pkg_share, 'urdf/sweeper_robot_description_package.urdf.xacro')
    rviz_config_path = os.path.join(pkg_share, 'config/display.rviz')
    
    #use_sim_time = LaunchConfiguration('use_sim_time')

    model_arg = DeclareLaunchArgument(
        name='model', 
        default_value=model_path,
        description='Absolute path to robot urdf file'
    )
    
    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig', 
        default_value=rviz_config_path,
        description='Absolute path to rviz config file'
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

    # joint_state_publisher_gui_node = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     name='joint_state_publisher_gui'
    # )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')]
    )
  
    return LaunchDescription([

        model_arg,
        rviz_arg,
        joint_state_publisher_node,
        #joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])
    