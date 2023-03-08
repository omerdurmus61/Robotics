#include <ros/ros.h>
#include <sensor_msgs/Joy.h>


class TeleopRobot
{
public:
  TeleopRobot()
  {
    nh_.param("axis_linear", linear_, linear_);
    nh_.param("axis_angular", angular_, angular_);
    nh_.param("scale_angular", a_scale_, a_scale_);
    nh_.param("scale_linear", l_scale_, l_scale_);

    joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopRobot::joyCallback, this);
  }

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
  {
    float angular = a_scale_*joy->axes[angular_];
    float linear = l_scale_*joy->axes[linear_];
    float analogLt = l_scale_*joy->axes[2];
    float analogRt = a_scale_*joy->axes[5];
    int buttonA = joy->buttons[0];
    int buttonB = joy->buttons[1];
    int buttonX = joy->buttons[2];
    int buttonY = joy->buttons[3];
    int buttonLB = joy->buttons[4];
    int buttonRB = joy->buttons[5];
  }

  ros::NodeHandle nh_;

  int linear_, angular_;
  double l_scale_, a_scale_;
  ros::Subscriber joy_sub_;

};


int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_robot");
  TeleopRobot teleop_robot;

  ros::spin();
}