import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchPersonalityWords } from '../services/api';

// Async thunk for fetching personality words
export const loadPersonalityWords = createAsyncThunk(
  'wordSelection/loadPersonalityWords',
  async (_, { rejectWithValue }) => {
    try {
      const words = await fetchPersonalityWords();
      return words;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const initialState = {
  words: [],
  wordsData: [], // Store the full word objects with id and descricao
  selectedWords: [],
  loading: false,
  error: null
};

const wordSelectionSlice = createSlice({
  name: 'wordSelection',
  initialState,
  reducers: {
    toggleWord: (state, action) => {
      const word = action.payload;
      const index = state.selectedWords.indexOf(word);
      
      if (index > -1) {
        // Remove word if already selected
        state.selectedWords.splice(index, 1);
      } else {
        // Add word if not selected
        state.selectedWords.push(word);
      }
    },
    clearSelection: (state) => {
      state.selectedWords = [];
    },
    clearError: (state) => {
      state.error = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(loadPersonalityWords.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loadPersonalityWords.fulfilled, (state, action) => {
        state.loading = false;
        state.wordsData = action.payload;
        state.words = action.payload.map(word => word.descricao);
        state.error = null;
      })
      .addCase(loadPersonalityWords.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});

export const { toggleWord, clearSelection, clearError } = wordSelectionSlice.actions;
export default wordSelectionSlice.reducer;
