-- FUNCIONES DE AGREGACION, agregar funcionalidad a nuestras consultas, solo para SELECT
-- Permiten efectuar operaciones sobre las columnas para obtener resultados
 use minimarket;
 
 select * from productos;
 
 -- Para utilizar cualquier funcion de agregacion se tiene que indicar la clausula GROUP BY y esta clausula
-- servira para indicar como queremos que se realice la agrupacion antes de usar la funcion
-- si solamente queremos obtener un solo resultado entonces la clausula GROUP BY no se puede tomar en consideracion
 -- AVG (COLUMNA) - AVERAGE ES EL PROMEDIO
 SELECT categoria_id, AVG (precio)
 FROM productos
 GROUP BY categoria_id;
 
 -- MAX (COLUMNA) > El valor maximo de esa columna
 SELECT MAX(precio)
 FROM productos;
 
  -- MIN (COLUMNA) > El valor minimo de esa columna
 SELECT MIN(precio)
 FROM productos;
 
 -- COUNT (Columna) -- cuenta cuantos registros tenemos
 SELECT COUNT(precio)
 FROM productos;
 
  -- SUM (Columna) - suma 
  -- PostgreSQL o SQL SERVER intentamos sumar una columna que no es numerica, me da ERROR
 SELECT SUM(precio)
 FROM productos;
 
 -- PAGINACION para ver cuantos items muestro en una pagina
 -- LIMIT me da la cantidad de items que quiero mostrar
 -- OFFSET indica cuantos quiero saltarme
 SELECT * FROM PRODUCTOS
 LIMIT 4
 OFFSET 4;
 
 SELECT * FROM PRODUCTOS;
 
 -- ORDENAMIENTO
 -- ASC:Ascedente  DESC:Descendente
SELECT * FROM PRODUCTOS 
 ORDER BY nombre DESC;
 
 SELECT * FROM PRODUCTOS 
 ORDER BY fecha_vencimiento DESC, nombre DESC;
 
 -- Orden estandar - Buenas Practicas
 SELECT * 
 FROM productos AS p INNER JOIN categorias AS c ON p.categoria_id = c.id
 WHERE c.nombre = 'otros'
 GROUP BY p.id
 ORDER BY fecha_vencimiento DESC, c.nombre DESC
 LIMIT 1
 OFFSET 0;
