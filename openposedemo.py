import os
import subprocess

file = __file__
openposedir = os.path.abspath('openpose')
video = os.path.abspath('arms.mp4')
options = f'--video {video}'
#subprocess.run([r'D:/Documents/openpose-pipeline/openpose/bin/OpenPoseDemo.exe', options], cwd=r'D:/Documents/openpose-pipeline/openpose', shell=False)
subprocess.run([os.path.join(openposedir, 'bin/OpenPoseDemo.exe'), options], cwd=openposedir, shell=False)
