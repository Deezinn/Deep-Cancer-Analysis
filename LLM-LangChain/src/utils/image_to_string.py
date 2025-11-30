import base64

def transform_to_base64(image):
    return base64.b64encode(image).decode() 