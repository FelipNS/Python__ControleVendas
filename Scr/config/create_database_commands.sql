DROP DATABASE IF EXISTS `acaiteria`;
CREATE DATABASE `acaiteria`;
USE `acaiteria`;


DROP TABLE IF EXISTS `cidades`;
CREATE TABLE `cidades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `UF` char(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `previlegios`;
CREATE TABLE `previlegios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `empregados`;
CREATE TABLE `empregados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_previlegio` int DEFAULT NULL,
  `primeiro_nome` varchar(50) DEFAULT NULL,
  `sobrenome` varchar(50) DEFAULT NULL,
  `nr_celular` char(12) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `id_filial` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `empregados_id_cargo_fk` (`id_previlegio`),
  KEY `FK_filial` (`id_filial`),
  CONSTRAINT `empregados_id_cargo_fk` FOREIGN KEY (`id_previlegio`) REFERENCES `previlegios` (`id`),
  CONSTRAINT `FK_filial` FOREIGN KEY (`id_filial`) REFERENCES `cidades` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `login_empregados`;
CREATE TABLE `login_empregados` (
  `id_login` int NOT NULL AUTO_INCREMENT,
  `id_empregado` int DEFAULT NULL,
  `nome_usuario` varchar(20) DEFAULT NULL,
  `senha_usuario` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_login`),
  UNIQUE KEY `id_login` (`id_login`),
  KEY `login_empregados_id_empregado_fk` (`id_empregado`),
  CONSTRAINT `login_empregados_id_empregado_fk` FOREIGN KEY (`id_empregado`) REFERENCES `empregados` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


#  Random values to povoate table 

INSERT INTO cidades 
VALUES (1, 'Capelinha', 'MG'),
       (2, 'São Paulo', 'SP'),
       (3, 'Rio de Janeiro', 'RJ');

INSERT INTO previlegios
VALUES (1, 'Administrador'),
       (2, 'Gerente'),
       (3, 'Atendente');

INSERT INTO empregados
VALUES (1, 1, 'Felipe', 'Nunes', '33114578025', 'felipe@mail.com', 1),
       (2, 2, 'João', 'Silva', '33114578025', 'joao@mail.com', 1),
       (3, 3, 'Maria', 'Sampaio', '33114578025', 'maria@mail.com', 2),
       (4, 3, 'Pedro', 'Soares', '33114578025', 'pedro@mail.com', 3);

INSERT INTO login_empregados
VALUES (1, 1, 'felipenunes', '123456789'),
       (2, 2, 'joaosilva', '456789123'),
       (3, 3, 'mariasampaio', '987654321'),
       (4, 4, 'pedrosoares', '1537594862');