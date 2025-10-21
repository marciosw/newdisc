import { configureStore } from '@reduxjs/toolkit';
import wordSelectionReducer from './wordSelectionSlice';

export const store = configureStore({
  reducer: {
    wordSelection: wordSelectionReducer,
  },
});

export default store;
