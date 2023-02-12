//Asi se exporta utilizado ECMAscript
import conexion from '../conector_bd.js'

export const crearCategoria = async (req, res) => {
    const { body } = req
    console.log(body)
    //Si es que la creacion es exitosa
    // de manera asincrona
    // el await hace esperar la ejecucion de la cat..por lo tanto se pone ASYNC arriba
    const respuesta = await conexion.categoria.create({
        data:{
            nombre:body.nombre,
        },
    })

    res.json({
        message:'Se creo la categoria exitosamente',
        content: respuesta,

    })
}

export const listarCategorias = async (req,res) => {
    const respuesta = await conexion.categoria.findMany()// findmany para extraer todas las categorias

    res.json({
        content: respuesta,
    })
}

export const buscarCategoriaPorId = async (req, res) => {
    console.log(req.params)
    const { id } = req.params
    const resultado = await conexion.categoria.findFirst({where:{id: +id}}) //Al agregar + adelante del id, se toma como entero porque le decimos que lo queremos sumar. Tambien se puede usar parseInt(id)

    if (!resultado) {
        res.json({
            message: 'Categoria no existe'
        })
    }

    res.json({
        content: resultado,
    })
}

// Asi se exporta commonJS -> JS Comun
// module.exports = {
//     crearCategoria,
// }

