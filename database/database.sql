CREATE DATABASE db_empresa_polar;

CREATE TABLE dependencias (
    id_dependencia INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_dependencia VARCHAR(30) NOT NULL
);

CREATE TABLE cargos (
    id_cargo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_cargo VARCHAR(30) NOT NULL UNIQUE,
    salario NUMERIC(9, 0) NOT NULL,
    id_dependencia INTEGER NOT NULL,
    FOREIGN KEY(id_dependencia) REFERENCES dependencias(id_dependencia)
);

CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombres VARCHAR(30) NOT NULL,
    apellidos VARCHAR(30),
    documento NUMERIC(11, 0) UNIQUE NOT NULL,
    fecha_nacimiento DATE,
    genero VARCHAR(10),
    correo VARCHAR(200) UNIQUE NOT NULL,
    celular NUMERIC(11, 0),
    direccion VARCHAR(200),
    ciudad VARCHAR(20),
    estado_civil VARCHAR(20),
    password VARCHAR(200),
    rol VARCHAR(3) NOT NULL
);

CREATE TABLE info_laboral (
    id_info INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_cargo INTEGER NOT NULL,
    tipo_contrato VARCHAR(30) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    fecha_terminacion DATE NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY(id_cargo) REFERENCES cargos(id_cargo)
);

CREATE TABLE retroalimentaciones (
    id_retroalimentacion INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    puntaje NUMERIC(3, 0) NOT NULL,
    fecha_retroalimentacion DATE NOT NULL,
    retroalimentacion TEXT NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_evaluador INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY(id_evaluador) REFERENCES usuarios(id_usuario)
);