#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2
from ball_chaser.srv import DriveToTarget, DriveToTargetResponse


def find_ball(hsv_img):

    # find ball (red)
    lower_red_0 = np.array([0, 43, 46])
    upper_red_0 = np.array([10, 255, 255])
    lower_red_1 = np.array([156, 43, 46])
    upper_red_1 = np.array([180, 255, 255])
    
    mask_red_0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
    mask_red_1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
    mask_red_0 = cv2.medianBlur(mask_red_0, 7)
    mask_red_1 = cv2.medianBlur(mask_red_1, 7)
    
    mask = cv2.bitwise_or(mask_red_0, mask_red_1)
    contour_i, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # find the center of the ball
    avg_y = []
    avg_x = []
    for cnt in contours:
      for c in cnt:
        avg_y.append(c[0][0])
        avg_x.append(c[0][1])
    mean_y = np.mean(avg_y)
    mean_x = np.mean(avg_x)
    mu = (mean_y, mean_x)
    return mu

def process_frame(image_message):

    # convert the image data to opencv format
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_message,desired_encoding='bgr8')
    hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    
    cols,rows,channels = cv_image.shape
    
    x, y = find_ball(hsv_image)

    # wait until the drive_bot service is ready
    rospy.wait_for_service('drive_bot')
    # call the drive_bot service
    chaser = rospy.ServiceProxy('drive_bot', DriveToTarget)

    try:
        # call the service 
        chaser( x, y, rows, cols )
	
    except rospy.ServiceException as e:
    	print("Service call failed: %s"%e)    

def camera2cv():

    # create a node called 'process_img'
    rospy.init_node('process_img',anonymous=True)
    # subscribe the topic to obtain frame information
    rospy.Subscriber( 'camera/rgb/image_raw', Image, process_frame )
    
    rospy.spin()

if __name__ == '__main__':
    camera2cv()
