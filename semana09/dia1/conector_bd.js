import prisma from '@prisma/client'

// asi se exporta de manera por defecto (en el caso que tengamos una sola exportacion en nuestro archivo)
// solamente se puede tener una exportacion por defecto
export default new prisma.PrismaClient()