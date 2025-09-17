import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './SplashScreen.css';

const SplashScreen = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Navigate to login after 3 seconds
    const timer = setTimeout(() => {
      navigate('/'); // assuming '/' is login
    }, 3000);

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="splash-container">
      <h1 className="app-title">ToDoFlix</h1>
      <p className="tagline">Your tasks, your way.</p>
      <button className="get-started-btn" onClick={() => navigate('/login')}>
        Get Started
      </button>
    </div>
  );
};

export default SplashScreen;
