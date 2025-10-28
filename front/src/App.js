import React from "react";
import { Provider } from "react-redux";
import { BrowserRouter as Router, Routes, Route, useParams } from "react-router-dom";
import { store } from "./store/store";
import Header from "./components/Header";
import MainPage from "./components/MainPage";
import Footer from "./components/Footer/Footer";
import "./App.css";

// Wrapper component to pass UID to MainPage
const MainPageWithUID = () => {
  const { uid } = useParams();
  return <MainPage uid={uid} />;
};

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <Header />
          <Routes>
            <Route path="/:uid" element={<MainPageWithUID />} />
            <Route path="/" element={<MainPage />} />
          </Routes>
          <Footer />
        </div>
      </Router>
    </Provider>
  );
}

export default App;
