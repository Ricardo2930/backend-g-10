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
    const resultado = await conexion.categoria.findFirst({
        where:{
            id: +id
        },//Al agregar + adelante del id, se toma como entero porque le decimos que lo queremos sumar. Tambien se puede usar parseInt(id)
        include: {
            productos:true
        },// include -> Sirve para indicar si queremos algun modelo vecino (Productos de la CategoriaId)
    }) 

    if (!resultado) {
        return res.json({
            message: 'Categoria no existe'
        })
    }

    // no se puede enviar dos o mas respuestas al cliente porque la conexion ya termino    
    else {
       return res.json({
            content: resultado,
        })
    }
    
}

export const actualizarCategoria = async(req, res) => {
    const { id } = req.params
    const { body } = req

    //Buscar primero si la categoria existe, sino existe retornar un mensaje que no existe
    const categoria = await conexion.categoria.findFirst({where:{id : +id}})
    if(!categoria) {
        return res.json({
            message:'La categoria no existe',
        })
    }

    const resultado = await conexion.categoria.update({
        data:{
            nombre: body.nombre,
        }, 
        where:{
            id: +id,
        },
    })

    return res.json({
        content : resultado,
    })

}

export const eliminarCategoria = async (req, res) => {
    const { id } = req.params

    const categoriaEncontrada = await conexion.categoria.findFirst({where: {id: +id}})
    if (!categoriaEncontrada) {
        return res.json({
            message: 'La categoria no existe'
        })
    }

    await conexion.categoria.delete({where:{id : +id}})

    return res.json({
        message:'Categoria eliminada exitosamente',
    })
}

// Asi se exporta commonJS -> JS Comun
// module.exports = {
//     crearCategoria,
// }

