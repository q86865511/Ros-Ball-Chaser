# Ros-Ball-Chaser
於Gazebo及Rviz 3D中，利用cv2和ROS實作出一個能夠讓robot追著紅球跑的程式。

# 使用流程
1. red_ball 放到 ~/model_editor_models 中

2.將 ball_chaser 放到 ~/catkin_ws/src 中

3.執行 catkin_make 編譯 ball_chaser

4.source devel/setup.bash

5.export TURTLEBOT3_MODEL=waffle_pi

6.roslaunch ball_chaser ball_chaser.launch

7.在gazebo中，將 red_ball 加入地圖

8.將red_ball移動到 turtlebot看的到的地方

# 結果圖
![圖](https://user-images.githubusercontent.com/95120819/192147346-1bd4b131-dbdb-4096-924a-1c32d1d3272c.png)

# 備註
中原大學ROS智慧機器人系統概論project
