#!/usr/bin/python

import rospy
from std_msgs.msg import String
#from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped


if __name__ == '__main__':
	rospy.init_node('racecar_driver',anonymous=True)
	#pub = rospy.Publisher("/lidar_msg",String,queue_size=1)
	#pub = rospy.Publisher('/vesc/low_level/ackermann_cmd_mux/input/navigation', AckermannDriveStamped,queue_size=1)
	#pub = rospy.Publisher('/racecar/ackermann_cmd_mux/output', AckermannDriveStamped,queue_size=10)
	pub = rospy.Publisher('/vesc/high_level/ackermann_cmd_mux/output', AckermannDriveStamped,queue_size=10)

	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		msg = AckermannDriveStamped()
       		msg.drive.speed = 0.5;
       		msg.drive.acceleration = 1;
       		msg.drive.jerk = 1;
       		msg.drive.steering_angle = 0.5;
       		msg.drive.steering_angle_velocity = 1;

		pub.publish(msg)
	rospy.spin()
