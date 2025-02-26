import os
import xml.etree.ElementTree as ET
import cv2

yolo_labels_path = "Test\Annotations-1"  
images_path = r"images\test"  
output_voc_path = "Test\Annotations-1-xml" 
classes = ["0", "1", "2"]  

os.makedirs(output_voc_path, exist_ok=True)

def yolo_to_voc(yolo_file, image_file):
    image = cv2.imread(image_file)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_file}")
        return

    h, w, c = image.shape

    annotation = ET.Element("annotation")
    
    ET.SubElement(annotation, "folder").text = "VOC2007"
    ET.SubElement(annotation, "filename").text = os.path.basename(image_file)

    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "The VOC2007 Database"
    ET.SubElement(source, "annotation").text = "PASCAL VOC2007"
    ET.SubElement(source, "image").text = "flickr"

    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = str(w)
    ET.SubElement(size, "height").text = str(h)
    ET.SubElement(size, "depth").text = str(c)

    ET.SubElement(annotation, "segmented").text = "0"

    with open(yolo_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])

            xmin = int((x_center - width / 2) * w)
            ymin = int((y_center - height / 2) * h)
            xmax = int((x_center + width / 2) * w)
            ymax = int((y_center + height / 2) * h)

            obj = ET.SubElement(annotation, "object")
            ET.SubElement(obj, "name").text = classes[class_id]  
            ET.SubElement(obj, "pose").text = "Unspecified"
            ET.SubElement(obj, "truncated").text = "0"
            ET.SubElement(obj, "difficult").text = "0"

            bndbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bndbox, "xmin").text = str(xmin)
            ET.SubElement(bndbox, "ymin").text = str(ymin)
            ET.SubElement(bndbox, "xmax").text = str(xmax)
            ET.SubElement(bndbox, "ymax").text = str(ymax)

    tree = ET.ElementTree(annotation)
    output_file = os.path.join(output_voc_path, os.path.basename(yolo_file).replace(".txt", ".xml"))
    tree.write(output_file)
    print(f"Arquivo salvo: {output_file}")

for txt_file in os.listdir(yolo_labels_path):
    if txt_file.endswith(".txt"):
        yolo_path = os.path.join(yolo_labels_path, txt_file)
        image_path = os.path.join(images_path, txt_file.replace(".txt", ".png")) 
        if os.path.exists(image_path):
            yolo_to_voc(yolo_path, image_path)
        else:
            print(f"Imagem correspondente não encontrada: {image_path}")
