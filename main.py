from lib import data, html
import argparse
import json
import os


parser = argparse.ArgumentParser()
parser.add_argument( # args.input
    "-i", "--input", "-v", "--video",
    nargs=1,
    type=str,
    required=True,
    help="Path for video file",
    default=None,
    metavar="VideoFile"
)
parser.add_argument( # args.config
    "-c", "--config", "-cfg",
    nargs=1,
    type=str,
    required=True,
    help="Path for Configuration file",
    default=None,
    metavar="ConfigFile"
)
print("Checking for arguments...")
args = parser.parse_args()

config = json.loads(open(args.config[0], 'r').read())

videoname = config['name']
description = config['metadata']['description']
thumbnail = config['metadata']['thumbnail']
print("Checking if input files exist...")
video = data.checkvideo(args.input[0])
id = data.uuidgen()

print(f"""
Video name: {videoname}
Metadata:
    - Description: {description}
    - Thumbnail path: {thumbnail}

Video path: {video}
Video UUID: {id}
Processing the data...
""")

try: 
    os.mkdir("temp")
except FileExistsError:
    pass
os.system(f"cp {video} temp/{id}.{video.split('.')[-1]}")
os.system(f"cp {thumbnail} temp/{id}.{thumbnail.split('.')[-1]}")

print("Moving...")
os.chdir("temp")

video = f"{id}.{video.split('.')[-1]}"
thumbnail = f"{id}.{thumbnail.split('.')[-1]}"
page = id+".html"

print("Generating page...")
i = open(page, 'w')
i.write(html.create_video_page(videoname,description,"video/"+video,"static/"+thumbnail,id,"static/"+darkthumb))
i.close()
print("Moving files to the distribution directory...")

os.system(f"mv {video} ../dist/video")
os.system(f"mv {page} ../dist/")
os.system(f"mv {thumbnail} ../dist/static")
os.system(f"mv {darkthumb} ../dist/static")

print("Page Created!")
print("Moving on...")

os.chdir("../dist")

print("Registering video...")

try:
    open("videos.json", 'x')
    open("videos.json", 'w').write("{}")
except FileExistsError:
    pass

cfg = open("videos.json", 'r').read()
videos = json.loads(cfg)
cfg = open("videos.json", 'w')
videos[id] = {
    "name": videoname,
    "description": description,
    "thumbnail": thumbnail,
}
cfg.write(json.dumps(videos))
print("Generating index.html...")

with open("index.html", 'w') as index:
    index.write(html.genindex(videos))
print("Done! Your video should be available as " + videoname + " in the index or as " + id + ".html")
