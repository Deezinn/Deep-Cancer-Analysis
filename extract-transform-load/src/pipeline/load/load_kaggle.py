import cv2

class LoadKaggle:
    def save(self, content):
        for c in content:
            cv2.imwrite(c['output_path'], c['resized'])
