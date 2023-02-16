import jwt from "jsonwebtoken";

export const validarToken = (req, res, next) => {
    return res.status(401).json({
        message: "Se necesita una token para realizar una peticion",
    })
}

//Bearer 
//['Bearer']

const token = req.headers.authorization.split(" ")[1];
if(!token) {
    return res.status(401),json({
        message: "Formato de token invalido, deber ser en el formato Bearer <tu_token>",
    });
}