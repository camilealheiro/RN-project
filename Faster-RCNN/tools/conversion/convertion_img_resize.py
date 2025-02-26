from PIL import Image
import os

def resize_images(folder_path, output_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.png', '.jpeg')):  
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            img.thumbnail((720, 720))
            
            img.save(os.path.join(output_path, f"{filename}"))

resize_images("Train/JPEGImages-1080", "Train/JPEGImages-720")