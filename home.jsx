import React, { useState } from 'react';
import './HomeScreen.css'; // Import styles for this component

const HomeScreen = () => {
  const [location, setLocation] = useState('');

  const fetchCurrentLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setLocation(`Lat: ${latitude}, Lon: ${longitude}`);
        },
        (error) => {
          console.error('Error fetching location:', error);
        }
      );
    } else {
      alert('Geolocation is not supported by your browser.');
    }
  };

  return (
    <div className="home-screen">
      {/* Header Section */}
      <header className="header">
        <img src="/logo.png" alt="Logo" className="logo" />
        <h2 className="tagline">Find events and activities you’ll love!</h2>
      </header>

      {/* Search Bar */}
      <div className="search-bar">
        <input type="text" placeholder="What are you looking for?" className="search-input" />
        <button className="voice-search">
          <span role="img" aria-label="Microphone">🎤</span>
        </button>
      </div>

      {/* Suggested Categories */}
      <div className="categories">
        <h3>Explore Categories</h3>
        <div className="scrollable">
          <button className="category">🎵 Music</button>
          <button className="category">🎨 Art</button>
          <button className="category">🌳 Outdoor</button>
          <button className="category">📚 Workshops</button>
        </div>
      </div>

      {/* Current Location Prompt */}
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

      {/* Upcoming Events Section */}
      <div className="upcoming-events">
        <h3>Upcoming Events</h3>
        <div className="events-grid">
          <div className="event-card">
            <img src="/event1.jpg" alt="Event 1" className="event-image" />
            <h4 className="event-title">Kynnovate 2025</h4>
            <p className="event-details">Date: 25th December | Online</p>
            <button className="learn-more">Learn More</button>
          </div>

          <div className="event-card">
            <img src="/event2.jpg" alt="Event 2" className="event-image" />
            <h4 className="event-title">Art Festival 2025</h4>
            <p className="event-details">Date: 10th January | New York</p>
            <button className="learn-more">Learn More</button>
          </div>

          {/* Add more cards as needed */}
        </div>
      </div>
    </div>
  );
};

export default HomeScreen;
