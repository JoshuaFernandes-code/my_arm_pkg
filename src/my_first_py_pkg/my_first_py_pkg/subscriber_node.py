#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CustomSubscriberNode(Node):
    def __init__(self):
        super().__init__('custom_subscriber')
        
        # Create subscriber: (Message Type, Topic Name, Callback Function, QoS Queue Size)
        self.subscription = self.create_subscription(
            String,
            'custom_chatter',
            self.listener_callback,
            10
        )
        self.get_logger().info("Custom Subscriber Node has started listening...")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received from topic: '{msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    node = CustomSubscriberNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

