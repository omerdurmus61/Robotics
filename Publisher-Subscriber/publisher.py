#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from first_package.msg import drone
import random

pub = rospy.Publisher("drone_topic",drone,queue_size=10)

rospy.init_node("publisher",anonymous= True)

rate = rospy.Rate(10)

i = 0

while(not rospy.is_shutdown()):

    drone_data = drone()

    drone_data.id = 1
    drone_data.name = "drone-001"
    drone_data.speed = random.randint(5,25)
    drone_data.tempeture = random.uniform(20,30)
    drone_data.battery = 4000 - i

    rospy.loginfo(drone_data)

    pub.publish(drone_data)

    rate.sleep()

    i = i+1