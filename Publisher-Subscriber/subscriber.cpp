#include "ros/ros.h"
#include "first_package/zaman.h"

void func(const first_package::zaman::ConstPtr& msg)
{
    ROS_INFO("received message = %d",msg->stamp.sec);
    ROS_INFO("received message = %d",msg->stamp.nsec);
    ROS_INFO("received message = %d",msg->data);

}

int main(int argc, char **argv)
{
    ros::init(argc,argv,"subscriber");

    ros::NodeHandle nh;

    ros::Subscriber first_package_sub = nh.subscribe("msg_time",100,func);

    ros::spin();
    

    return 0;
}
