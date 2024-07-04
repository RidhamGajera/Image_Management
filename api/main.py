# api/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.db_utils import create_image_record, get_all_images, delete_image_record
from utils.s3_utils import upload_to_s3, delete_from_s3

app = FastAPI()

class Image(BaseModel):
    filename: str
    url: str

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save to local DB
        image_id = create_image_record(file.filename)

        # Save to AWS S3
        upload_to_s3(file, image_id)

        return JSONResponse(content={"message": "Upload successful", "filename": file.filename})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/images/")
async def read_images():
    try:
        images = get_all_images()
        return images

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{image_id}")
async def delete_image(image_id: int):
    try:
        # Delete from local DB
        filename = delete_image_record(image_id)

        # Delete from AWS S3
        delete_from_s3(image_id, filename)

        return JSONResponse(content={"message": f"Image {image_id} deleted successfully"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
