# Rossum API Example
This is an example code that shows how to use the Rossum API to upload a document, extract text data using OCR, and export the OCR data to an Excel file.

## Prerequisites
To use this code, you'll need the following:

A Rossum API account. You can sign up for a free account at https://rossum.ai/.
Python 3.6 or higher. You can download Python from the official website: https://www.python.org/.

## Installation
Clone this repository to your local machine.

Open the terminal and navigate to the cloned repository.

Install the required Python packages by running the following command:
pip install -r requirements.txt

## Usage
Open the main.py file in your favorite text editor.

Enter your Rossum API account credentials (username and password) in the username and password variables at the beginning of the file.

Enter the ID of the Rossum API queue where you want to upload the document in the queue_id variable.

Enter the path to the image file that you want to upload in the path variable.

Save the changes to the file.

Open the terminal and navigate to the cloned repository.

Run the following command to upload the document, wait for 20 seconds, and export the OCR data to an Excel file:
python rossum_api.py
After the script finishes running, you'll find the exported OCR data in a file named exported_data.xlsx.


## Conclusion
That's it! You now know how to use the Rossum API to upload a document, extract text data using OCR, and export the OCR data to an Excel file. You also know how to clean the exported data using the data_cleaning.py script. Feel free to modify the code to suit your specific needs.
