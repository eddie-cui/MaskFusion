import os
import cv2
import numpy as np

def process_images_with_opencv(mask_folder, original_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mask_files = [f for f in os.listdir(mask_folder) if f.endswith('.png')]
    original_files = [f for f in os.listdir(original_folder) if f.endswith('.jpg')]

    for original_file in original_files:
        base_name = os.path.splitext(original_file)[0]  
        mask_name = "0"+base_name+ ".png"  

        if mask_name in mask_files:
            original_path = os.path.join(original_folder, original_file)
            mask_path = os.path.join(mask_folder, mask_name)

            original_image = cv2.imread(original_path, cv2.IMREAD_COLOR)  
            mask_image = cv2.imread(mask_path, cv2.IMREAD_COLOR)  
            mask_resized = cv2.resize(mask_image, (original_image.shape[1], original_image.shape[0]), interpolation=cv2.INTER_NEAREST)
            mask_gray = cv2.cvtColor(mask_resized, cv2.COLOR_BGR2GRAY)
            _, mask_binary = cv2.threshold(mask_gray, 32, 255, cv2.THRESH_BINARY)
            b, g, r = cv2.split(original_image)
            alpha = mask_binary  
            output_image = cv2.merge((b, g, r, alpha))  
            output_path = os.path.join(output_folder, original_file.replace('.jpg', '.png'))
            cv2.imwrite(output_path, output_image)
            print(f"Processed: {original_file} -> {output_path}")
        else:
            print(f"Mask file for {original_file} not found.")

mask_folder = 'D:\chz\capture/5\mask' 
original_folder = 'D:\capture/15\images'  
output_folder = 'D:\chz\capture/5\images' 

process_images_with_opencv(mask_folder, original_folder, output_folder)
