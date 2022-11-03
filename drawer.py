import os, time
max_image = 30  # 0 inclus
first_year = 1980

for i in range(max_image+1):
    image = f"{i:04d}.jpg"
    os.system(f"python DrawOnGithubActivity/main.py --year {i+first_year} --image {image} --path BadAppleDraw1980-2010")
    os.chdir("./")
    time.sleep(1)

