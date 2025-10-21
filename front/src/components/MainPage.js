import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadPersonalityWords, clearError } from '../store/wordSelectionSlice';
import WordCheckbox from './WordCheckbox';
import './MainPage.css';

const MainPage = () => {
  const dispatch = useDispatch();
  const words = useSelector((state) => state.wordSelection.words);
  const selectedWords = useSelector((state) => state.wordSelection.selectedWords);
  const loading = useSelector((state) => state.wordSelection.loading);
  const error = useSelector((state) => state.wordSelection.error);

  useEffect(() => {
    if (words.length === 0 && !loading && !error) {
      dispatch(loadPersonalityWords());
    }
  }, [dispatch, words.length, loading, error]);

  // Organize words into 3 columns
  const wordsPerColumn = Math.ceil(words.length / 3);
  const column1 = words.slice(0, wordsPerColumn);
  const column2 = words.slice(wordsPerColumn, wordsPerColumn * 2);
  const column3 = words.slice(wordsPerColumn * 2);

  return (
    <div className="main-page">
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
          {loading && (
            <div className="loading-container">
              <div className="loading-spinner"></div>
              <p className="loading-text">Carregando palavras...</p>
            </div>
          )}
          
          {error && (
            <div className="error-container">
              <p className="error-text">Erro ao carregar palavras: {error}</p>
              <button 
                className="retry-button"
                onClick={() => dispatch(loadPersonalityWords())}
              >
                Tentar novamente
              </button>
            </div>
          )}
          
          {!loading && !error && words.length > 0 && (
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
