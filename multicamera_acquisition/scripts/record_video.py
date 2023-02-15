import sys
from multicamera_acquisition.paths import DATA_DIR
from multicamera_acquisition.acquisition import acquire_video
import json


camera_list = [
    {'name': 'BackLeft', 'serial': 22181546, 'brand':'flir', 'gain': 12, "display":True},
    {'name': 'BackRight', 'serial': 22181539, 'brand':'flir', 'gain': 12, "display":True},
    {'name': 'FrontRight', 'serial': 22181541, 'brand':'flir', 'gain': 12, "display":True},
    {'name': 'FrontLeft', 'serial': 22181612, 'brand':'flir', 'gain': 12, "display":True},
    ##{'name': 'Bottom', 'serial': 22181550, 'brand':'flir', 'gain': 12, "display":True},
    {'name': 'Top', 'serial': 22181547, 'brand':'flir', 'gain': 12, "display":True},
]


    

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(len(sys.argv))
        print("Usage: python my_script.py [param1] [param2] [param3]")
        sys.exit(1)

    save_location = sys.argv[1]
    recording_duration_s = sys.argv[2]
    framerate = sys.argv[3]
    exposure_time = sys.argv[4]

    acquire_video(
        save_location,
        camera_list,
        framerate = int(framerate),
        exposure_time = int(exposure_time),
        recording_duration_s = int(recording_duration_s),
    )