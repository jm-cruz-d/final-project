#!/bin/bash
from google_images_download import google_images_download
import sys

# To get images for Dataset
def getImage(search, numberPhotos):
    #class instantiation
    response = google_images_download.googleimagesdownload()   
    #creating list of arguments
    arguments = {"keywords": search, "limit": numberPhotos, "print_urls":True}   
    #passing the arguments to the function
    response.download(arguments)   

# Create a folder downloads with other folder inside with the search
getImage(sys.argv[1], sys.argv[2])

# Calling in Terminal: python3 download_imag.py search numberPhotos