import cv2
import os
import numpy as np
from PIL import Image

# create recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

face_samples = []
ids = []

# loop through folders
for student_id in os.listdir(dataset_path):

    student_folder = os.path.join(dataset_path, student_id)

    for image_name in os.listdir(student_folder):

        image_path = os.path.join(student_folder, image_name)

        # open image in grayscale
        img = Image.open(image_path).convert("L")

        image_np = np.array(img, "uint8")

        face_samples.append(image_np)

        ids.append(int(student_id))

# train model
recognizer.train(face_samples, np.array(ids))

# save trained model
recognizer.save("trainer.yml")

print("Model trained successfully")
