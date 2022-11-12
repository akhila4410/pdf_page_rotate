import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from fastapi import FastAPI ,File, UploadFile
import uvicorn
import shutil
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def welcome():
    content = """
    <head>
    <style>
    .center {
              text-align: center;
              color: red;
              font-size:50px;
            }
    .center1 {
              text-align: center;
              color: black;
              font-size:30px;
            }
    .button {
              border: none;
              display: flex;
              color: #4CAF50;
              padding: 40px 70px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 35px;
              margin: 4px 2px;
              cursor: pointer;
              border: 2px solid #4CAF50;
              justify-content: center;
            }
    .center2 {
              margin: 0;
              position: absolute;
              top: 50%;
              left: 50%;
              -ms-transform: translate(-50%, -50%);
              transform: translate(-50%, -50%);
            }
    .button1:hover {
                  background-color: #4CAF50;
                  color: white;
                  }
    </style>
    </head>
    <body style="background-color:powderblue;">
    <p class = "center"> PDF_ROTATE-API</p> 
    <p class = "center1"> Rotate the page you like at a specified angle </p>
    <a href = "http://127.0.0.1:8080/docs">
    <div class="center2"><button class = "button button1" > Browse file </button></div>
    </a>
    </body>
    """
    return HTMLResponse(content=content)

@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    with open("rot.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.get("/rotate/{n}/{angle}")
def pdf_rotate(n:int,angle: int):
    pdf_in = open("rot.pdf", 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        if i==n-1:
            page.rotateClockwise(angle)
        pdf_writer.addPage(page)

    pdf_out = open('Rotated_file', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return {"filename":'Rotated_file'}

if __name__ == '__main__':
    uvicorn.run("pdf_rotate:app", host="127.0.0.1", port=8080, reload=True)



