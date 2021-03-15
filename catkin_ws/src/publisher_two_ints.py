#!/usr/bin/env python  
import rospy

from my_pkg.msg import two_ints

def main():
   rospy.init_node("two_ints_publisher")
   pub = rospy.Publisher("tow_ints", two_ints, queue_size=1)
   r=rospy.Rate(1)
   
   msg = two_ints()
   while not rospy.is_shutdown():
      msg.a = 2
      msg.b = 3
      pub.publish(msg)
      r.sleep()

if __name__ =="__main__":
   try:
      main()
   except rospy.ROSInterruptException:
      pass  

