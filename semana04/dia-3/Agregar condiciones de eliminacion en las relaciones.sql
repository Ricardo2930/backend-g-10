use minimarket;

ALTER TABLE almacen_producto DROP FOREIGN KEY almacen_producto_ibfk_2;
-- OPCIONES
-- RESTRICT > restringe o impide la eliminacion de nuestro padre si tiene hijos
-- CASCADE > elimina el padre y elimina a sus hijos
-- SET NULL > elimina al padre y a sus hijos les cambia el valor de esa columna a NULL
-- NO ACTION > elimina al padre PERO aun conversara su id dando como resultado un problema de integridad
-- SET DEFAULT > asigna un valor por defecto en el caso que se elimine el padre
ALTER TABLE almacen_producto ADD FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE;