import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import cv2
import cairosvg
import os
import re

first_year = 1980
last_year = 2010

for i in range(first_year, last_year+1):
    os.system(f"curl 'https://github.com/ARKANYOTA?tab=overview&from={i}-12-01&to={i}-12-31' | htmlq '.js-calendar-graph-svg' >> {i}.html")
    lines = open(f"{i}.html", "r").readlines()
    lines[0] = lines[0][:-2] + ' xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">' + ">"
    lines.insert(1, """<style>
*{
    background: #0D1117;
}
.d-0 {
    fill: #161b22;
}
.d-1 {
    fill: #0e4429;
}
.d-2 {
    fill: #006d32;
}
.d-3 {
    fill: #26a641;
}
.d-4 {
    fill: #39d353;
}
.ContributionCalendar-label{
    fill: white;

}
</style>""")
    text = "".join(lines)
    text = re.sub(r'data-hydro-click="[^"]*"', '', text)
    text = re.sub(r'data-hydro-click-hmac="[^"]*"', '', text)
    text = re.sub(r'data-date="[^"]*"', '', text)
    text = re.sub(r'data-level="[^"]*"', '', text)
    text = re.sub(r'class="ContributionCalendar-day"', '', text)
    text = re.sub(r'data-count="([^"]*)"', r'class="d-\g<1>"', text)
    open(f"{i}.svg", "w").write(text)



for i in range(first_year, last_year+1):
    # -*- coding: utf-8 -*-
    cairosvg.svg2png(url=f'{i}.svg', write_to=f'{i}.png')

image_folder = './'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
