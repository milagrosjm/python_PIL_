// Conexion con la API
const API_URL = 'url'

export const getHeroe = async () => {
    return await fetch(API_URL);
}

export const traerHeroe = [
    {
        id: 1,
        nombre: 'BATMAN',
        edad: '45',
        universo: 2,
    }
];

export const registerHeroe = async (newHeroe) =>{
    console.log(newHeroe);
    return await fetch(API_URL,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'no-cors',
        body: JSON.stringify({
            "name": String(newHeroe.nombre).trim(),
            "secret_identity": String(newHeroe.identidad_secreta).trim(),
            "age": Number(newHeroe.edad),
            "universe": Number(newHeroe.universo)
        })
    });
};

export const updateHeroe = async (heroe) => {
    return await fetch(API_URL,{
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "name": String(heroe.nombre).trim(),
            "secret_identity": String(heroe.identidad_secreta).trim(),
            "age": Number(heroe.edad),
            "universe": Number(heroe.universo) 
        })
    });
}

export const listHeroes = async () => {
    return await fetch(API_URL);
}

export const deleteHeroe = async () => {
    return await fetch(API_URL);
}

export const createHeroe = async () => {
    return await fetch(API_URL);
}