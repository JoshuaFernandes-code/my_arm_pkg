import os
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch

def generate_launch_description():
    # Path to arm.xacro in my_arm_pkg
    arm_pkg_share = get_package_share_directory('my_arm_pkg')
    xacro_file_path = os.path.join(arm_pkg_share, 'urdf', 'arm.xacro')

    moveit_config = (
        MoveItConfigsBuilder("robotic_arm", package_name="my_arm_config")
        .robot_description(file_path=xacro_file_path)
        .robot_description_semantic(file_path="config/robotic_arm.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .robot_description_kinematics(file_path="config/kinematics.yaml")
        .joint_limits(file_path="config/joint_limits.yaml")
        .to_moveit_configs()
    )

    return generate_demo_launch(moveit_config)
