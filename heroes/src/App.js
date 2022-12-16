import logo from './logo.svg';
import './App.css';
import Heroe from './components/heroes/HeroesForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <Heroe></Heroe>
    </div>
  );
}

export default App;
