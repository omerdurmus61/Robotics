#include "ros/ros.h"
#include "first_package/zaman.h"

int main(int argc, char **argv)
{
    ros::init(argc,argv,"publisher");

    ros::NodeHandle nh;

    ros::Publisher first_package_sub = nh.advertise<first_package::zaman>("msg_time",100);

    ros::Rate loop_rate(10);

    first_package::zaman msg;

    int count = 0;

    while(ros::ok())
    {
        msg.stamp = ros::Time::now();
        msg.data = count;

        ROS_INFO("Message second = %d",msg.stamp.sec);
        ROS_INFO("Message data = %d",msg.data);


        first_package_sub.publish(msg);

        loop_rate.sleep();

        ++count;
        

    }

    return 0;
}
