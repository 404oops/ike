print("Initializing verb 'htmlgen'")
import random

def genlogo():
    print("Generating logo...")
    toreturn = ""
    for i in list("[ike,.!]"):
        toreturn += "<span style='color:" + random.choice(["limegreen", "blue", "yellow", "orange"]) + ";'>" + i + "</span>"
    
    return toreturn

def create_video_page(name, description, path, thumbnail, id):
    # #VideoPath@ike, #VideoName@ike, #VideoDescription@ike, #VideoThumbnail@ike, #Logo@ike(from genlogo whatever thats supposed to be)
    page = open("../templates/video.html", 'r').read()
    replacements = [
        ("#VideoName@ike", name),
        ("#VideoDescription@ike", description),
        ("#VideoThumbnail@ike", thumbnail),
        ("#VideoPath@ike", path),
        ("#Logo@ike", genlogo()),
        ("#VideoID@ike", id),
    ]

    for old, new in replacements:
        page = page.replace(old, new)
    return page

def makevideolist(vidlist):
    toreturn = ""
    for video in vidlist:
        toreturn += f"""
        <div class="container">
            <a href="{video}.html">
                <img src="static/{vidlist[video]["thumbnail"]}">
                <h1>{vidlist[video]["name"]}</h1>
            </a>
        </div>"""
    return toreturn

def genindex(videos):
    index = open("../templates/index.html", 'r').read()
    index = index.replace("#ReplaceVideoList@ike", makevideolist(videos))
    return index