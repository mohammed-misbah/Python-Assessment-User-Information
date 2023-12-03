import io
from fastapi import FastAPI, File, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import SessionLocal
from models import User
import csv
from typing import List
from io import BytesIO
import csv
from io import TextIOWrapper


templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
def form_post(request: Request):
    result = "upload file"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.post("/")
def upload(request: Request, file: UploadFile = File(...)):
    print('AAAAAAAAAAA')
    contents1 = file.file.read()
    print("BBBBBBBBB")
    buffer1 = TextIOWrapper(BytesIO(contents1), encoding='utf-8', newline='')
    print("CCCCCCCCCCCC")
    reader = csv.DictReader(buffer1)
    print("DDDDDDDDDDD")
    # Assuming you want to convert the CSV data to a list of dictionaries
    global data_list
    data_list = list(reader)

    buffer1.close()
    file.file.close()

    return templates.TemplateResponse('index.html', context={'request': request, 'result': data_list})


@app.get('/display')
def get(request: Request):
    global data_list
    return templates.TemplateResponse('display.html', context={'request': request, 'data_list': data_list})









# @app.post("/file_upload")
# async def upload_file(request: Request, name: str = Form(...), age: str = Form(...)):
#     file = request.files['csv']
    
#     # Specify the file name
#     file_name = "people_data.csv"

#     # Save the uploaded file
#     with open(file_name, mode='wb') as csv_file:
#         csv_file.write(file.file.read())
#         print(file, "file name is readed")

#     # Read CSV file and map columns
#     names, ages = read_csv_and_map_columns(file_name, name, age)
#     print(names, ages, "Getting an name and age field is")
#     # Save data to SQLite database
#     save_to_database(names, ages)

#     print(f"Data from CSV file '{file_name}' has been saved to the database.")
#     return templates.TemplateResponse("index.html", {"request": request, "names": names, "ages": ages})