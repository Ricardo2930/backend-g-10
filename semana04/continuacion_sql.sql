-- Asi se crea una base de datos cada una es indpendiente
CREATE DATABASE IF NOT EXISTS practicas;

USE practicas;
-- ahora procedemos a crear nuestra primera tabla
-- tipos de datos:
-- AUTO_INCREMENT >> Solamente puede haber uno por tabla

CREATE TABLE usuarios (
-- nombre  datatype (config. adicionales)
	id 		INT 	AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre  TEXT    NOT NULL,
    DNI     CHAR(8) UNIQUE
    
);

CREATE TABLE tareas(
	id 			INT 			AUTO_INCREMENT PRIMARY KEY,
    titulo  	VARCHAR(100)	UNIQUE,
    descripcion TEXT,
    usuario_id  INT,
    -- CREO LA RELACION ENTRE LAS TABLAS
    -- indico entre parentesis la columna de esta tabla y luego la tabla(su columna)
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


-- SUB LENGUAJES
-- DDL (Data Definition Language)
-- Es un lenguaje que sirve para definir estructuras de datos (Crear bd, crear tablas,
-- actualizar tablas, eliminar tablas)
-- CREATE (Crear)
-- ALTER  (Actualizar)
-- DROP   (Eliminar) elimina absolutamente TODO

-- DML (Data Manipulation Language)
-- Es un lenguaje que sirve para definir la informacion que ira dentro de las estructuras
-- Insertar datos, actualizar datos, eliminar datos y leer datos
-- INSERT (Insertar)
-- SELECT (Visualizar)
-- UPDATE (Actualizar)
-- DELETE (Eliminar)

-- En este caso como el 'id' es auto_increment no le pondremos un valor 
INSERT INTO usuarios (nombre, dni) VALUES ('RICARDO', '46706232');

-- Si queremos utilizar el valor por defecto de una columna
INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Juana', '71589264');

-- Si queremos ingresar varios registros
INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Roberto', '35269485'), 
                                              (DEFAULT, 'Maria', '29165148'),
                                              (DEFAULT, 'Roxana', '56236841');

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
				(DEFAULT, 'ir a la playa', 'ire a la playa el fin de semana', 1),
                (DEFAULT, 'ir a la piscina', 'ire a la piscina a mis clases de natacion', 2);

-- Visualizar la informacion
SELECT nombre, dni, id, id FROM usuarios;

-- Visualizar la totalidad de las columnas
SELECT * FROM usuarios;

INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Juana', '33265946'), 
                                              (DEFAULT, 'Maria', '52698524');

-- SELECCIONA TODAS LAS COLUMNAS DE LA TABLA USUARIOS DONDE nombre SEA Juana
SELECT * FROM usuarios WHERE nombre='Juana' AND id=2;

-- Visualizar todas las tareas del usuario 1 Y/O del usuario 2
SELECT * FROM tareas WHERE usuario_id=1 OR usuario_id=2;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
					(DEFAULT, 'ir a comer', 'comer un pollo a la brasa', 1),
					(DEFAULT, 'comer pizza', 'comer una pizza peperonis', 1);

SELECT * FROM tareas WHERE usuario_id=1;

SELECT * FROM usuarios;
-- buscar una palabra o palabras dentro de un texto

SELECT * FROM usuarios where nombre like '%comer%';
SELECT * FROM usuarios where nombre like 'J%';
-- Si queremos hacer la distincion entre mayus y minus entonces antes de poner el texto colocaremos la palabra
-- BINARY y esto sirve para que haga la comparacion a nivel de numeros de caracteres (formato ASCII) 
SELECT * FROM usuarios where nombre like binary 'J%';
-- _ > indico cuantos caracteres debe saltar para que busque el caracter (cada guion abajo es un caracter)
SELECT * FROM usuarios where nombre like '_u%';

-- traer todos los usuarios que el segundo caracter NO es U
SELECT * FROM usuarios where nombre not like '_u%';

SELECT * FROM tareas;

-- Insertamos un tarea sin dueño
INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
			(DEFAULT, 'no hacer nada', 'no hacer nada porque es domingo', null);
            
INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
                  (DEFAULT, 'Jugar LOL', 'Jugar con mis amigos pros', 3);            

-- Interseccion entre la tabla usuarios con la tabla tareas donde usuarios.id=tareas.usuario.id
SELECT * FROM usuarios INNER JOIN tareas ON usuarios.id = tareas.usuario_id;

SELECT * FROM usuarios LEFT JOIN tareas ON usuarios.id = tareas.usuario_id;

SELECT * FROM usuarios RIGHT JOIN tareas ON usuarios.id = tareas.usuario_id;

-- FULL OUTER JOIN -> Selecciona todos los usuarios aun asi no tengan tareas, y todas las tareas
-- aun asi no tengan usuarios.
-- hace una mezcla completa entre los usuarios y las tareas respetando sus conexiones 
SELECT * FROM usuarios LEFT JOIN tareas ON usuarios.id = tareas.usuario_id UNION
SELECT * FROM usuarios RIGHT JOIN tareas ON usuarios.id = tareas.usuario_id;
-- UNION mezcla o combina las dos o mas consultas en una sola "tabla virtual"
-- pero esas consultas tienen que tener en mismo numero de columnas, sino el UNION sera incorrecto
SELECT nombre FROM usuarios UNION
SELECT titulo FROM tareas;

-- CONCATENAR > Juntar combinar
-- AS = Como, para poner un nombre a la columna CONCAT (Buenas practicas)
SELECT CONCAT(titulo,' ',descripcion) AS 'Detalles Completos' FROM tareas;

SELECT * FROM usuarios;
SELECT * FROM tareas;

-- EJERCICIOS
-- 1. Devolver todos los usuarios cuyo dni contenga el numero 5
SELECT * FROM usuarios where dni like '%5%';

-- 2. Devolver todos los usuarios cuyo dni tengan el tercer digito 8
SELECT * FROM usuarios where dni like '__8%';

-- 3. Devolver todas las tareas de usuario 'RICARDO'
SELECT * FROM usuarios INNER JOIN tareas ON usuarios.id = tareas.usuario_id WHERE nombre = 'RICARDO';