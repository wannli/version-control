import React, { useState, useEffect } from 'react';
import Superuser from './components/Superuser';
import User from './components/User';
import Resolution from './components/Resolution';
import Suggestion from './components/Suggestion';
import { getResolution, getSuggestions } from './services/resolution';
import { RESOLUTION_SUBMITTED, SUGGESTION_SUBMITTED, SUGGESTION_ACCEPTED, SUGGESTION_REJECTED } from './services/messages';

function App() {
  const [resolution, setResolution] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    fetchResolution();
    fetchSuggestions();
  }, []);

  const fetchResolution = async () => {
    const response = await getResolution();
    setResolution(response.data);
  };

  const fetchSuggestions = async () => {
    const response = await getSuggestions();
    setSuggestions(response.data);
  };

  const handleResolutionSubmit = (newResolution) => {
    setResolution(newResolution);
  };

  const handleSuggestionSubmit = (newSuggestion) => {
    setSuggestions([...suggestions, newSuggestion]);
  };

  const handleSuggestionAccept = (acceptedSuggestion) => {
    setResolution(acceptedSuggestion);
    setSuggestions(suggestions.filter(suggestion => suggestion !== acceptedSuggestion));
  };

  const handleSuggestionReject = (rejectedSuggestion) => {
    setSuggestions(suggestions.filter(suggestion => suggestion !== rejectedSuggestion));
  };

  return (
    <div className="App">
      <Superuser onSubmit={handleResolutionSubmit} />
      <Resolution resolution={resolution} />
      <User onSubmit={handleSuggestionSubmit} />
      <Suggestion suggestions={suggestions} onAccept={handleSuggestionAccept} onReject={handleSuggestionReject} />
    </div>
  );
}

export default App;