from fastapi import APIRouter, HTTPException
import httpx
import uuid
from datetime import datetime
from ..services.firebase import get_firestore_client, get_firebase_auth_info
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

class Respondente(BaseModel):
    id_externo: str
    nome: str
    email: str
    telefone: str
    estado: str
    mensagem: str

class ResultadoEncaminhamento(BaseModel):
    id_externo: str
    id_respondente: str
    mensagem: str


router = APIRouter()


async def salvar_teste_firestore(teste_comportamental: TesteComportamental, resultado):
    try:
        db = get_firestore_client()
        collection_ref = db.collection("testes_comportamentais")
        uid = uuid.uuid4()
        collection_ref.document(str(uid)).set({
            "id": str(uid),
            "dados_respondente": teste_comportamental.dados_respondente,
            "codigo_campanha": teste_comportamental.codigo_campanha,
            "ids_palavras": teste_comportamental.ids_palavras,
            "resultado": resultado["resultadoTesteVocacional"],
            "data_teste": datetime.now()
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving respondente to Firestore: {str(e)}")

@router.get("/external-example")
async def external_example():
    async with httpx.AsyncClient(timeout=10.0) as client:
        # Simple example hitting a public API
        resp = await client.get("https://api.github.com/rate_limit")
    return {"status_code": resp.status_code, "data": resp.json()}


@router.get("/firebase-auth-info")
async def get_firebase_auth_info_endpoint():
    """
    Get detailed information about the Firebase authentication account being used.
    """
    try:
        auth_info = get_firebase_auth_info()
        return auth_info
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting Firebase auth info: {str(e)}")


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

@router.post("/encaminhar")
async def encaminhar(respondente: Respondente):
    """
    Save a respondente to Firestore and return the result.
    """
    try:
        # Get Firestore client
        db = get_firestore_client()
        
        # Print Firebase authentication information
        auth_info = get_firebase_auth_info()
        print("=== Firebase Authentication Info ===")
        print(f"Service Account Email: {auth_info.get('service_account', {}).get('client_email', 'N/A')}")
        print(f"Project ID: {auth_info.get('firebase_app', {}).get('project_id', 'N/A')}")
        print(f"Credentials Source: {auth_info.get('configuration', {}).get('credentials_source', 'N/A')}")
        print("=====================================")
        
        collection_ref = db.collection("respondentes")
        print("Collection reference created")
        uid = uuid.uuid4()
        print(f"Generated UID: {uid}")
        collection_ref.document(str(uid)).set({
            "id": str(uid),
            "id_externo": respondente.id_externo,
            "nome": respondente.nome,
            "email": respondente.email,
            "telefone": respondente.telefone,
            "estado": respondente.estado,
            "mensagem": respondente.mensagem,
            "data_encaminhamento": datetime.now()
        }, merge=True)
        print("Document saved successfully")
        # return ResultadoEncaminhamento
        return ResultadoEncaminhamento(
            id_externo=respondente.id_externo,
            id_respondente=str(uid),
            mensagem="Respondente encaminhado com sucesso"
        )
        
    except Exception as e:
        print(f"Error encaminhando respondente: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error reading from Firestore: {str(e)}")


#Buscar respondente por id_externo
@router.get("/BuscarRespondente/{id_externo}")
async def buscar_respondente(id_externo: str):
    """
    Buscar respondente por id_externo
    """
    try:
        db = get_firestore_client()
        collection_ref = db.collection("respondentes")
        doc_ref = collection_ref.document(id_externo)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading from Firestore: {str(e)}")

#Buscar respondente por id
@router.get("/BuscarRespondente/{id}")
async def buscar_respondente(id: str):
    """
    Buscar respondente por id
    """
    try:
        db = get_firestore_client()
        collection_ref = db.collection("respondentes")
        doc_ref = collection_ref.document(id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading from Firestore: {str(e)}")

#Buscar respondente por email
@router.get("/BuscarRespondenteByEmail/{email}")
async def buscar_respondente_by_email(email: str):
    """
    Buscar respondente por email
    """
    try:
        db = get_firestore_client()
        collection_ref = db.collection("respondentes")
        docs = collection_ref.where("email", "==", email).get()
        if docs:
            return docs[0].to_dict()
        else:
            return None
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
        retSalvar = await vfit_salvar_teste(
            dados_respondente=teste_comportamental.dados_respondente,
            codigo_campanha=teste_comportamental.codigo_campanha,
            ids_palavras=teste_comportamental.ids_palavras
        )        
        resultado = await obter_resultado_teste(retSalvar["dadosRespondente"]["id"])
        await salvar_teste_firestore(teste_comportamental, resultado)
        return resultado
        
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
