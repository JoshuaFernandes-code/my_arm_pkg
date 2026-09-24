import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Load URDF / Xacro
    urdf_path = os.path.join(
        FindPackageShare('my_arm_pkg').find('my_arm_pkg'),
        'urdf',
        'arm.xacro'
    )
    import xacro
    doc = xacro.parse(open(urdf_path))
    xacro.process_doc(doc)
    robot_description_config = {'robot_description': doc.toxml()}

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description_config]
        )
    ])
