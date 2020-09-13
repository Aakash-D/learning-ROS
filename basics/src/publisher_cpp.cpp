#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv){
  ros::init(argc, argv, "publisher_cpp");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<std_msgs::String>("chatter", 1000);
  ros::Rate loop_rate(1);

  while(ros::ok()){
    std_msgs::String msg;
    std::stringstream ss;
    ss<<"Hello CPP World";
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}
