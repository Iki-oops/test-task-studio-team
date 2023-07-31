import { useState } from "react";
import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { Routes, Route } from 'react-router-dom';
import Topbar from "./scenes/global/TopBar";
import Dashboard from "./scenes/dashboard";
import Sidebar from "./scenes/global/Sidebar";
import HistoryMessages from "./scenes/historyMessages";

import './index.scss';
import AboutTeam from "./scenes/aboutTeam";
import FAQ from "./scenes/faq";
import ChangeCommand from "./scenes/changeCommand";


function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider as value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar isSidebar={isSidebar}/>
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar}/>
            <Routes>
              <Route path='/' element={<HistoryMessages />} />
              <Route path='/dashboard' element={<Dashboard />} />
              <Route path='/change-command' element={<ChangeCommand />} />
              <Route path='/about-team' element={<AboutTeam />} />
              <Route path='/faq' element={<FAQ/>} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  )
}

export default App;
