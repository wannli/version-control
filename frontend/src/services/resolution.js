import axios from './api';

export const getLatestResolution = async () => {
  try {
    const response = await axios.get('/resolutions/latest');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const submitResolution = async (resolutionText) => {
  try {
    const response = await axios.post('/resolutions', { text: resolutionText });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};