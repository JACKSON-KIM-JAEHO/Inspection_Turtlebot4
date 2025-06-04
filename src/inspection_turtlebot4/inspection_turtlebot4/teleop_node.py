#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist
import sys, tty, termios, threading

msg = """
---------------------------
Moving around:
   u(↖)  i(↑)  o(↗)
   j(←)   k    l(→)

anything else : stop
CTRL-C to quit
"""

moveBindings = {
    'i': (1,0,0,0), 'o': (1,0,0,-1), 'j': (0,0,0,1),
    'l': (0,0,0,-1), 'u': (1,0,0,1),
}

def getKey():
    settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('teleop_twist_keyboard')
    pub = node.create_publisher(Twist, 'cmd_vel', 10)
    print(msg)

    try:
        while True:
            key = getKey()
            x, y, z, th = moveBindings.get(key, (0,0,0,0))
            twist = Twist()
            twist.linear.x = x * 0.5
            twist.angular.z = th * 1.0
            pub.publish(twist)
            if key == '\x03':
                break
    except Exception as e:
        print(e)
    finally:
        pub.publish(Twist())
        rclpy.shutdown()
