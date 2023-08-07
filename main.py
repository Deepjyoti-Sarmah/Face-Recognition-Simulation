# ##### reading from a folder ###################################################

import cv2
import os

# Path to the input images folder
input_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/Face_working_recognition/Working/images_2'

# Path to the output images folder
output_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/results_123'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the Haar cascade classifier
detector = cv2.CascadeClassifier(
    '/home/deepjyotisarmah/Documents/Drone_stuffs/haarcascade_frontalface_default.xml')

# Iterate over the images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Read the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Convert the image to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = detector.detectMultiScale(img, 1.3, 5)

        # Iterate over the detected faces
        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Save the detected face to the output folder
            face_img = img[y:y + h, x:x + w]
            output_path = os.path.join(output_folder, f'detected_{filename}')
            cv2.imwrite(output_path, face_img)

        # Display the image with detected faces
        cv2.imshow('Detected Faces', img)
        cv2.waitKey(1)  # Introduce a slight delay between images

# Clean up
cv2.destroyAllWindows()


# reading images from lfw ########################################

# import cv2
# import os

# # Path to the input images folder
# input_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/lfw'

# # Path to the output images folder
# output_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/output_images'

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Load the Haar cascade classifier
# detector = cv2.CascadeClassifier('/home/deepjyotisarmah/Documents/Drone_stuffs/haarcascade_frontalface_default.xml')

# # Iterate over the subfolders of the input folder
# for subfolder in os.listdir(input_folder):
#     # Only process the first 1000 images
#     if len(os.listdir(os.path.join(input_folder, subfolder))) > 100:
#         num_images = 100
#     else:
#         num_images = len(os.listdir(os.path.join(input_folder, subfolder)))

#     # Iterate over the images in the subfolder
#     for i in range(num_images):
#         filename = os.listdir(os.path.join(input_folder, subfolder))[i]
#         if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
#             # Read the image
#             img_path = os.path.join(input_folder, subfolder, filename)
#             img = cv2.imread(img_path)

#             # Convert the image to grayscale
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#             # Detect faces in the grayscale image
#             faces = detector.detectMultiScale(gray, 1.3, 5)

#             # Iterate over the detected faces
#             for (x, y, w, h) in faces:
#                 # Draw a rectangle around the face
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#                 # Save the detected face to the output folder
#                 face_img = gray[y:y + h, x:x + w]
#                 output_path = os.path.join(output_folder, subfolder, os.path.basename(img_path))
#                 os.makedirs(output_path, exist_ok=True)
#                 cv2.imwrite(output_path, face_img)

#         # Display the image with detected faces
#         cv2.imshow('Detected Faces', img)
#         cv2.waitKey(1) # Introduce a slight delay between images

# # Clean up
# cv2.destroyAllWindows()


############################################################################

# import cv2
# import os

# # Path to the input images folder
# input_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/lfw'

# # Path to the output images folder
# output_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/output_images'

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Load the Haar cascade classifier
# detector = cv2.CascadeClassifier('/home/deepjyotisarmah/Documents/Drone_stuffs/haarcascade_frontalface_default.xml')

# # Iterate over the subfolders of the input folder
# for subfolder in os.listdir(input_folder):
#     subfolder_path = os.path.join(input_folder, subfolder)
#     if os.path.isdir(subfolder_path):  # Check if it is a subfolder
#         images = os.listdir(subfolder_path)
#         num_images = min(len(images), 100)  # Limit the number of images to 100

#         # Iterate over the images in the subfolder
#         for i in range(num_images):
#             filename = images[i]
#             if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
#                 # Read the image
#                 img_path = os.path.join(subfolder_path, filename)
#                 img = cv2.imread(img_path)

#                 # Convert the image to grayscale
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#                 # Detect faces in the grayscale image
#                 faces = detector.detectMultiScale(gray, 1.3, 5)

#                 # Iterate over the detected faces
#                 for (x, y, w, h) in faces:
#                     # Draw a rectangle around the face
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#                     # Save the detected face to the output folder
#                     output_subfolder = os.path.join(output_folder, subfolder)
#                     os.makedirs(output_subfolder, exist_ok=True)  # Create the subfolder
#                     output_path = os.path.join(output_subfolder, filename)  # Use the original filename
#                     face_img = gray[y:y + h, x:x + w]
#                     cv2.imwrite(output_path, face_img)

#             # Display the image with detected faces
#             cv2.imshow('Detected Faces', img)
#             cv2.waitKey(1)  # Introduce a slight delay between images

# # Clean up
# cv2.destroyAllWindows()


##############################################################################
# import cv2
# import os

# # Path to the input images folder
# input_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/Hog/Youtube/input_images'

# # Path to the output images folder
# output_folder = r'/home/deepjyotisarmah/Documents/Drone_stuffs/Hog_output_images'

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Load the Haar cascade classifier
# detector = cv2.CascadeClassifier('/home/deepjyotisarmah/Documents/Drone_stuffs/haarcascade_frontalface_default.xml')

# # Maximum number of images to process in total
# max_total_images = 1000
# total_images_processed = 0

# # Iterate over the subfolders of the input folder
# for subfolder in os.listdir(input_folder):
#     subfolder_path = os.path.join(input_folder, subfolder)
#     if os.path.isdir(subfolder_path):  # Check if it is a subfolder
#         images = os.listdir(subfolder_path)
#         num_images = min(len(images), max_total_images - total_images_processed)  # Limit the number of images per subfolder

#         # Iterate over the images in the subfolder
#         for i in range(num_images):
#             filename = images[i]
#             if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
#                 # Read the image
#                 img_path = os.path.join(subfolder_path, filename)
#                 img = cv2.imread(img_path)

#                 # Convert the image to grayscale
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#                 # Detect faces in the grayscale image
#                 faces = detector.detectMultiScale(gray, 1.3, 5)

#                 # Iterate over the detected faces
#                 for (x, y, w, h) in faces:
#                     # Draw a rectangle around the face
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#                     # Save the detected face to the output folder
#                     output_subfolder = os.path.join(output_folder, subfolder)
#                     os.makedirs(output_subfolder, exist_ok=True)  # Create the subfolder
#                     output_path = os.path.join(output_subfolder, filename)  # Use the original filename
#                     face_img = gray[y:y + h, x:x + w]
#                     cv2.imwrite(output_path, face_img)

#             # Display the image with detected faces
#             cv2.imshow('Detected Faces', img)
#             cv2.waitKey(1)  # Introduce a slight delay between images

#             total_images_processed += 1
#             if total_images_processed >= max_total_images:
#                 break

#     if total_images_processed >= max_total_images:
#         break

# # Clean up
# cv2.destroyAllWindows()


# area of interest detections 