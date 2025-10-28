import { configureStore } from '@reduxjs/toolkit';
import wordSelectionReducer from './wordSelectionSlice';
import respondentReducer from './respondentSlice';

export const store = configureStore({
  reducer: {
    wordSelection: wordSelectionReducer,
    respondent: respondentReducer,
  },
});

export default store;
