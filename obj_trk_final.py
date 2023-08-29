import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("C:/Users/bilal/Desktop/Coding Files/Projects/107/footvolleyball.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
success, img = video.read()

# Select the bounding box on the image
box = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the image and the bounding box
tracker.init(img, box)
    
def goalTrack(img, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img, (c1,c2), 2, (0, 0, 255), 5)

    cv2.circle(img, (int(p1), int(p2)), 2, (0, 255, 0), 3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)
        
    if (dist <= 20):
        cv2.putText(img, "Goal", (300,90), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs) - 1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0, 0, 255), 5)

def drawBox(img, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    check, img = video.read()
    success, box = tracker.update(img)

    if success:
        drawBox(img, box)
    else:
        cv2.putText(img, "Lost", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    goalTrack(img, box)

    cv2.imshow("Output", img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        print("Closing...")
        break
    
video.release()
cv2.destroyALLwindows() 