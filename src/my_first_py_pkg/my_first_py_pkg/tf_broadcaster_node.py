#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class FrameBroadcaster(Node):
    def __init__(self):
        super().__init__('tf_broadcaster_node')
        
        # Initialize the Transform Broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback) # 10 Hz
        self.angle_ = 0.0
        self.get_logger().info("TF2 Broadcaster Node active. Publishing base_link -> sensor_frame transform...")

    def broadcast_timer_callback(self):
        t = TransformStamped()

        # Header metadata
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'       # Parent frame
        t.child_frame_id = 'sensor_frame'    # Child frame

        # Simulated circular movement in 3D space
        t.transform.translation.x = 0.5 * math.cos(self.angle_)
        t.transform.translation.y = 0.5 * math.sin(self.angle_)
        t.transform.translation.z = 0.2

        # Fixed unit quaternion rotation (no rotation)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)
        self.angle_ += 0.05

def main(args=None):
    rclpy.init(args=args)
    node = FrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
