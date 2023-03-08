#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import Float32

class SubscriberSample(object):
    def __init__(self):
        self.mainFunction()
    
    def mainFunction(self):
        rospy.Subscriber("/calculate_distance_sample",Float32,self.calculate_distance_callback)

        rospy.spin()

    def calculate_distance_callback(self,distanceData):
        print("\nData = "+ str(distanceData.data) + "\n\n\n")

if __name__ == "__main__":
    try:
        rospy.init_node("subscriberSampleNode",anonymous=True)

        node = SubscriberSample()
        
    except rospy.ROSInterruptException:
        pass
