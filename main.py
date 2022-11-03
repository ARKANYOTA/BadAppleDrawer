import cv2
x, y = 52, 7
nb_images = 2010-1980
vidcap_len = 0
vidcapt = cv2.VideoCapture("videoplayback.mp4")
successs, image = vidcapt.read()
while successs:
    successs, image = vidcapt.read()
    if cv2.waitKey(10) == 27:
        break
    vidcap_len += 1

vidcap = cv2.VideoCapture("videoplayback.mp4")
count = 0
# Capture video frame by frame
success, image = vidcap.read()
  
# Declare the variable with value 0
count = 0
img_count = 0
  
# Creating a loop for running the video
# and saving all the frames
while success:
  
    # Capture video frame by frame
    success, image = vidcap.read()
  
    if count%(vidcap_len//nb_images) == 0:
        # Resize the image frames
        resize = cv2.resize(image, (x, y))
      
        # Saving the frames with certain names
        cv2.imwrite("%04d.jpg" % img_count, resize)
        img_count += 1
  
    # Closing the video by Escape button
    if cv2.waitKey(10) == 27:
        break
  
    # Incrementing the variable value by 1
    count += 1
