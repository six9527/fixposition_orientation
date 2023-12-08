import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from autoware_sensing_msgs.msg import GnssInsOrientation
from pix_hooke_driver_msgs.msg import V2aDriveStaFb
from fixposition_driver_ros2.msg import Speed


class FixPositionOrientationNode(Node):

    def __init__(self):
        super().__init__('fixposition_orientation_node')
        self.get_logger().info('FixPositionOrientationNode has been started.')

        self.sub_odometry_enu = self.create_subscription(
            Odometry,
            '/fixposition/odometry_enu',  # Replace with the actual topic name
            self.odometry_callback,
            10)
        
        self.sub_hook_speed = self.create_subscription(
            V2aDriveStaFb,
            '/pix_hooke/v2a_drivestafb',  # Replace with the actual topic name
            self.speed_callback,
            10)

        self.pub_oriention = self.create_publisher(
            GnssInsOrientation,
            '/autoware_orientation',  # Replace with the actual topic name
            10)
        
        self.pub_speed = self.create_publisher(
            Speed,
            '/fixposition/speed',  # Replace with the actual topic name
            10)
        
        
    
    def speed_callback(self,msg):
        vehicle_speed = Speed()
        vehicle_speed.speeds = [int(msg.vcu_chassis_speed_fb * 1000)]
        self.pub_speed.publish(vehicle_speed)


    def odometry_callback(self, msg):
        # Extract the orientation from the Odometry message
        orientation = msg.pose.pose.orientation

        # Create a GnssInsOrientation message and set its values
        gnss_ins_orientation_msg = GnssInsOrientation()
        gnss_ins_orientation_msg.orientation = orientation
        gnss_ins_orientation_msg.rmse_rotation_x = 0.0017  # Set the appropriate values
        gnss_ins_orientation_msg.rmse_rotation_y = 0.0017  # Set the appropriate values
        gnss_ins_orientation_msg.rmse_rotation_z = 0.0017  # Set the appropriate values

        # Publish the GnssInsOrientation message
        self.pub_oriention.publish(gnss_ins_orientation_msg)

def main(args=None):
    rclpy.init(args=args)

    fixposition_orientation_node = FixPositionOrientationNode()

    try:
        rclpy.spin(fixposition_orientation_node)
    except KeyboardInterrupt:
        pass

    fixposition_orientation_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
