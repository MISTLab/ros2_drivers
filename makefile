build:
	docker build -f Dockerfile.robot . -t ros2_drivers

start:
	docker run -itd --rm --ipc host --net host --pid host --name ros2_drivers ros2_drivers

stop:
	docker kill ros2_drivers

attach:
	docker exec -it ros2_drivers bash