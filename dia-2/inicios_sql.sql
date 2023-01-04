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
