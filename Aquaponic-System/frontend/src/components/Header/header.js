import React from "react";
import ModernButton from "../Button/button";
import "./header.css";

const Header = () => {
  const handleButtonClick = () => {
    alert("Button clicked!");
  };
  return (
    <div className="header-container">
      <div className="header-content">
        <ModernButton label="Home" onClick={handleButtonClick} />
      </div>
      <div className="header-content">Smart Plants Watering System</div>
    </div>
  );
};

export default Header;
