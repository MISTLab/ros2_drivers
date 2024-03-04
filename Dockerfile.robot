FROM ros:humble-perception

RUN apt-get update
RUN apt-get install python3-pip python3-vcstool -y

RUN git clone https://github.com/MISTLab/ros2_drivers.git &&\
    cd ros2_drivers &&\
    vcs import src < robot.repos

RUN cd ros2_drivers &&\
    rosdep update &&\
    rosdep install --from-paths src --ignore-src -r -y

RUN cd ros2_drivers &&\
    . /opt/ros/humble/setup.sh &&\
    colcon build