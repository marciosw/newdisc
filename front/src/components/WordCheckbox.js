import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { toggleWord } from '../store/wordSelectionSlice';
import './WordCheckbox.css';

const WordCheckbox = ({ word }) => {
  const dispatch = useDispatch();
  const selectedWords = useSelector((state) => state.wordSelection.selectedWords);
  
  const isSelected = selectedWords.includes(word);
  
  const handleToggle = () => {
    dispatch(toggleWord(word));
  };

  return (
    <div className="word-checkbox-container">
      <label className="word-checkbox-label">
        <input
          type="checkbox"
          checked={isSelected}
          onChange={handleToggle}
          className="word-checkbox-input"
        />
        <span className="word-checkbox-text">{word}</span>
      </label>
    </div>
  );
};

export default WordCheckbox;
