#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class FrameListener(Node):
    def __init__(self):
        super().__init__('tf_listener_node')
        
        # Buffer stores incoming dynamic transforms over time
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Call lookup_transform every 1 second
        self.timer = self.create_timer(1.0, self.on_timer)
        self.get_logger().info("TF2 Listener Node initialized. Listening for base_link -> sensor_frame...")

    def on_timer(self):
        from_frame_rel = 'sensor_frame'
        to_frame_rel = 'base_link'

        try:
            # Look up the latest available transform between base_link and sensor_frame
            t = self.tf_buffer.lookup_transform(
                to_frame_rel,
                from_frame_rel,
                rclpy.time.Time())

            x = t.transform.translation.x
            y = t.transform.translation.y
            z = t.transform.translation.z

            self.get_logger().info(
                f"Transform lookup success! [{from_frame_rel} -> {to_frame_rel}]: x={x:.2f}, y={y:.2f}, z={z:.2f}"
            )

        except TransformException as ex:
            self.get_logger().info(f"Could not transform {to_frame_rel} to {from_frame_rel}: {ex}")

def main(args=None):
    rclpy.init(args=args)
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
