# Learning ROS

## The basics

### Publisher & Subscriber nodes

/publisher_node sends a 'Hello World' message as a String via the topic /chatter, which is received by the /subscriber_node

These publisher and subscriber nodes are implemented in pyton and cpp, python ones can be launched by the launch file `pub-sub.launch` and the cpp ones can be launched using `pub-sub_cpp.launch`

### rrbot

rrbot as the name suggests is a robot manipulator with 2 revolute joints, this is an opensource robot by Dave Coleman, developed to get familiar with ROS and Gazebo, can be found [here](https://github.com/ros-simulation/gazebo_ros_demos). Here I am controlling the joint positons of the robot..

###### prerequisites

I had some errors following the instructions here, had some packages missing, could finally control the robot after installing them by running the below commands

`sudo apt-get install ros-kinetic-joint-state-publisher-gui`

`sudo apt-get install ros-kinetic-ros-control ros-kinetic-ros-controllers ros-kinetic-gazebo-ros-control`

###### Controlling RRbot    

Gazebo and ROS control need to be launched before controlling the robot, they can be run by `roslaunch rrbot_gazebo rrbot_world.launch` and `roslaunch rrbot_control rrbot_control.launch`

This 2DOF robot is controlled by publishing individual joint values as Float64 to their respective topics

The publisher node to control robot can be run by `rosrun basics rrbot_pub.py`
