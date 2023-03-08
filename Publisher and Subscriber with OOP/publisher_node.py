#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import Float32
import random

class PublisherSample(object):
    def __init__(self):
        self.totalDistance = 0

        self.mainFunction()

    def calculateDistance(self):
        randomValue = random.uniform(10,100)

        return randomValue

    def mainFunction(self):
        distanceCalculatePublish = rospy.Publisher("/calculate_distance_sample",Float32,queue_size=10)

        rate = rospy.Rate(2)

        distanceCalculateMessage = Float32()

        while not rospy.is_shutdown():
            self.totalDistance += self.calculateDistance()

            distanceCalculateMessage.data = self.totalDistance

            rospy.loginfo(distanceCalculateMessage)

            distanceCalculatePublish.publish(distanceCalculateMessage)

            rate.sleep()

if __name__ == "__main__":
    try:
        rospy.init_node("PublisherSampleNode",anonymous=True)

        node = PublisherSample()

    except rospy.ROSInterruptException:
        pass