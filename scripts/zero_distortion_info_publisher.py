#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2022 SoftBank Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import rospy
from sensor_msgs.msg import CameraInfo


class ZeroDistortionInfoPublisher(object):
    def __init__(self):
        self.publisher = rospy.Publisher('~output', CameraInfo, queue_size=1)
        rospy.Subscriber('~input', CameraInfo, self.__publish, queue_size=1)

    def __publish(self, msg):
        msg.D = [0.0] * len(msg.D)
        self.publisher.publish(msg)


if __name__ == '__main__':
    rospy.init_node('zero_distortion_info_publisher')
    rospy.spin()
