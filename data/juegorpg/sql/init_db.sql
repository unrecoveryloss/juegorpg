CREATE DATABASE IF NOT EXISTS juegorpg CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE juegorpg;

CREATE TABLE rol (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre_rol VARCHAR(20) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(20) NOT NULL,
  correo_usuario VARCHAR(40) NOT NULL UNIQUE,
  contraseña_usuario VARCHAR(255) NOT NULL,
  id_rol INT NOT NULL,
  FOREIGN KEY (id_rol) REFERENCES rol(id_rol) ON DELETE RESTRICT,
  INDEX (correo_usuario)
) ENGINE=InnoDB;

CREATE TABLE raza (
  id_raza INT AUTO_INCREMENT PRIMARY KEY,
  nombre_raza VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE estado (
  id_estado INT AUTO_INCREMENT PRIMARY KEY,
  nombre_estado VARCHAR(50) NOT NULL UNIQUE,
  estado_base VARCHAR(50),
  origen_estado VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE personaje (
  id_personaje INT AUTO_INCREMENT PRIMARY KEY,
  nombre_personaje VARCHAR(20) NOT NULL,
  nivel INT NOT NULL DEFAULT 1,
  id_usuario INT NOT NULL,
  id_raza INT NOT NULL,
  id_estado INT NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
  FOREIGN KEY (id_raza) REFERENCES raza(id_raza) ON DELETE RESTRICT,
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado) ON DELETE RESTRICT,
  INDEX (nombre_personaje)
) ENGINE=InnoDB;

CREATE TABLE habilidad (
  id_habilidad INT AUTO_INCREMENT PRIMARY KEY,
  nombre_habilidad VARCHAR(50) NOT NULL,
  descripcion_habilidad VARCHAR(100),
  origen_habilidad VARCHAR(50),
  id_raza INT NOT NULL,
  FOREIGN KEY (id_raza) REFERENCES raza(id_raza) ON DELETE CASCADE,
  INDEX (nombre_habilidad)
) ENGINE=InnoDB;

CREATE TABLE poder (
  id_poder INT AUTO_INCREMENT PRIMARY KEY,
  nombre_poder VARCHAR(50) NOT NULL,
  descripcion_poder VARCHAR(100),
  origen_poder VARCHAR(50),
  id_raza INT NOT NULL,
  FOREIGN KEY (id_raza) REFERENCES raza(id_raza) ON DELETE CASCADE,
  INDEX (nombre_poder)
) ENGINE=InnoDB;

CREATE TABLE equipo (
  id_equipo INT AUTO_INCREMENT PRIMARY KEY,
  nombre_equipo VARCHAR(50) NOT NULL,
  descripcion_equipo VARCHAR(100),
  origen_equipo VARCHAR(50),
  UNIQUE(nombre_equipo)
) ENGINE=InnoDB;

CREATE TABLE personaje_habilidad (
  id_personaje INT NOT NULL,
  id_habilidad INT NOT NULL,
  PRIMARY KEY (id_personaje, id_habilidad),
  FOREIGN KEY (id_personaje) REFERENCES personaje(id_personaje) ON DELETE CASCADE,
  FOREIGN KEY (id_habilidad) REFERENCES habilidad(id_habilidad) ON DELETE CASCADE,
  INDEX (id_habilidad)
) ENGINE=InnoDB;

CREATE TABLE personaje_poder (
  id_personaje INT NOT NULL,
  id_poder INT NOT NULL,
  PRIMARY KEY (id_personaje, id_poder),
  FOREIGN KEY (id_personaje) REFERENCES personaje(id_personaje) ON DELETE CASCADE,
  FOREIGN KEY (id_poder) REFERENCES poder(id_poder) ON DELETE CASCADE,
  INDEX (id_poder)
) ENGINE=InnoDB;

CREATE TABLE personaje_equipo (
  id_personaje INT NOT NULL,
  id_equipo INT NOT NULL,
  PRIMARY KEY (id_personaje, id_equipo),
  FOREIGN KEY (id_personaje) REFERENCES personaje(id_personaje) ON DELETE CASCADE,
  FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo) ON DELETE RESTRICT,
  INDEX (id_equipo)
) ENGINE=InnoDB;

INSERT INTO raza (nombre_raza) VALUES 
('Humano'),
('Elfo'),
('Enano'),
('Orco');

INSERT INTO rol (nombre_rol) VALUES ('usuario'), ('admin');

INSERT INTO estado (nombre_estado, estado_base, origen_estado) VALUES 
('Saludable', 'base', 'inicial'),
('Enfermo', 'base', 'evento'),
('Herido', 'base', 'combate');