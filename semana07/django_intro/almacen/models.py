from django.db import models

# Create your models here.

class ProductosModel (models.Model): 
    id = models.AutoField(primary_key=True) #autofield es para ser autoincrementable
    nombre = models.CharField(max_length=45, null=False)
    precio = models.FloatField(null=False)
    estado = models.BooleanField(default=True, null=False)

    class Meta: # Se define el nombre de la tabla
        db_table = 'productos'

    def __str__(self) -> str: #metodo magico
        return self.nombre

class CategoriasModel (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    estado = models.BooleanField(default=True, null=True)
    producto = models.ManyToManyField(ProductosModel) #usamos el metodo models.ManyToManyField(ProductosModel) para usar relaciones de muchos a muchos, asi se crea la tabla puente categorias_producto

    class Meta:
        db_table = 'categorias'
    
    def __str__(self) -> str:
        return self.nombre

# class ProductosCategoriasModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     producto_id = models.ForeignKey(ProductosModel, on_delete=models.CASCADE)
#     categoria_id = models.ForeignKey(CategoriasModel, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'productos_categorias'
