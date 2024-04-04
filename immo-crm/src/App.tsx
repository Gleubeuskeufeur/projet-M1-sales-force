import React from 'react';
import logo from './logo.svg';
import './App.css';
import MainPage from './pages/main_page';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to the Estate-CRM, Select a City to look for Real Estate Prices
        </p>
        <MainPage />
      </header>
    </div>
  );
}

export default App;
