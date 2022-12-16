import React from "react";
import {Link} from 'react-router-dom';


const Navbar =() => {

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="conteiner-fluid">
                <a className="navbar-brand" to='#/'>
                    HEROES | ISP | REACT + Django
                </a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="nav">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <Link className="nav-link" to='/'>
                                Home
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to='/heroe-form'>
                                Add Heroe
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to='/heroes-list'>
                                List Heroes
                            </Link>
                        </li>
                    </ul>

                </div>

            </div>
        </nav>
    )
};

export default Navbar;
