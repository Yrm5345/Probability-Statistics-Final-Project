import React from "react";
import "./button.css";

const ModernButton = ({ label, onClick }) => {
  return (
    <button className="modern-button" onClick={onClick}>
      {label}
    </button>
  );
};

export default ModernButton;
