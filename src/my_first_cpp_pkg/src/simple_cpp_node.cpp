#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class CustomCppPublisher : public rclcpp::Node {
public:
    CustomCppPublisher() : Node("cpp_publisher_node"), count_(0) {
        // Create publisher on topic '/cpp_chatter'
        publisher_ = this->create_publisher<std_msgs::msg::String>("cpp_chatter", 10);
        
        // Create timer firing every 500ms (2 Hz)
        timer_ = this->create_wall_timer(
            500ms, std::bind(&CustomCppPublisher::timer_callback, this));
        
        RCLCPP_INFO(this->get_logger(), "C++ Publisher Node initialized!");
    }

private:
    void timer_callback() {
        auto message = std_msgs::msg::String();
        message.data = "Hello from C++ ROS 2 Node! Counter: " + std::to_string(count_++);
        
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        publisher_->publish(message);
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    size_t count_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CustomCppPublisher>());
    rclcpp::shutdown();
    return 0;
}
