import easyocr
import cv2
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

import mangarecog

output_dir = Path('./output/cropped_images')
output_dir.mkdir(parents=True, exist_ok=True)

font_path = './font/NotoSansCJK-Regular.ttc'

reader = easyocr.Reader(['ja'])

def display_japanese_text(image, text, position, font_path, font_size=20):
    # Convert OpenCV image (BGR) to PIL image (RGB)
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image_pil)

    # Draw the text on the image
    draw.text(position, text, font=font, fill=(255, 0, 0))  # Green text color

    # Convert back to OpenCV image (RGB to BGR)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    return image

def detect_text(image_path):
    result = reader.readtext(image_path)
    return result

def show_textregion(image, result):
    combined_text = ""
    
    for i, (bbox, text, prob) in enumerate(result):
        # Ensure the bounding box coordinates are in integer format
        (top_left, top_right, bottom_right, bottom_left) = bbox
        
        # Convert the bounding box coordinates to integers
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Draw rectangle around the detected text region
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        
        # Crop the image using array slicing (top-left to bottom-right)
        cropped_image = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        
        # Save the cropped image for debugging or further use
        cropped_path = output_dir / f'cropped_{i}.jpg'
        cv2.imwrite(str(cropped_path), cropped_image)
        print(f"Cropped image saved to {cropped_path}")
        
        # Use MangaOCR to recognize text in the cropped image
        mocrtext = mangarecog.recognize_text(cropped_path)
        print(f"Recognized text (MangaOCR): {mocrtext}")
        
        # Accumulate the recognized text into the combined_text string
        combined_text += mocrtext.strip() + " "  # Add space between each text block
        
        # Display the recognized text on the image
        image = display_japanese_text(image, mocrtext, top_left, font_path)
        cv2.imshow("Text Detection", image)  # Display the image with text regions

    return combined_text