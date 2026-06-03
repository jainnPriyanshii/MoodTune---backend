import cv2
import base64
import numpy as np

def image_decoder(image):

    

    image_bytes = base64.b64decode(image)

        
    nparr = np.frombuffer(image_bytes, np.uint8)

      
    image = cv2.imdecode(
            nparr,
            cv2.IMREAD_COLOR
        )
    if image is None:
        raise ValueError("Invalid image data")
    return image
