#!/usr/bin/env python

from __future__ import print_function
from geometry_msgs.msg import Twist
import rospy
from ball_chaser.srv import DriveToTarget, DriveToTargetResponse

def drive_to_target(req):

    # create a publisher which publish message to the 'cmd_vel' topic 
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) # start publisher of cmd_vel to control Turtlesim
    # try

    twist = Twist()
    
    # get the position of the ball
    ball_x = req.x
    left_th = req.image_width / 3
    right_th = (req.image_width / 3) * 2

    # compute the corresponding moving directions
    if ball_x < left_th:
        # try
        twist.linear.x = 0.0
        twist.angular.z = 0.05
        # Create Twist message & add linear x and angular z
        
    elif ball_x > right_th:
        # try
        twist.linear.x = 0.0
        twist.angular.z = -0.05
        
    elif ball_x < right_th and ball_x > left_th:
        # try
        twist.linear.x = 0.1
        twist.angular.z = 0.0
        
    else:
        # try
        twist.linear.x = 0.0
        twist.angular.z = 0.0

    # send the message
    pub.publish(twist)
    
    return DriveToTargetResponse('done.')

def drive_bot():
    
    #create a node called chaser
    rospy.init_node('chaser',anonymous=True)
    #create a service that invokes drive_to_target
    s = rospy.Service('drive_bot', DriveToTarget, drive_to_target)

    rospy.spin()

if __name__ == "__main__":
    drive_bot()
