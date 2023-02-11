//Asi se importa utilizado ECMAscript
import express from 'express'
import prisma from '@prisma/client'
import {crearCategoria} from './controllers/categorias.controllers.js'

//Importamos la libreria EXPRESS
//Asi se importa usando commonJS -> JS Comun
    // const express = require("express");
    // const { PrismaClient } = require("@prisma/client");
    // const {crearCategoria} = require ('./controllers/categorias.controllers')

    // const prisma = new PrismaClient()
const conexion = new prisma.PrismaClient()

// Se va a copia toda la funcionalidad de la liberia express en la varibale servidor
const servidor = express()

//Ahora mi sercidor podra convertir la info entrante para los JSON
//MIDDLEWARE para convertir la info entrante a un formato legible
servidor.use(express.json())

// Creamos nuestra primera ruta
    //req -> es la info que me envia el cliente
    //res -> es la info que le devuelvo al cliente
    // ENDPOINT - CONTROLADOR - RUTA INICIAL
servidor.get('/',(req,res)=>{
    res.json ({
        message:"Bienvenido a mi API"
    });
});

servidor.route('/categorias').post(crearCategoria)

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