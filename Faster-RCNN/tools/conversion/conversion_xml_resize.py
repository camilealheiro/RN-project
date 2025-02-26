import os
import xml.etree.ElementTree as ET

def resize_boxes(boxes, orig_size, target_width):
    orig_width, orig_height = orig_size
    scale_x = target_width / orig_width
    scale_y = scale_x  
    target_height = int(orig_height * scale_y)
    
    new_boxes = [
        int(boxes[0] * scale_x),
        int(boxes[1] * scale_y),
        int(boxes[2] * scale_x),
        int(boxes[3] * scale_y)
    ]
    return new_boxes, target_height

def process_annotations(input_folder, output_folder, target_width=720):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            file_path = os.path.join(input_folder, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            orig_width = int(root.find("size/width").text)
            orig_height = int(root.find("size/height").text)
            
            for obj in root.findall("object"):
                bndbox = obj.find("bndbox")
                xmin = int(bndbox.find("xmin").text)
                ymin = int(bndbox.find("ymin").text)
                xmax = int(bndbox.find("xmax").text)
                ymax = int(bndbox.find("ymax").text)
                
                new_coords, target_height = resize_boxes([xmin, ymin, xmax, ymax], (orig_width, orig_height), target_width)
                
                bndbox.find("xmin").text = str(new_coords[0])
                bndbox.find("ymin").text = str(new_coords[1])
                bndbox.find("xmax").text = str(new_coords[2])
                bndbox.find("ymax").text = str(new_coords[3])
                
            root.find("size/width").text = str(target_width)
            root.find("size/height").text = str(target_height)
            
            output_path = os.path.join(output_folder, filename)
            tree.write(output_path)
            print(f"Processado: {filename}")

input_folder = "Train\Annotations-3"  
output_folder = "Train\Annotations-3-720"  
process_annotations(input_folder, output_folder)
