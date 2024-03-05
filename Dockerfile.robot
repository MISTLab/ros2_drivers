FROM ros:humble-perception

RUN apt-get update
RUN apt-get install python3-pip python3-vcstool -y

ADD https://api.github.com/repos/MISTLab/ros2_drivers/commits?per_page=1 head_ros2_drivers

RUN git clone https://github.com/MISTLab/ros2_drivers.git &&\
    cd ros2_drivers &&\
    vcs import src < robot.repos

RUN cd ros2_drivers &&\
    rosdep update &&\
    rosdep install --from-paths src --ignore-src -r -y

RUN cd ros2_drivers &&\
    . /opt/ros/humble/setup.sh &&\
    colcon build

COPY config/lidar_config.yaml /ros2_drivers/src/ouster/ros2_ouster/params/driver_config.yaml

RUN cd ros2_drivers &&\
    . /opt/ros/humble/setup.sh &&\
    colcon build

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source ros2_drivers/install/setup.bash" >> ~/.bashrc
