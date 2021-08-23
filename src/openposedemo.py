import os
import subprocess
from pathlib import Path

def openposedemo(options):
    openposedir = Path(__file__).parent.parent / 'openpose'
    subprocess.run([openposedir / 'bin/OpenPoseDemo.exe', *options], cwd=openposedir)


def run_openpose(input_video, speedup=True, use_hand=False):
    video_name = os.path.split(input_video)[1].split('.')[0]
    folder_path = Path(__file__).parent.parent / 'output' / video_name
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    json_path = os.path.abspath(os.path.join(folder_path, 'json'))
    #os.mkdir(json_path)
    openposedemo(['--video', os.path.abspath(input_video), '--write_json', json_path, '--write_video', os.path.join(folder_path ,video_name + '_saved.avi')]
                 + (['--net_resolution=-1x320', '--tracking', '1', '--number_people_max', '1'] if speedup else [])
                 + (['--net_resolution=-1x160', '--hand'] if use_hand else []))
    return folder_path
