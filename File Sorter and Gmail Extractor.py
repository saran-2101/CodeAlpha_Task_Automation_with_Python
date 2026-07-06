# -------------------------------------------------------
# Project: Python File Organizer & Gmail Extractor
# Author : SARAN
# Description:
# Organizes text and image files into separate folders
# and extracts unique Gmail addresses from text files.
# -------------------------------------------------------

import os
import shutil
from pathlib import *

# Source folder containing files to organize
source = r"C:\Users\saran\Documents\Test_Folder"

# Destination folder where organized files will be stored
destination = r"C:\Users\saran\OneDrive\Pictures"

# Set to store unique Gmail addresses
emailset = set()

try:

    # Loop through every file in the source folder
    for file in os.listdir(source):

        # Get the file extension and convert it to lowercase
        ext = os.path.splitext(file)[1][1:].lower()

        # Change the current working directory to the destination folder
        os.chdir(destination)

        # Process Text Files
        if ext == "txt":

            # Create the 'Text Files' folder if it doesn't exist
            if not os.path.exists("Text Files"):
                os.mkdir("Text Files")

            # Copy the text file to the destination folder
            shutil.copy(
                os.path.join(source, file),
                os.path.join(destination, "Text Files", file)
            )

            # Read the text file and extract Gmail addresses
            with open(os.path.join(source, file), "r", encoding="utf-8") as line:
                for text in line:
                    text = text.strip()

                    # Check if the line ends with '@gmail.com'
                    if text.endswith("@gmail.com"):

                        # Store only unique email addresses
                        if text not in emailset:
                            emailset.add(text)

        # Process Image Files
        elif ext in ("jpg", "jpeg", "png"):

            # Create the 'Images' folder if it doesn't exist
            if not os.path.exists("Images"):
                os.mkdir("Images")

            # Copy the image file to the Images folder
            shutil.copy(
                os.path.join(source, file),
                os.path.join(destination, "Images", file)
            )

    # Save all unique email addresses into Email.txt
    with open(os.path.join(destination, "Email.txt"), "w", encoding="utf-8") as em:
        for email in emailset:
            em.write(email + "\n")

    print("Task Completed Successfully!")

except Exception as e:
    print("Error:", e)