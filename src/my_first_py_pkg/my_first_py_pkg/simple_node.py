#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisher(Node):
    def __init__(self):
        super().__init__('hardware_status_publisher')
        
        # Create publisher using your custom message type
        self.publisher_ = self.create_publisher(HardwareStatus, 'hardware_status', 10)
        self.timer = self.create_timer(1.0, self.publish_hardware_status)
        self.get_logger().info("Hardware Status Publisher Node has been started!")

    def publish_hardware_status(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = "All systems operational"
        
        self.publisher_.publish(msg)
        self.get_logger().info(
            f"Published -> Temp: {msg.temperature}°C, Motors Ready: {msg.are_motors_ready}, Status: '{msg.debug_message}'"
        )

def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
