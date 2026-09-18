#include <sstream>
#include <string>
#include <cmath>
#include <vector>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "nav_msgs/msg/odometry.hpp"
#include "ackermann_msgs/msg/ackermann_drive_stamped.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"
#include "visualization_msgs/msg/marker.hpp"
#include <tf2_ros/transform_broadcaster.h>
#include <tf2/LinearMath/Matrix3x3.h>
#include <tf2/LinearMath/Quaternion.h>
/// CHECK: include needed ROS msg type headers and libraries

using namespace std;

class PurePursuit : public rclcpp::Node
{
    // Implement PurePursuit
    // This is just a template, you are free to implement your own node!

private:

public:
    PurePursuit() : Node("pure_pursuit_node")
    {
        // The autograder starts this node twice: with track:=levine, then with track:=spielberg
        std::string track = this->declare_parameter<std::string>("track", "levine");

        // TODO: load the waypoints of `track` from the package's installed waypoints/ folder:
        //       ament_index_cpp::get_package_share_directory("pure_pursuit") + "/waypoints/<your csv>"
        //       (#include "ament_index_cpp/get_package_share_directory.hpp").
        //       A path like /home/you/... only exists on your laptop.

        // TODO: create ROS subscribers and publishers
    }

    void pose_callback(const geometry_msgs::msg::PoseStamped::ConstPtr &pose_msg)
    {
        // TODO: find the current waypoint to track using methods mentioned in lecture

        // TODO: transform goal point to vehicle frame of reference

        // TODO: calculate curvature/steering angle

        // TODO: publish drive message, don't forget to limit the steering angle.
    }

    ~PurePursuit() {}
};
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PurePursuit>());
    rclcpp::shutdown();
    return 0;
}