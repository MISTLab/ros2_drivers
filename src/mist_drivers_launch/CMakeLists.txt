cmake_minimum_required(VERSION 3.5)
project(mist_drivers_launch)

install(DIRECTORY 
   launch
   DESTINATION share/${PROJECT_NAME}/
)

find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)

find_package(launch_testing_ament_cmake REQUIRED)

find_package(ament_cmake_python REQUIRED)

ament_package()
