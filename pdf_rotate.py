import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from fastapi import FastAPI ,File, UploadFile
import uvicorn
import shutil
from fastapi.responses import HTMLResponse
from html_file import content

app = FastAPI()

@app.get('/')
def welcome():
    return HTMLResponse(content=content)

@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    with open("uploadedfile.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.get("/rotate/{n}/{angle}")
def pdf_rotate(n:int,angle: int):
    pdf_in = open("uploadedfile.pdf", 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        if i==n-1:
            page.rotateClockwise(angle)
        pdf_writer.addPage(page)

    pdf_out = open('/home/akki4410/Desktop/Rotated_file', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return {"filepath":'/home/akki4410/Desktop/Rotated_file'}

if __name__ == '__main__':
    uvicorn.run("pdf_rotate:app", host="127.0.0.1", port=8080, reload=True)

