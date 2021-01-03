#/bin/bash

find /media/seyfer/TERRA_SSD/Videos/Gaming/Converted/ -maxdepth 1 -type f -iname "*.mp4" -print0 | sort -zn | xargs -0 -I '{}' python3 my_upload.py '{}';

