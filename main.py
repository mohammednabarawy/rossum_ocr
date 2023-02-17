import requests
import json
import csv
import pandas as pd
from rossum.lib.api_client import RossumClient
import datetime
import time


# Login to Rossum API
username = "username"
password = "password"
queue_id = 'queue_id'
path = r"C:\Users\moham\desktop\New folder\01 - 0175.jpg"
api_url = "https://api.elis.rossum.ai/v1"


def upload():
    # Upload the image to Rossum API
    with RossumClient(
        context=None, user=username, password=password, url=api_url
    ) as client:
        response = client.upload_document(queue_id, path)

    annotation_url = response["results"][0]["annotation"]
    print("The file is reachable at the following URL:", annotation_url)


def wait():
    # Wait for 20 seconds with progress printing
    print("Waiting for 20 seconds...")
    for i in range(20):
        print(f"{i+1} seconds passed.")
        time.sleep(1)

    print("Finished waiting.")


def export_documents():
    # Export OCR data for confirmed documents
    with RossumClient(context=None, user=username, password=password, url=api_url) as client:
        date_today = datetime.date.today()
        date_start = datetime.date(date_today.year, 1, 1)
        date_end = datetime.date(date_today.year, 12, 31)
        response = client.get(
            f"queues/{queue_id}/export?format=xlsx&"
            f"status=confirmed,exported,reviewing,importing&"
            f"ordering=exported_at&"
            f"page_size=100&page=1"
        )

    if not response.ok:
        raise ValueError(f"Failed to export: {response.status_code}")

    # Save the response to a file
    with open("exported_data.xlsx", "wb") as f:
        f.write(response.content)

    print("OCR data for confirmed documents exported to file 'exported_data.xlsx'")


def clean_exported_data():
    # Load the exported excel file into a DataFrame
    df = pd.read_excel("exported_data.xlsx")

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Drop empty columns
    df.dropna(axis=1, how="all", inplace=True)

    # Save the cleaned DataFrame back to the same excel file
    with pd.ExcelWriter("exported_data.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    print("Exported data cleaned and saved to 'exported_data.xlsx'")


upload()
wait()
export_documents()
clean_exported_data()
