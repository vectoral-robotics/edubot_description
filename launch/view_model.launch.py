"""
Launch file for visualizing the OmniBot robot description (URDF/Xacro).

Starts:
  - joint_state_publisher_gui for interactive joint control
  - robot_state_publisher to publish TFs from the URDF/Xacro
  - optional RViz2 visualization with a predefined config
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition


def generate_launch_description():
    # ----------------------------------------------------------
    # Default paths
    # ----------------------------------------------------------
    model_path = PathJoinSubstitution([
        FindPackageShare('omnibot_description'),
        'urdf',
        'omnibot.urdf.xacro',
    ])
    rviz_config_path = PathJoinSubstitution([
        FindPackageShare('omnibot_description'),
        'urdf',
        'view.rviz',
    ])

    # ----------------------------------------------------------
    # Launch arguments
    # ----------------------------------------------------------
    declare_model = DeclareLaunchArgument(
        'model',
        default_value=model_path,
        description='Path to the URDF/Xacro model file.',
    )

    declare_rvizconfig = DeclareLaunchArgument(
        'rvizconfig',
        default_value=rviz_config_path,
        description='Path to the RViz configuration file.',
    )

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Whether to start RViz2 automatically.',
    )

    # ----------------------------------------------------------
    # Nodes
    # ----------------------------------------------------------

    # GUI to move joints manually
    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
    )

    # Robot State Publisher (expands Xacro -> URDF -> TF)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', LaunchConfiguration('model')]),
        }],
    )

    # Optional RViz2 visualization
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
        condition=IfCondition(LaunchConfiguration('use_rviz')),
    )

    # ----------------------------------------------------------
    # LaunchDescription
    # ----------------------------------------------------------
    return LaunchDescription([
        declare_model,
        declare_rvizconfig,
        declare_use_rviz,
        joint_state_publisher_gui,
        robot_state_publisher,
        rviz,
    ])
