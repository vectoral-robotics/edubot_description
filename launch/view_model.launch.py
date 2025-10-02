from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('omnibot_description')
    default_model_path = os.path.join(pkg_share, 'urdf', 'omnibot.urdf.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'urdf', 'view.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'model',
            default_value=default_model_path,
            description='Pfad zur URDF/Xacro Datei'
        ),

        DeclareLaunchArgument(
            'rvizconfig',
            default_value=default_rviz_config_path,
            description='Pfad zur RViz Config'
        ),

        # Joint State Publisher GUI
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),

        # Robot State Publisher mit Xacro expand
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('model')])
            }]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', LaunchConfiguration('rvizconfig')],
            output='screen'
        )
    ])
