from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='fixposition_orientation',
            executable='fixposition_orientation_node',
            name='fixposition_orientation_node',
        ),
    ])
