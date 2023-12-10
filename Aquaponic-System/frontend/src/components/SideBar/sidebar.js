import React, { useState } from "react";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faTint,
  faClock,
  faChartLine,
  faSeedling,
  faBell,
  faSun,
  faCogs,
  faQuestionCircle,
  faBars,
  faUser,
  faSignOutAlt,
} from "@fortawesome/free-solid-svg-icons";
import "./sidebar.css";

const SideBar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  return (
    <div className={`sidebar ${isMenuOpen ? "open" : ""}`}>
      <div className="menu-items">
        <Link
          to="/profile"
          style={{ fontSize: "24px", display: "block", textAlign: "center" }}
        >
          <FontAwesomeIcon icon={faUser} />
        </Link>

        <Link to="/home">
          <FontAwesomeIcon icon={faTint} style={{ marginRight: "8px" }} />
          Home
        </Link>
        <Link to="/water-now">
          <FontAwesomeIcon icon={faTint} style={{ marginRight: "8px" }} />
          Water Now
        </Link>
        <Link to="/set-schedule">
          <FontAwesomeIcon icon={faClock} style={{ marginRight: "8px" }} />
          Set Schedule
        </Link>
        <Link to="/view-stats">
          <FontAwesomeIcon icon={faChartLine} style={{ marginRight: "8px" }} />
          View Stats
        </Link>
        <Link to="/add-plant">
          <FontAwesomeIcon icon={faSeedling} style={{ marginRight: "8px" }} />
          Add Plant
        </Link>
        <Link to="/notifications">
          <FontAwesomeIcon icon={faBell} style={{ marginRight: "8px" }} />
          Notifications
        </Link>
        <Link to="/weather-forecast">
          <FontAwesomeIcon icon={faSun} style={{ marginRight: "8px" }} />
          Weather Forecast
        </Link>
        <Link to="/settings">
          <FontAwesomeIcon icon={faCogs} style={{ marginRight: "8px" }} />
          Settings
        </Link>
        <Link to="/help">
          <FontAwesomeIcon
            icon={faQuestionCircle}
            style={{ marginRight: "8px" }}
          />
          Help
        </Link>
        <Link to="/sign-out">
          <FontAwesomeIcon icon={faSignOutAlt} style={{ marginRight: "8px" }} />
          Sign Out
        </Link>
      </div>
    </div>
  );
};

export default SideBar;
