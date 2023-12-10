import React, { useState } from "react";
import "./AddPlant.css";

const AddPlant = () => {
  const [plantName, setPlantName] = useState("");
  const [plantType, setPlantType] = useState("");

  const handleAddPlant = () => {
    console.log("Plant added:", { plantName, plantType });
  };

  return (
    <div className="add-plant-container">
      <h2>Add Plant</h2>
      <form>
        <label>Plant Name:</label>
        <input
          type="text"
          value={plantName}
          onChange={(e) => setPlantName(e.target.value)}
          required
        />

        <label>Plant Type:</label>
        <input
          type="text"
          value={plantType}
          onChange={(e) => setPlantType(e.target.value)}
          required
        />

        <button type="button" onClick={handleAddPlant}>
          Add Plant
        </button>
      </form>
    </div>
  );
};

export default AddPlant;
