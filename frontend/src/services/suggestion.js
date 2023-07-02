import axios from './api';

export const submitSuggestion = async (suggestion) => {
  try {
    const response = await axios.post('/suggestions', suggestion);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getSuggestions = async () => {
  try {
    const response = await axios.get('/suggestions');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const updateSuggestion = async (suggestionId, suggestion) => {
  try {
    const response = await axios.put(`/suggestions/${suggestionId}`, suggestion);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const deleteSuggestion = async (suggestionId) => {
  try {
    const response = await axios.delete(`/suggestions/${suggestionId}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};