import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("images/cam1.jpeg")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original Image")
plt.show()
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur image to remove noise
blur = cv2.GaussianBlur(gray, (9, 9), 2)

plt.imshow(blur, cmap='gray')
plt.title("Blurred Image")
plt.show()
edges = cv2.Canny(blur, 50, 150)

plt.imshow(edges, cmap='gray')
plt.title("Edges")
plt.show()
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=100,
    param1=100,
    param2=30,
    minRadius=0,
    maxRadius=0
)
if circles is not None:
    circles = np.uint16(np.around(circles))
    
    for i in circles[0, :]:
        # Draw outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw center
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Detected Circles")
    plt.show()
   
   
    radii = sorted([i[2] for i in circles[0]])

inner_radius = radii[0]
outer_radius = radii[-1]

thickness = outer_radius - inner_radius

print("Inner Radius:", inner_radius)
print("Outer Radius:", outer_radius)
print("Ring Thickness (pixels):", thickness)
radii = sorted([i[2] for i in circles[0]])

inner_radius = radii[0]
outer_radius = radii[-1]

thickness = outer_radius - inner_radius

print("Inner Radius:", inner_radius)
print("Outer Radius:", outer_radius)
print("Ring Thickness (pixels):", thickness)
thickness_mm = thickness * 0.05
print("Thickness in mm:", thickness_mm)