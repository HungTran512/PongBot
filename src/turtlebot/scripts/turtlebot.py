#!/usr/bin/env python
import roslib; roslib.load_manifest('lab3')
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan


def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = msg.ranges[len(msg.ranges)/2]

    
# Main program
g_range_ahead = 1 # anything to start

# Declare a subscriber to message 'scan' with message class LaserScan
scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)

# Same code can be a publisher and a subscriber, this is no problem
# be ready to publish the cmd_vel topic of class Twist
cmd_vel_pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)

# Declare us to be a node
rospy.init_node('wander')
state_change_time = rospy.Time.now()

# driving_forward: forward(true) vs. spin inplace (false)
#   TRUE: until x seconds pass or get close to an obstacle, go forward
#   FALSE: until y seconds pass, spin in place
driving_forward = True
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    print("***")
    print(rospy.Time.now() > state_change_time, g_range_ahead, driving_forward)

    # check whether antyhing is closer than x meters or 
    # time for driving foreward is over, then start spinning in place
    if driving_forward:
        if math.isnan(g_range_ahead):
            driving_forward = False
            state_change_time = rospy.Time.now() + rospy.Duration(3)
        elif (g_range_ahead < 0.5 or rospy.Time.now() > state_change_time):
            driving_forward = False
            state_change_time = rospy.Time.now() + rospy.Duration(3)
            
    # check whether time to spin is over, then go back to driving
    else: # we're not driving_forward
        if rospy.Time.now() > state_change_time:
            driving_forward = True # we're done spinning, time to go forward!
            state_change_time = rospy.Time.now() + rospy.Duration(3)
    
    # Create an all zero Twist() message. Note a new one is created each loop
    twist = Twist()

    # Depending on whether we are driving foreward, set linear or angular
    if driving_forward:
        twist.linear.x = 0.2
    else:
        twist.angular.z = 1.0
    
    # Publish cmd_vel with the desired motion
    cmd_vel_pub.publish(twist)

    # Sleep for 1/rate seconds
rate.sleep()