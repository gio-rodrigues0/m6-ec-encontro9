import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import os
from supabase import create_client, Client
import time

app = FastAPI()

url: str = "https://rxqmpnumofinecvdttsr.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4cW1wbnVtb2ZpbmVjdmR0dHNyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njc3MTQ5NCwiZXhwIjoyMDAyMzQ3NDk0fQ.jC21KS9xsc2-Y5k3TMgNcYGyLtXyZDyaHGNdcpXXUL0"
supabase: Client = create_client(url, key)
bucket_name: str = "bucketlindo"

@app.get("/list")
async def list():
    res = supabase.storage.from_(bucket_name).list()
    print(res)

@app.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):
    with open(f"recebidos/siu{time.time()}.png", 'wb') as f:
        dados = content.file.read()
        f.write(dados)
    return {"status": "ok"}

list_files = os.listdir("recebidos")

@app.post("/images")
def images():
    for arquivo in list_files:
        with open(os.path.join("recebidos", arquivo), 'rb+') as f:
            dados = f.read()
            res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
    return {"message": "Image uploaded successfully"}