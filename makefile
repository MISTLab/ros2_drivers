OUSTER_HOST_NAME=os-992039000794.local

install_zenoh:
	echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
	sudo apt update
	sudo apt install zenoh-bridge-ros2dds

launch_zenoh:
	zenoh-bridge-ros2dds -c config/zenoh_config.json5

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
	docker exec -it ros2_drivers ros2 launch mist_drivers_launch sensors.launch.py
	# $(MAKE) launch_zenoh

swarmslam-lidar:
	docker exec -it ros2_drivers ros2 launch mist_drivers_launch swarmslam_lidar_odom.launch.py