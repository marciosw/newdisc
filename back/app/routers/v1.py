from fastapi import APIRouter, HTTPException
import httpx
from ..services.firebase import get_firestore_client
from ..services.discsite import salvar_teste_comportamental as vfit_salvar_teste, obter_resultado_teste as vfit_obter_resultado
from pydantic import BaseModel

class TesteComportamental(BaseModel):
    dados_respondente: dict
    codigo_campanha: str
    ids_palavras: list

class ResultadoTeste(BaseModel):
    dados_respondente: dict
    codigo_campanha: str
    ids_palavras: list
    resultado: dict

router = APIRouter()


@router.get("/external-example")
async def external_example():
    async with httpx.AsyncClient(timeout=10.0) as client:
        # Simple example hitting a public API
        resp = await client.get("https://api.github.com/rate_limit")
    return {"status_code": resp.status_code, "data": resp.json()}


@router.get("/ObterPalavras")
async def obter_palavras():
    """
    Read the 'palavras' collection from Firestore and return all documents as an array.
    """
    try:
        # Get Firestore client
        db = get_firestore_client()
        
        # Reference to the palavras collection
        collection_ref = db.collection("palavras")
        
        # Get all documents from the collection
        docs = collection_ref.stream()
        
        # Convert documents to list of dictionaries
        palavras = []
        for doc in docs:
            palavra_data = doc.to_dict()
            # Add document ID to the data
            palavra_data["id"] = doc.id
            palavras.append(palavra_data)
        
        return {"palavras": palavras}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading from Firestore: {str(e)}")




@router.post("/SalvarTesteComportamental")
async def salvar_teste_comportamental(
    teste_comportamental: TesteComportamental
):
    """
    Save a teste comportamental to VFIT system.
    """
    try:
        # Call VFIT service
        result = await vfit_salvar_teste(
            dados_respondente=teste_comportamental.dados_respondente,
            codigo_campanha=teste_comportamental.codigo_campanha,
            ids_palavras=teste_comportamental.ids_palavras
        )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving to VFIT: {str(e)}")


@router.get("/ObterResultadoTeste/{id_respondente}")
async def obter_resultado_teste(
    id_respondente: str
):
    """
    Get test result from VFIT system.
    """
    try:
        # Call VFIT service
        print(f"id_respondente: {id_respondente}")
        result = await vfit_obter_resultado(
            id_respondente=id_respondente
        )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting result from VFIT: {str(e)}")
