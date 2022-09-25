1. red_ball 放到 ~/model_editor_models 中
2.將 ball_chaser 放到 ~/catkin_ws/src 中
3.執行 catkin_make 編譯 ball_chaser
4.source devel/setup.bash
5.export TURTLEBOT3_MODEL=waffle_pi
6.roslaunch ball_chaser ball_chaser.launch
7.在gazebo中，將 red_ball 加入地圖
8.將red_ball移動到 turtlebot看的到的地方
  
