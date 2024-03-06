OUSTER_HOST_NAME=os-992039000794.local
ROBOT_ID=0

build:
	docker build -f Dockerfile.robot . -t ros2_drivers

run:
	docker run -itd --rm --ipc host --net host --pid host --privileged -v /dev/:/dev/  -e OUSTER_HOST_NAME=$(OUSTER_HOST_NAME) --name ros2_drivers ros2_drivers

start:
	docker start ros2_drivers

stop:
	docker stop ros2_drivers

kill:
	docker kill ros2_drivers

attach:
	docker exec -it ros2_drivers bash

sensors:
	docker exec -it ros2_drivers bash -c "source /opt/ros/humble/setup.bash; source ros2_drivers/install/setup.bash; ros2 launch mist_drivers_launch all_sensors.launch.py robot_id:=$(ROBOT_ID)"

swarmslam-lidar:
	docker exec -it ros2_drivers bash -c "source /opt/ros/humble/setup.bash; source ros2_drivers/install/setup.bash; ros2 launch mist_drivers_launch swarmslam_lidar_odom.launch.py robot_id:=$(ROBOT_ID)"