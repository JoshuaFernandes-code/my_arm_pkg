#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeTwoInts

class ComputeTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__('compute_two_ints_client')
        self.client_ = self.create_client(ComputeTwoInts, 'compute_two_ints')
        
        # Wait for the service server to come online before sending requests
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, a, b):
        request = ComputeTwoInts.Request()
        request.a = a
        request.b = b
        
        # Asynchronous service call
        self.future = self.client_.call_async(request)
        return self.future

def main(args=None):
    rclpy.init(args=args)
    node = ComputeTwoIntsClientNode()
    
    # Send request with values 10 and 32
    future = node.send_request(10, 32)
    
    # Wait until the future receives a response from the server
    rclpy.spin_until_future_complete(node, future)
    
    try:
        response = future.result()
        node.get_logger().info(f"Result of compute_two_ints: {response.sum}")
    except Exception as e:
        node.get_logger().error(f"Service call failed: {e}")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

