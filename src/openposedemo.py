import os
import subprocess

def openposedemo(options):
    openposedir = os.path.abspath('openpose')
    subprocess.run([os.path.join(openposedir, 'bin/OpenPoseDemo.exe'), *options], cwd=openposedir)


def run_openpose(input_video, speedup=True):
    video_name = os.path.split(input_video)[1].split('.')[0]
    folder_path = os.path.abspath(os.path.join('output', video_name))
    os.mkdir(folder_path)
    json_path = os.path.abspath(os.path.join(folder_path, 'json'))
    #os.mkdir(json_path)
    openposedemo(['--video', os.path.abspath(input_video), '--write_json', json_path, '--write_video', os.path.join(folder_path ,video_name + '_saved.avi')] + (['--tracking', '1', '--number_people_max', '1'] if speedup else []))
    return folder_path
