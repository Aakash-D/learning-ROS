#include "ros/ros.h"
#include "std_msgs/String.h"

void callback(const std_msgs::String::ConstPtr& data){
  ROS_INFO("message is: %s", data->data.c_str());
}

int main(int argc, char **argv){
  ros::init(argc, argv, "subscriber_cpp");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("chatter", 1000, callback);
  ros::spin();
  return 0;
}
