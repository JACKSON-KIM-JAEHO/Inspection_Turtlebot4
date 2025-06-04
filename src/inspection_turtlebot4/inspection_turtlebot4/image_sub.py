#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.bridge = CvBridge()
        self.create_subscription(
            Image, '/oakd/rgb/preview/image_raw', self.image_cb, qos_profile_sensor_data)

    def image_cb(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow('Camera', image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
