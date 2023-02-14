import conexion from '../conector_bd.js'

export const crearProducto = async (req,res) => {
    const { body } = req
    // {nombre:'blabla' , precio:10 , tieneIgv=true, sku:'10a15, categoriaId: 1}

    //Primero buscar si existe la categoria
    const categoria = await conexion.categoria.findFirst({where: {id : +body.categoriaId }})
    // Si no existe retornar un mensaje que los datos son incorrectos
    if (!categoria) {
        return res.json({
            message : 'La categoria no existe'
        })
    }
    // Si existe la categoria entonces crear ese nuevo producto
    const resultado = await conexion.producto.create ({
        data:{
            // nombre: body.nombre,
            // precio: body.precio,
            // tieneIgv: body.tieneIgv,
            // sku: body.sku,
            
            //SPREAD OPERATOR -> Sacar el contenido de un json, utilizare su contenido, mas no creare una llave llamada 'body'
            ...body,
            categoriaId: +body.categoriaId

        },
    })

    return res.json({
        message: 'Producto creado exitosamente',
        content: resultado,
    })
}

export const toggleProducto = async (req,res) => {
    // hablilitar-deshabilitar el producto
    const { id }= req.params
    //SELECT habilitado FROM productos WHERE id=
    const producto = await conexion.producto.findFirst({
        where: {id: +id}, 
        select:{habilitado: true},
    })

    if(!producto) {
        return res.json({
            message: 'El producto no existe'
        })
    }

    //!boolean -> Indicamos que queremos el valor contario
    const resultado = await conexion.producto.update({
        where: { 
            id: +id 
        },
        data:{
            habilitado: !producto.habilitado
        },
        // aparte de realizar la actualizacion indicaremos que columnas queremos visualizar como respuesta
        // NOTA: no es obligatorio solamente indicar la informacion que estamos actualizando
        // el select me indica que columnas queremos visualizar
        select: { 
            habilitado:true 
        },
    })

    return res.json({
        message: 'Producto ' + (resultado.habilitado === true ? 'habilitado' : 'deshabilitado'), // ? : Operadores ternarios
    })


}