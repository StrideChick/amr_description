import os

import launch_ros
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time", default="true")
    use_rviz_arg = DeclareLaunchArgument("use_rviz", default_value="true")

    urdf_file = os.path.join(
        get_package_share_directory("amr_description"),
        "amr",
        "amr.urdf"
    )

    robot_description = launch_ros.descriptions.ParameterValue(
        Command(["xacro ", urdf_file]), value_type=str  # スペースを追加
    )
    
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {"robot_description": robot_description},
            {"use_sim_time": use_sim_time}
        ],
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[
            {"robot_description": robot_description},
            {'use_gui': False}
        ]
    )

    rviz_node = Node(
        condition=IfCondition(LaunchConfiguration("use_rviz")),
        package="rviz2",
        executable="rviz2",
        name="rviz2",
    )

    return LaunchDescription([
        use_rviz_arg,
        joint_state_publisher,
        robot_state_publisher,
        rviz_node
    ])
