import React, { useState } from 'react';
import { submitResolution } from '../services/resolution';

const Superuser = () => {
  const [resolution, setResolution] = useState('');

  const handleInputChange = (event) => {
    setResolution(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await submitResolution(resolution);
    if (response.status === 200) {
      alert('Resolution submitted successfully');
      setResolution('');
    } else {
      alert('Error submitting resolution');
    }
  };

  return (
    <div>
      <h2>Superuser Panel</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="superuser-text-input">Paste Draft Resolution:</label>
        <textarea
          id="superuser-text-input"
          value={resolution}
          onChange={handleInputChange}
          rows="10"
          cols="50"
        />
        <button type="submit">Submit Resolution</button>
      </form>
    </div>
  );
};

export default Superuser;