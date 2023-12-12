import React, { useState } from "react";
import "./SetSchedule.css";

const SetSchedule = () => {
  const [startDate, setstartDate] = useState("");
  const [startTime, setstartTime] = useState("");
  const [endDate, setendDate] = useState("");
  const [endTime, setendTime] = useState("");

  const handleSetSchedule = () => {
    console.log("Schedule set:", { startDate, startTime, endDate, endTime });
  };

  return (
    <div className="set-schedule-container">
      <h2>Set Schedule</h2>
      <form>
        <label>Start Date (DDMMYYYY):</label>
        <input
          type="text"
          value={startDate}
          onChange={(e) => setstartDate(e.target.value)}
          required
        />

        <label>Start Time (HHMM):</label>
        <input
          type="text"
          value={startTime}
          onChange={(e) => setstartTime(e.target.value)}
          required
        />

        <label>End Date (DDMMYYYY):</label>
        <input
          type="text"
          value={endDate}
          onChange={(e) => setendDate(e.target.value)}
          required
        />

        <label>End Time (HHMM):</label>
        <input
          type="text"
          value={endTime}
          onChange={(e) => setendTime(e.target.value)}
          required
        />

        <button type="button" onClick={handleSetSchedule}>
          Set Schedule
        </button>
      </form>
    </div>
  );
};

export default SetSchedule;
