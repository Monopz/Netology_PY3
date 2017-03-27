import os
import sys
import subprocess

def search_jpg(folder):
    yield from (
        filename
        for filename in os.listdir(folder)
        if '.jpg' in filename
    )

def resize_pic(folder, filename, resized_folder='result'):
    geometry = '-resize 200'.split()

    resized_folder = os.path.join(folder, resized_folder)
    if not os.path.exists(resized_folder):
        os.mkdir(resized_folder)

    original_filepath = os.path.join(folder, filename)
    resized_filepath = os.path.join(resized_folder, filename)

    return subprocess.Popen([
        'convert',
        *geometry,
        original_filepath,
        resized_filepath
    ])

def convert_pictures(jobs):
    # start jobs by turning generator into list
    for job in list(jobs):
        try:
            job.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            job.terminate()
            job.wait()

if __name__ == '__main__':
    folder = '/Picture'
    if len(sys.argv) == 2:
        folder = sys.argv[-1]

    convert_pictures(
        resize_pic(folder, filename)
        for filename in search_jpg(folder)
    )
