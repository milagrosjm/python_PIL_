import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter, Route, Routes} from 'react-router-dom'

import HeroesForm from './components/heroes/HeroesForm'
import Navbar from './components/navbar/Navbar'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <>
    <BrowserRouter>
      <Navbar></Navbar>
        <div className='conteiner my-4'>
          <Routes>
            <Route exact path='/' element={<App/>}/>
            <Route path='/heroe-form' element={<HeroesForm/>}/>
          </Routes>
        </div>
    </BrowserRouter>
  </>
  
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
