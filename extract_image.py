import cv2
import matplotlib.pyplot as plt
import os
# import ollama
import fitz
from pdf2image import convert_from_path
from extract_image_functions import *


## run all the function
raw_pdf_dir = 'raw_pdf'
raw_img_dir_name = 'images'
cropped_img_dir_name = 'cropped_image'

convert_pdf_to_img_page(raw_pdf_dir)
save_all_images(raw_img_dir_name,cropped_img_dir_name)