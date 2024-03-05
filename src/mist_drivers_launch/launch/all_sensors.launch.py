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
    camera_proc = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('mist_drivers_launch'), 'launch', 'realsense_d400.launch.py')),
        launch_arguments={
            "namespace": "/r" + LaunchConfiguration('robot_id').perform(context),
        }.items(),
    )

    lidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros2_ouster'), 'launch', 'driver_launch.py')),
	)

    imu = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('vectornav'), 'launch',
                         'vectornav.launch.py')),
        )

    tf_process = Node(package="tf2_ros",
                      executable="static_transform_publisher",
                      arguments="0 0 0 0 0 0 base_link laser_sensor_frame".split(" "),
                      parameters=[])

    tf_process2 = Node(package="tf2_ros",
                      executable="static_transform_publisher",
                      arguments="0 0 0 0 0 0 base_link laser_data_frame".split(" "),
                      parameters=[])

    tf_process_imu = Node(package="tf2_ros",
                      executable="static_transform_publisher",
                      arguments="0.0679 -0.073 0.342 3.14159 0 3.14159 base_link vectornav".split(" "),
                      parameters=[])
    
    # Launch schedule
    schedule = []

    schedule.append(SetEnvironmentVariable('ROS_DOMAIN_ID',  LaunchConfiguration('robot_id').perform(context)))
     
    schedule.append(PushLaunchConfigurations())
    schedule.append(camera_proc)
    schedule.append(PopLaunchConfigurations())   

    schedule.append(PushLaunchConfigurations())
    schedule.append(lidar)
    schedule.append(PopLaunchConfigurations())  

    schedule.append(PushLaunchConfigurations())
    schedule.append(tf_process)
    schedule.append(PopLaunchConfigurations())  

    schedule.append(PushLaunchConfigurations())
    schedule.append(tf_process2)
    schedule.append(PopLaunchConfigurations()) 

    schedule.append(PushLaunchConfigurations())
    schedule.append(tf_process_imu)
    schedule.append(PopLaunchConfigurations())

    schedule.append(PushLaunchConfigurations())
    schedule.append(imu)
    schedule.append(PopLaunchConfigurations()) 

    return schedule


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('robot_id', default_value='0'),
        OpaqueFunction(function=launch_setup)
    ])
