  ![logo](https://github.com/vickyskarthik/ROS-template/blob/master/images/ros%20logo.png)
  
### MyRobot   
This repo is created as a part of the Robot Operating System(ROS) course.
This repo can be used as a template to create the ROS workspace.
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


```python
mkdir catkin_ws
```

Inside the catkin workspace create another directory src
All the programmer code and files are stored in the src directory

```python
cd catkin_ws
mkdir src
```


