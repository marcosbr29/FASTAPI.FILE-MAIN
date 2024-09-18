from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException, logger
from domain import file_processor
import logging

from domain.file_processor import FileProcessor

router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()


@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    return await FileProcessor().upload_file


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
        logger.info("Chamando list_data()")
        data = file_processor.list_data()  # Chama o método list_data
        logger.info("Dados lidos: %s", data)
        return data  # Retorna os dados lidos do arquivo
    except HTTPException as e:
        logger.error("HTTPException: %s", e.detail)
        raise e  # Repassa a exceção para o FastAPI
    except Exception as e:
        logger.error("Erro interno: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
