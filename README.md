Repo to run multiple robot sensors (cameras, lidars, imus) on ROS 2 inside docker.

To start sensors:
```
make build
make run
make sensors
```

Refer to the `makefile` for the detailed build instructions. 

The robot ID and Lidar hostname specific to the robot should be modified at the top of the makefile.

IMPORTANT: By default, the sensors will run in ROS_DOMAIN_ID=0, change the `robot_id` in the makefile to change the domain. [Explanation on ROS_DOMAIN_ID](https://docs.ros.org/en/foxy/Concepts/About-Domain-ID.html).