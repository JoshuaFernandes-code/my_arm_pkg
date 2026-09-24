from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the Publisher Node
        Node(
            package='my_first_py_pkg',
            executable='my_node',
            name='publisher_node_launched'
        ),
        # Launch the Subscriber Node
        Node(
            package='my_first_py_pkg',
            executable='my_sub',
            name='subscriber_node_launched'
        )
    ])

