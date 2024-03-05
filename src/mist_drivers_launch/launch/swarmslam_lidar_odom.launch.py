import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import TimerAction, OpaqueFunction, PushLaunchConfigurations, PopLaunchConfigurations, DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import launch_testing
import launch_testing.actions
from launch.substitutions import LaunchConfiguration


def launch_setup(context, *args, **kwargs):

    # Camera
    sensors = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('mist_drivers_launch'), 'launch', 'all_sensors.launch.py')),
        launch_arguments={
            "robot_id": LaunchConfiguration('robot_id').perform(context),
        }.items(),
    )

    # Odom
    odom_proc = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('mist_drivers_launch'), 'launch', 'rtabmap_ouster_lidar_odometry.launch.py')),
            launch_arguments={
                "namespace": "",
                "robot_id": LaunchConfiguration('robot_id').perform(context),
                'log_level': "error",
            }.items(),
        )
    
    # Launch schedule
    schedule = []

    schedule.append(SetEnvironmentVariable('ROS_DOMAIN_ID',  LaunchConfiguration('robot_id').perform(context)))
     
    schedule.append(PushLaunchConfigurations())
    schedule.append(sensors)
    schedule.append(PopLaunchConfigurations())   

    schedule.append(PushLaunchConfigurations())
    schedule.append(odom_proc)
    schedule.append(PopLaunchConfigurations()) 
    
    return schedule


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('robot_id', default_value='0'),
        OpaqueFunction(function=launch_setup)
    ])
