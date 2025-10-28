import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadPersonalityWords } from '../store/wordSelectionSlice';
import { loadRespondentData } from '../store/respondentSlice';
import WordCheckbox from './WordCheckbox';
import './MainPage.css';

const MainPage = ({ uid }) => {
  const dispatch = useDispatch();
  const words = useSelector((state) => state.wordSelection.words);
  const selectedWords = useSelector((state) => state.wordSelection.selectedWords);
  const loading = useSelector((state) => state.wordSelection.loading);
  const error = useSelector((state) => state.wordSelection.error);
  
  // Respondent data
  const respondentData = useSelector((state) => state.respondent.data);
  const respondentLoading = useSelector((state) => state.respondent.loading);
  const respondentError = useSelector((state) => state.respondent.error);

  useEffect(() => {
    if (words.length === 0 && !loading && !error) {
      dispatch(loadPersonalityWords());
    }
  }, [dispatch, words.length, loading, error]);

  // Load respondent data when UID is provided
  useEffect(() => {
    if (uid && !respondentData && !respondentLoading && !respondentError) {
      dispatch(loadRespondentData(uid));
    }
  }, [uid, dispatch, respondentData, respondentLoading, respondentError]);

  // Organize words into 3 columns
  const wordsPerColumn = Math.ceil(words.length / 3);
  const column1 = words.slice(0, wordsPerColumn);
  const column2 = words.slice(wordsPerColumn, wordsPerColumn * 2);
  const column3 = words.slice(wordsPerColumn * 2);

  return (
    <div className="main-page">
      {/* Hidden inputs for respondent data */}
      {respondentData && (
        <form style={{ display: 'none' }}>
          <input type="hidden" name="email" value={respondentData.email || ''} />
          <input type="hidden" name="telefone" value={respondentData.telefone || ''} />
          <input type="hidden" name="nome" value={respondentData.nome || ''} />
          <input type="hidden" name="id" value={respondentData.id || ''} />
          <input type="hidden" name="data_encaminhamento" value={respondentData.data_encaminhamento || ''} />
          <input type="hidden" name="estado" value={respondentData.estado || ''} />
          <input type="hidden" name="id_externo" value={respondentData.id_externo || ''} />
          <input type="hidden" name="mensagem" value={respondentData.mensagem || ''} />
        </form>
      )}

      <div className="page-content">
        <div className="page-header">
          <h1 className="page-title">
            Escolha as palavras com as quais você se identifica
          </h1>
          <p className="page-subtitle">
            Não há um limite de palavras, escolha quantas você quiser.
          </p>
        </div>
        
        <div className="words-section">
          {(loading || respondentLoading) && (
            <div className="loading-container">
              <div className="loading-spinner"></div>
              <p className="loading-text">
                {loading ? 'Carregando palavras...' : 'Carregando dados do respondente...'}
              </p>
            </div>
          )}
          
          {(error || respondentError) && (
            <div className="error-container">
              <p className="error-text">
                {error ? `Erro ao carregar palavras: ${error}` : `Erro ao carregar dados do respondente: ${respondentError}`}
              </p>
              <button 
                className="retry-button"
                onClick={() => {
                  if (error) {
                    dispatch(loadPersonalityWords());
                  } else if (respondentError && uid) {
                    dispatch(loadRespondentData(uid));
                  }
                }}
              >
                Tentar novamente
              </button>
            </div>
          )}
          
          {!loading && !error && !respondentLoading && !respondentError && words.length > 0 && (
            <div className="words-grid">
              <div className="words-column">
                {column1.map((word) => (
                  <WordCheckbox key={word} word={word} />
                ))}
              </div>
              <div className="words-column">
                {column2.map((word) => (
                  <WordCheckbox key={word} word={word} />
                ))}
              </div>
              <div className="words-column">
                {column3.map((word) => (
                  <WordCheckbox key={word} word={word} />
                ))}
              </div>
            </div>
          )}
        </div>
        
        <div className="selection-summary">
          <div className="selected-count">
            {selectedWords.length} palavra{selectedWords.length !== 1 ? 's' : ''} selecionada{selectedWords.length !== 1 ? 's' : ''}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainPage;
