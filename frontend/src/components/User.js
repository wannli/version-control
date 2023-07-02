import React, { useState } from 'react';
import { submitSuggestion } from '../services/suggestion';

const User = () => {
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
      <h2>User</h2>
      <form onSubmit={handleSuggestionSubmit}>
        <label>
          Suggestion:
          <textarea value={suggestion} onChange={handleSuggestionChange} />
        </label>
        <button type="submit">Submit Suggestion</button>
      </form>
    </div>
  );
};

export default User;