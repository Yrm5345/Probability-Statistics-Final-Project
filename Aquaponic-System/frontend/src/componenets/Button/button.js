import React from 'react';
import './button.css'; 

const PushButton = ({ label, onClick }) => {
  return (
    <button className="custom-button" onClick={onClick}>
      {label}
    </button>
  );
};

export default PushButton;
