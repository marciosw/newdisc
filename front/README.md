# Personality Assessment Web App

A React web application for personality assessment where users can select words that describe their personality traits. Built with React and Redux for state management.

## Features

- **Dark Theme Design**: Modern dark interface with gradient header background
- **Dynamic Word Loading**: Fetches personality words from API endpoint
- **Page-Based Layout**: Clean page layout with header, main content, and footer
- **Word Selection Interface**: Interactive word selection directly on the main page
- **Enhanced Header**: Logo, image placeholder, and mail icon in a three-column layout
- **Redux State Management**: Centralized state management for word selections
- **Loading States**: Loading spinner and error handling for API calls
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Selection Counter**: Shows number of selected words
- **Accessibility**: Proper focus management and keyboard navigation

## Technology Stack

- **React 18**: Frontend framework
- **Redux Toolkit**: State management
- **React Redux**: React bindings for Redux
- **CSS3**: Styling with modern features
- **Create React App**: Build tooling

## Project Structure

```
src/
├── components/
│   ├── Header.js              # Header component with logo, image, and mail icon
│   ├── Header.css
│   ├── MainPage.js            # Main page component with word selection
│   ├── MainPage.css
│   ├── WordCheckbox.js        # Individual word checkbox component
│   └── WordCheckbox.css
├── services/
│   └── api.js                 # API service for fetching personality words
├── store/
│   ├── store.js               # Redux store configuration
│   └── wordSelectionSlice.js  # Redux slice for word selection state
├── App.js                     # Main app component
├── App.css                    # Global styles
├── index.js                   # App entry point
└── index.css                  # Base styles
```

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Usage

1. The application opens with a clean page layout featuring a header with logo and image
2. The main content area displays Portuguese personality words in a three-column grid
3. Users can select multiple words by clicking on the checkboxes
4. The selection counter at the bottom shows how many words are selected
5. The interface is fully responsive and works on mobile devices
6. Loading states and error handling provide smooth user experience

## API Integration

The application fetches personality words from the following API endpoint:

- **URL**: `https://newdiscapi-181165400335.southamerica-east1.run.app/v1/ObterPalavras`
- **Method**: GET
- **Headers**: `X-API-Key: your_api_key`
- **Response Format**:
  ```json
  {
    "palavras": [
      {
        "id": "1427",
        "descricao": "Simpático"
      },
      {
        "id": "1428", 
        "descricao": "Cuidadoso"
      }
    ]
  }
  ```

### Environment Variables

Create a `.env` file in the root directory:
```
REACT_APP_API_KEY=your_actual_api_key
REACT_APP_API_BASE_URL=https://newdiscapi-181165400335.southamerica-east1.run.app/v1
```

## Redux State Structure

```javascript
{
  wordSelection: {
    words: [...],           // Array of word descriptions
    wordsData: [...],       // Array of full word objects with id and descricao
    selectedWords: [...],   // Array of currently selected words
    isModalOpen: true,      // Modal visibility state
    loading: false,         // API loading state
    error: null             // API error state
  }
}
```

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (one-way operation)

## Design Features

- **Header**: Gradient background with "Z Ouzaz" logo, image placeholder, and mail icon in three-column layout
- **Main Page**: Clean white content area with rounded corners and shadow
- **Word Grid**: Three-column layout for optimal word organization
- **Interactive Elements**: Hover effects and smooth transitions
- **Selection Summary**: Real-time counter showing selected words
- **Footer**: "BLACKBOX" branding in bottom-right corner

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is created for educational/demonstration purposes.
