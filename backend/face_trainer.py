import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
ids = []

dataset_path = "student_images"

for student_id in os.listdir(dataset_path):
    student_folder = os.path.join(dataset_path, student_id)

    for image_name in os.listdir(student_folder):
        img_path = os.path.join(student_folder, image_name)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            faces.append(img)
            ids.append(int(student_id))

recognizer.train(faces, np.array(ids))
recognizer.save("../model/trainer.yml")

print("Training completed successfully")