import os
import shutil
import cv2

class TransformKaggle:
    def __init__(self, path):
        self.__path = path

    @classmethod
    def verify_if_exists(cls, path):
        if os.path.exists(path):
            destino = '../data/images/raw'
            if not os.path.exists(destino):
                os.makedirs(destino, exist_ok=True)
                shutil.move(path,destino)
        return cls(path)

    def transform_images(self):
        input_folders = [
            '../data/images/raw/1/dataset/yes/3D_Rendering',
            '../data/images/raw/1/dataset/no/3D_Rendering'
        ]

        output_base = '../data/images/process'
        os.makedirs(output_base, exist_ok=True)  
        
        list_images = []

        for folder in input_folders:
            
            subfolder_name = os.path.basename(os.path.dirname(folder))
            output_folder = os.path.join(output_base, subfolder_name)
            os.makedirs(output_folder, exist_ok=True)

            for filename in os.listdir(folder):
                if filename.endswith('.jpg'):
                    img_path = os.path.join(folder, filename)  

                    img = cv2.imread(img_path)
                    if img is None:
                        print(f"Erro ao ler {img_path}")
                        continue

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    resized = cv2.resize(gray, (256, 256))

                    output_path = os.path.join(output_folder, filename)

                    list_images.append({'resized': resized,
                            'output_path': output_path})
                    
        return list_images
                    
                    
