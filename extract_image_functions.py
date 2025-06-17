import cv2
import matplotlib.pyplot as plt
import os
# import ollama
import pymupdf
from pdf2image import convert_from_path



def convert_pdf_to_img_page(raw_pdf_dir):
    for file_name in os.listdir(os.path.join(os.getcwd(),raw_pdf_dir)):
        file_path = os.path.join(os.getcwd(), raw_pdf_dir, file_name)
        # open the PDF file
        pdf_file = pymupdf.open(file_path)
        
        # Iterate over PDF pages
        for page_index in range(len(pdf_file)):
            # get the page itself
            page = pdf_file.load_page(page_index)  # load the page
            # Convert PDF page to image
            pix = page.get_pixmap(dpi=300)  # render the page to an image
            # Save the image to a file
            image_path = os.path.join(os.getcwd(), 'images', f'{file_name}_{page_index + 1}.png')
            # Ensure the directory exists
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            # Save the image as a PNG file
            pix.save(image_path)
            print(f"{file_name}{page_index + 1} saved as {image_path}")
            
        # Close the PDF file
        pdf_file.close()


def crop_quadilateral(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)
    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Loop through the contours and find all rectangles or squares
    rectangles = []
    for contour in contours:
        # Approximate the contour shape
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        # Check if the contour is rectangular (4 points) and convex
        if len(approx) == 4 and cv2.isContourConvex(approx):
            # Store the rectangle's bounding box
            rectangles.append(approx)

    # Plot all detected rectangles
    cropped_image = []
    for i, rectangle in enumerate(rectangles):
        # Get the bounding box coordinates for each rectangle
        x, y, w, h = cv2.boundingRect(rectangle)
        # Crop and save the image for each rectangle
        cropped_image.append(image[y:y+h, x:x+w])
    return cropped_image


def save_all_images(raw_img_dir_name, cropped_img_dir_name):
    for img in os.listdir(os.path.join(os.getcwd(),raw_img_dir_name)):
        image_path = os.path.join(os.getcwd(),raw_img_dir_name,img)
        print(f"processing : {image_path}")
        cropped_image = crop_quadilateral(image_path)
        # print(cropped_image)
        for i in range(len(cropped_image)):
            # print(f"{(cropped_image[i].shape[0] * cropped_image[i].shape[1])/1024}")
            if (cropped_image[i].shape[0] * cropped_image[i].shape[1])/1024 > 100:
                # dir_name = 'cropped_image'
                cropped_block_path = os.path.join(os.getcwd(),cropped_img_dir_name,f'{img}_cropped_block_{i}.png')
                # print(cropped_block_path)
                cv2.imwrite(cropped_block_path,cropped_image[i])
