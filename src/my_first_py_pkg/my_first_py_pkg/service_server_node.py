#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeTwoInts

class ComputeTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__('compute_two_ints_server')
        
        # Create service server: (Interface Type, Service Name, Callback Function)
        self.srv = self.create_service(
            ComputeTwoInts,
            'compute_two_ints',
            self.compute_two_ints_callback
        )
        self.get_logger().info("Compute Two Ints Service Server is ready!")

    def compute_two_ints_callback(self, request, response):
        # Process the request parameters 'a' and 'b'
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming Request: a={request.a}, b={request.b} -> Returning Sum={response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ComputeTwoIntsServerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
