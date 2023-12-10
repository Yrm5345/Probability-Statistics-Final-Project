// App.js
import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Header from "./components/Header/header";
import Home from "./components/Home/home";
import SideBar from "./components/SideBar/sidebar";
import SignInForm from "./components/Auth/signin";
import SignUpForm from "./components/Auth/signup";
import "./App.css";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <div className="full-container">
              <div className="App">
                <div className="menu-container">
                  <SideBar />
                </div>
                <div className="main-container">
                  <Header />
                  <Home />
                </div>
              </div>
            </div>
          }
        />
        <Route path="/sign-out" element={<SignInForm />} />
        <Route path="/sign-up" element={<SignUpForm />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
};

export default App;
