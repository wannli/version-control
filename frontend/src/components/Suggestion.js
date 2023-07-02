import React, { useState } from 'react';
import { submitSuggestion } from '../services/suggestion';

const Suggestion = () => {
  const [suggestion, setSuggestion] = useState('');

  const handleSuggestionChange = (event) => {
    setSuggestion(event.target.value);
  };

  const handleSuggestionSubmit = async (event) => {
    event.preventDefault();
    const response = await submitSuggestion(suggestion);
    if (response.status === 200) {
      alert('Suggestion submitted successfully');
      setSuggestion('');
    } else {
      alert('Failed to submit suggestion');
    }
  };

  return (
    <div>
      <h2>Make a Suggestion</h2>
      <form onSubmit={handleSuggestionSubmit}>
        <textarea
          id="user-suggestion-input"
          value={suggestion}
          onChange={handleSuggestionChange}
          placeholder="Enter your suggestion here"
        />
        <button type="submit">Submit Suggestion</button>
      </form>
    </div>
  );
};

export default Suggestion;