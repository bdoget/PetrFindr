import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router";
import Dashboard from "./Dashboard";
import HomePage from "./pages/HomePage";
import BioPage from "./pages/BioPage";
import { ThemeProvider } from "@emotion/react";
import theme from "./theme"
import ImageSubmitPage from "./pages/ImageSubmitPage";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <ThemeProvider theme={theme}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />

        <Route path="/project" element={<ImageSubmitPage />}>

          {/* <Route index element={<Home />} /> */}
          {/* <Route path="settings" element={<Settings />} /> */}
        </Route>

        <Route path="/team-bio" element={<BioPage/>}>
        </Route>

      </Routes>
    </BrowserRouter>
  </ThemeProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
