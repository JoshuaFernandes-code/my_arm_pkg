#!/usr/bin/env python3
import rclpy
from rclpy.lifecycle import LifecycleNode, State, TransitionCallbackReturn

class HardwareLifecycleNode(LifecycleNode):
    def __init__(self):
        super().__init__('hardware_lifecycle_node')
        self.get_logger().info("Lifecycle Node instantiated (State: UNCONFIGURED)")

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Configuring hardware interfaces and parameters...")
        # Allocate resources or load calibration files here
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Activating hardware output streams (State: ACTIVE)...")
        # Enable motor drivers or hardware publish loops here
        return super().on_activate(state)

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Deactivating hardware output streams (State: INACTIVE)...")
        # Pause hardware execution safely
        return super().on_deactivate(state)

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Cleaning up memory and hardware connections...")
        # Free memory or reset configuration
        return TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info("Shutting down node safely...")
        return TransitionCallbackReturn.SUCCESS

def main(args=None):
    rclpy.init(args=args)
    node = HardwareLifecycleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
