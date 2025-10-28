import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchRespondentData } from '../services/api';

// Async thunk for fetching respondent data
export const loadRespondentData = createAsyncThunk(
  'respondent/loadRespondentData',
  async (uid, { rejectWithValue }) => {
    try {
      const data = await fetchRespondentData(uid);
      return data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const initialState = {
  data: null,
  loading: false,
  error: null
};

const respondentSlice = createSlice({
  name: 'respondent',
  initialState,
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
    clearData: (state) => {
      state.data = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(loadRespondentData.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loadRespondentData.fulfilled, (state, action) => {
        state.loading = false;
        state.data = action.payload;
        state.error = null;
      })
      .addCase(loadRespondentData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});

export const { clearError, clearData } = respondentSlice.actions;
export default respondentSlice.reducer;
