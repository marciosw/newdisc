import httpx
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class VFITService:
    """Service for interacting with VFIT API endpoints."""
    
    def __init__(self, base_url: str = "http://vfit.ouzaz.com.br", api_key: Optional[str] = "3022A778-74C4-4934-94EB-758D630862AA"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
        self.api_key = api_key
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
    
    async def salvar_teste_comportamental(
        self,
        dados_respondente: Dict[str, Any],
        codigo_campanha: str,
        ids_palavras: List[int]
    ) -> Dict[str, Any]:
        """
        Save behavioral test data to VFIT system.
        
        Args:
            dados_respondente: Respondent data dictionary
            codigo_campanha: Campaign code
            ids_palavras: List of word IDs
            api_key: Optional API key for authentication
            
        Returns:
            API response data
        """
        url = f"{self.base_url}/VFIT/SalvarTesteComportamental"
        if self.api_key:
            url += f"?api_key={self.api_key}"
        
        payload = {
            "dadosRespondente": dados_respondente,
            "codigoCampanha": codigo_campanha,
            "idsPalavras": ids_palavras
        }
        
        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            
            logger.info(f"Successfully saved behavioral test for campaign: {codigo_campanha}")
            return response.json()
            
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error saving behavioral test: {e.response.status_code} - {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Request error saving behavioral test: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error saving behavioral test: {e}")
            raise
    
    async def obter_resultado_teste(
        self,
        id_respondente: str
    ) -> Dict[str, Any]:
        """
        Get test result from VFIT system.
        
        Args:
            id_respondente: Respondent id returned by the VFIT system
            
        Returns:
            API response data with test results
        """
        url = f"{self.base_url}/VFIT/ObterResultadoTeste"
        
        payload = {
            "idRespondnete": id_respondente,
        }
        
        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            
            return response.json()
            
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error getting test result: {e.response.status_code} - {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Request error getting test result: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error getting test result: {e}")
            raise
    
    def create_respondent_data(
        self,
        nome: str,
        email: str,
        data_nascimento: Optional[datetime] = None,
        id_externo: Optional[str] = None,
        dados_adicionais: Optional[Dict[str, Any]] = None,
        inativo: bool = False
    ) -> Dict[str, Any]:
        """
        Helper method to create respondent data structure.
        
        Args:
            nome: Respondent name
            email: Respondent email
            data_nascimento: Birth date (optional)
            id_externo: External ID (optional)
            dados_adicionais: Additional data (optional)
            inativo: Whether respondent is inactive (default: False)
            
        Returns:
            Formatted respondent data dictionary
        """
        now = datetime.utcnow()
        
        return {
            "id": 0,
            "nome": nome,
            "dataInclusao": now.isoformat() + "Z",
            "dataNascimento": data_nascimento.isoformat() + "Z" if data_nascimento else now.isoformat() + "Z",
            "email": email,
            "idExterno": id_externo or "",
            "dadosAdicionais": dados_adicionais or {},
            "inativo": inativo
        }
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()


# Convenience functions for direct usage
async def salvar_teste_comportamental(
    dados_respondente: Dict[str, Any],
    codigo_campanha: str,
    ids_palavras: List[int],
    base_url: str = "http://vfit.ouzaz.com.br"
) -> Dict[str, Any]:
    """
    Convenience function to save behavioral test data.
    
    Args:
        dados_respondente: Respondent data dictionary
        codigo_campanha: Campaign code
        ids_palavras: List of word IDs
        base_url: VFIT API base URL
        api_key: Optional API key for authentication
        
    Returns:
        API response data
    """
    async with VFITService(base_url) as service:
        return await service.salvar_teste_comportamental(
            dados_respondente, codigo_campanha, ids_palavras
        )


async def obter_resultado_teste(
    id_respondente: str,
    base_url: str = "http://vfit.ouzaz.com.br"
) -> Dict[str, Any]:
    """
    Convenience function to get test result data.
    
    Args:
        id_respondente: Respondent ID returned by VFIT system
        base_url: VFIT API base URL
        
    Returns:
        API response data with test results
    """
    async with VFITService(base_url) as service:
        return await service.obter_resultado_teste(id_respondente)


# Example usage:
"""
# Using the service class
async with VFITService() as vfit:
    respondent_data = vfit.create_respondent_data(
        nome="João Silva",
        email="joao@example.com",
        data_nascimento=datetime(1990, 5, 15)
    )
    
    response = await vfit.salvar_teste_comportamental(
        dados_respondente=respondent_data,
        codigo_campanha="CAMP001",
        ids_palavras=[1, 2, 3, 4]
    )

# Using the convenience function
response = await salvar_teste_comportamental(
    dados_respondente=respondent_data,
    codigo_campanha="CAMP001",
    ids_palavras=[1, 2, 3, 4]
)
"""
