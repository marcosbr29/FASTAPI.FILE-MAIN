from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException
from domain import file_processor

from domain.file_processor import FileProcessor

router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()


@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    return await FileProcessor().upload_file(file)


@router.post("/file/add_data")
async def add_data(conta: str, agencia: str, texto: str, valor: float):
    data = {"conta": conta, "agencia": agencia, "texto": texto, "valor": valor}
    return await FileProcessor().add_data_to_file(data)


@router.delete("/file/delete_data")
async def delete_data():
    return {"message": "Dado removido com sucesso"}


@router.get("/file/list_files")
async def list_files():
    try:
        data = file_processor.list_data()  # Chama o método list_data
        return data  # Retorna os dados lidos do arquivo
    except HTTPException as e:
        raise e  # Repassa a exceção para o FastAPI
