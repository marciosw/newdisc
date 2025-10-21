import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-background">
        <div className="header-content">
          <div className="header-left">
            <div className="logo">
              <span className="logo-text">Z Ouzaz</span>
            </div>
          </div>
          <div className="header-center">
            <div className="header-image">
              <div className="image-placeholder">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2" stroke="white" strokeWidth="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5" stroke="white" strokeWidth="2"/>
                  <polyline points="21,15 16,10 5,21" stroke="white" strokeWidth="2"/>
                </svg>
              </div>
            </div>
          </div>
          <div className="header-actions">
            <button className="mail-button">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 4H20C21.1 4 22 4.9 22 6V18C22 19.1 21.1 20 20 20H4C2.9 20 2 19.1 2 18V6C2 4.9 2.9 4 4 4Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <polyline points="22,6 12,13 2,6" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
