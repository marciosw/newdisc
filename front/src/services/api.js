const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'https://newdiscapi-181165400335.southamerica-east1.run.app/v1';
const API_KEY = process.env.REACT_APP_API_KEY || 'your_api_key';

export const fetchPersonalityWords = async () => {
  try {
    console.log(`APIKEY: ${API_KEY}`);
    console.log(`API_BASE_URL: ${API_BASE_URL}`);
    
    // Try direct request first, then fallback to proxy if CORS fails
    let response;
    try {
      response = await fetch(`${API_BASE_URL}/ObterPalavras`, {
        method: 'GET',
        headers: {
          'X-API-Key': API_KEY,
          'Accept': 'application/json',
        },
      });
    } catch (corsError) {
      console.log('CORS error, trying with proxy...', corsError);
      // Fallback to CORS proxy
      const proxyUrl = 'https://api.allorigins.win/raw?url=';
      const targetUrl = encodeURIComponent(`${API_BASE_URL}/ObterPalavras`);
      response = await fetch(`${proxyUrl}${targetUrl}`, {
        method: 'GET',
        headers: {
          'X-API-Key': API_KEY,
          'Accept': 'application/json',
        },
      });
    }

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.palavras || [];
  } catch (error) {
    console.error('Error fetching personality words:', error);
    throw error;
  }
};
