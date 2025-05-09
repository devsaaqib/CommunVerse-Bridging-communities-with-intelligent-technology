<div className="location-prompt">
  <button onClick={fetchCurrentLocation} className="location-button">
    Use My Location
  </button>
  <input
    type="text"
    placeholder="Enter location manually"
    value={location}
    onChange={(e) => setLocation(e.target.value)}
    className="location-input"
  />
</div>
