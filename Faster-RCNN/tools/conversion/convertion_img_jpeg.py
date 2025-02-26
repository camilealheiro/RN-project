from PIL import Image
import os

input_folder = "VOC2007-test/JPEGImages"
output_folder = "VOC2007-test/JPEGImages2" 

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".png"):  
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path).convert("RGB")  

        new_file = file.replace(".png", ".jpg")
        img.save(os.path.join(output_folder, new_file), "JPEG", quality=95)

print("Conversão concluída!")
