#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
from first_package.msg import drone

def func(data):

    rospy.loginfo("received message: (%d,%s,%d,%.2f,%.2f)",
    data.id,data.name,data.speed,data.tempeture,data.battery)

rospy.init_node("subscriber",anonymous= True)

rospy.Subscriber("drone_topic",drone,func)

rospy.spin()
