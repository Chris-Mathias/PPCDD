DROP DATABASE IF EXISTS pop;

CREATE DATABASE pop;

USE pop;

CREATE TABLE municipio (
    id INT NOT NULL AUTO_INCREMENT,
    uf VARCHAR(2) NOT NULL,
    cod_uf INT NOT NULL,
    cod_municipio INT NOT NULL,
    nome_municipio VARCHAR(100) NOT NULL,
    populacao INT NOT NULL,
	PRIMARY KEY (id, cod_uf, cod_municipio)
);