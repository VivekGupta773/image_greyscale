import cv2
import os

# Function to convert image to grayscale
def convert_to_grayscale(image_path, output_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, grayscale_image)

# Directory containing the images
directory = "Narendra_Modi"
output = 'output'

# Loop through each image in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(directory, filename)
        output_path = os.path.join(output, "grayscale_" + filename)
        convert_to_grayscale(image_path, output_path)

        print(f"Converted {filename} to grayscale.")
    
    else:
        continue

print("Conversion completed.")
