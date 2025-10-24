import React from "react";
import { Provider } from "react-redux";
import { store } from "./store/store";
import Header from "./components/Header";
import MainPage from "./components/MainPage";
import Footer from "./components/Footer/Footer";
import "./App.css";

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <Header />
        <MainPage />
        <Footer />
      </div>
    </Provider>
  );
}

export default App;
