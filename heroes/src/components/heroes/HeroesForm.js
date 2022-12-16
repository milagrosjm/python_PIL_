import React, {useState, useEffect} from "react";
import {useParams, useNavigate} from 'react-router-dom'
import * as HeroesServer from './HeroesServer';

import Select from 'react-select';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap'

const Heroe = () => {
    const history = useNavigate();
    const params = useParams();

const initialState = {
    id: 0,
    nombre: '',
    identidad_secreta: '',
    edad: 0,
    universo: 0,
}

const [heroe, setHeroe] = useState(initialState);

const getHeroe = async () => {
    try {
        //request a la API
        const res = await HeroesServer.getHeroe();
        //transformo a json
        const data = await res.json();
        //guardo los datos en un diccionario
        const {id, nombre, edad, universo} = data.heroe;
        //seteo el heroe
        setHeroe({id, nombre, edad, universo});
    }
    catch(error){
        console.log(error)

    }
}

const handleInputChange = (e) => {
    setHeroe({...heroe,[e.target.name]: e.target.value})
}

const handleInputSelectUniverso = (e) => {
    setHeroe({...heroe, universo: e.value})
}

var res;
const handleSubmit = async(e) =>{
    console.log("Handle submit:", heroe.id)
    e.preventDefault();
    try{
        if (!params.id){
            console.log("Id no existe");
            res = await HeroesServer.registerHeroe(heroe);
            console.log("Res:", res);
            const data = await res.json();
            console.log("Data:", data);
            if (data.id !=0){
                console.log("Id es != de 0");
                setHeroe(initialState);
            }
        }
        else{
            res = await HeroesServer.updateHeroe(params.id, heroe);
        }
        history("/")
    }
    catch(error){
            console.log(error);
        }
    }


useEffect(() => {
    if (params.id){
        getHeroe(params.id);
    }
 }, []);

const options_universe = [
    {value: '1', label: 'MARVEL'},
    {value: '2', label: 'DC'}
]

return(
    <div className='col-md-10 mx-auto'>
        <div className="col-md-12 mx-auto">
            <h2 className='mb-12 text-center'>Heroe</h2>
            <form onSubmit={handleSubmit}>
                <div className='row'>
                    <div className="mb-8">
                        <label className="form-label col-12" htmlFor='nombre'>Nombre</label>
                        <input className='form-control' type="text" name="nombre" id="nombre" value={heroe.nombre} onChange={handleInputChange}></input>
                    </div>
                </div>
                <div className='row'>
                    <div className="mb-8">
                        <label className="form-label col-12" htmlFor='identidad_secreta'>Identidad Secreta</label>
                        <input className='form-control' type="text" name="identidad_secreta" id="identidad_secreta" value={heroe.identidad_secreta} onChange={handleInputChange}></input>   
                    </div>
                </div>
                <div className='row'>
                    <div className="mb-6">
                        <label className="form-label col-12" htmlFor='edad'>Edad</label>
                        <input className='form-control' type="number" name="edad" id="edad" value={heroe.edad} onChange={handleInputChange}></input>   
                        <div className="mb-6">
                            <label className="form-label" htmlFor="universo"> Universo</label>
                            <Select id="universo" name="universso" className="form-control"
                            onChange={handleInputSelectUniverso} classNamePrefix="my-react-select" options={options_universe}/>
                        </div>
                    </div>
                </div>
                <br>
                </br>
                <div className="row">
                    <p>
                        {res}
                    </p>
                </div>
                <div className="row">
                    <div className="d-grid ???">

                    </div>

                </div>
            </form>
        </div>
    </div>
);
};

export default Heroe;

