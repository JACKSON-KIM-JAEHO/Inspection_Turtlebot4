#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
import numpy as np
import cv2

class LiDARSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.create_subscription(
            LaserScan, '/scan', self.lidar_cb, qos_profile_sensor_data)

    def lidar_cb(self, msg):
        lidar = np.array(msg.ranges)
        lidar = np.resize(lidar, (20, 720))
        cv2.imshow('LiDAR', lidar)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = LiDARSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
