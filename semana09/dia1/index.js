//Importamos la libreria EXPRESS
const express = require("express");

// Se va a copia toda la funcionalidad de la liberia express en la varibale servidor
const servidor = express();

// Creamos nuestra primera ruta
    //req -> es la info que me envia el cliente
    //res -> es la info que le devuelvo al cliente
    // ENDPOINT - CONTROLADOR - RUTA INICIAL
servidor.get('/',(req,res)=>{
    res.json ({
        message:"Bienvenido a mi API"
    });
});

servidor.post("/productos",(req,res) => {
    console.log(req.body);

    res.json({
        message:"Producto creado exitosamente",
    });
});


// Ejecutamos con el metodo listen
servidor.listen(5000, () => {
    console.log ("Servidor corriendo exitosamente en el puerto 5000");
});