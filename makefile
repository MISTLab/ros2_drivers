OUSTER_HOST_NAME=os-992039000794.local

build:
	docker build -f Dockerfile.robot . -t ros2_drivers

start:
	docker run -itd --rm --ipc host --net host --pid host --privileged -v /dev/:/dev/  -e OUSTER_HOST_NAME=$(OUSTER_HOST_NAME) --name ros2_drivers ros2_drivers

stop:
	docker kill ros2_drivers

attach:
	docker exec -it ros2_drivers bash