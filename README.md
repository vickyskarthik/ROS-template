  ![logo](https://github.com/vickyskarthik/ROS-template/blob/master/images/ros%20logo.png)
  
### MyRobot   
This repo is created as a part of the Robot Operating System(ROS) course.
This repo can be used as a template to create the ROS workspace.

### ROS CHEAT SHEET
Use ROS cheat sheet for reference to ROS command.

### INSTALLATION
To install ROS following the instruction provided in [ROS Wiki](http://wiki.ros.org/ROS/Installation)
1. Choose the intended Ubuntu Operating System.
2. Choose the appropriate ROS version.
3. Setup your sources.list.
4. Set up your keys.
5. Use the cmd sudo apt-get install ros-<ROS Version>-desktop-full
6. Environment setup
7. Dependencies for building packages
8. Initialize rosdep
  
### Workspace Creation
The ROS workspace is commonly called catkin workspace - catkin_ws
use the command

## Check your ROS installation
```cmd
rosversion -d
```

This should return the version of ROS installed
```cmd
echo $ROS_ROOT
```
  
Create a ROS Workspace


```python
mkdir -p ~/your_workspace_name/src
cd ~/your_workspace_name/src
catkin_init_workspace
```


Create a Package
```python
catkin_create_pkg your_package_name roscpp rospy pcl_ros
```

Update the CMakeLists.txt in the pacakage
```python
cmake_minimum_required(VERSION 3.0.2)
project(your_package_name)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
  pcl_ros
)

## System dependencies are found with CMake's conventions
find_package(PCL REQUIRED)

## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
)

## Declare a catkin package
catkin_package()

## Declare a C++ executable
add_executable(main src/main.cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(main
  ${catkin_LIBRARIES}
  ${PCL_LIBRARIES}
)

```
