//Asi se exporta utilizado ECMAscript
export const crearCategoria = (req, res) => {
    const { body } = req
    console.log(body)

    res.json({
        'message':'Se creo la categoria exitosamente',
    })
}

// Asi se exporta commonJS -> JS Comun
// module.exports = {
//     crearCategoria,
// }

