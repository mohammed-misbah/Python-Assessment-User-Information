from fastapi import FastAPI, File, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from database import SessionLocal
from models import User
import csv
from typing import List
import csv
from io import StringIO


templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
def form_post(request: Request):
    result = "upload file"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

data_list = []  # global variable to store the data
csv_file_submitted = False # Assume csv file is false before submiting a file

@app.post("/file_upload")
def upload(request: Request, file: UploadFile = File(...)):
    """
    Handles file upload, processes the CSV data, and updates global variables.

    Args:
        request (Request): The incoming request.
        file (UploadFile): The uploaded file containing CSV data.

    Returns:
        TemplateResponse: Response with processed data for display.
    """
    global csv_file_submitted
    # Read and decode CSV data from the uploaded file
    datas = file.file.read().decode("utf-8")
    # Create a temporary storage for CSV data
    temp_store = StringIO(datas)
    global data_list

    # Parse CSV data into a list of dictionaries
    data_list = list(csv.DictReader(temp_store))

    # Close the temporary storage and uploaded file
    temp_store.close()
    file.file.close()
    # Set flag to indicate that a CSV file has been submitted
    csv_file_submitted = True

    # Return response with processed data for display
    return templates.TemplateResponse('display.html', context={'request': request, 'items': data_list, 'csv_file_submitted': csv_file_submitted})



@app.post("/save_selected_items")
def save_selected_items(request: Request, selected_items: List[int] = Form(...)):
    """
    Saves selected items to the database.

    Args:
        request (Request): The incoming request.
        selected_items (List[int]): List of indices corresponding to selected items.

    Returns:
        TemplateResponse: Response containing the result message.
    """
    global data_list

    # Extract selected data based on indexes
    selected_data = [data_list[index] for index in selected_items]

    # Create a new database session to store a values
    data_base = SessionLocal()
    try:
        # Iterate through selected data and add to the database
        for item in selected_data:
            user = User(**item)
            data_base.add(user)

        # Commit the changes to the database
        data_base.commit()

    finally:
        # Close the database session in any case
        data_base.close()
    result = f"Successfully saved {len(selected_data)} items to the database"

    # Return response with result message
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})
