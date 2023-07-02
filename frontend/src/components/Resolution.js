import React, { useState, useEffect } from 'react';
import { getResolution, submitResolution } from '../services/resolution';

const Resolution = () => {
  const [resolution, setResolution] = useState('');
  const [newResolution, setNewResolution] = useState('');

  useEffect(() => {
    fetchResolution();
  }, []);

  const fetchResolution = async () => {
    const res = await getResolution();
    setResolution(res.data);
  };

  const handleResolutionChange = (event) => {
    setNewResolution(event.target.value);
  };

  const handleResolutionSubmit = async () => {
    await submitResolution(newResolution);
    setNewResolution('');
    fetchResolution();
  };

  return (
    <div>
      <h2>Current Resolution</h2>
      <p id="resolution-display">{resolution}</p>
      <h2>Submit New Resolution</h2>
      <textarea
        id="superuser-text-input"
        value={newResolution}
        onChange={handleResolutionChange}
      />
      <button onClick={handleResolutionSubmit}>Submit</button>
    </div>
  );
};

export default Resolution;