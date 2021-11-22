CREATE TABLE empregados(
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    id_cargo INT,
    primeiro_nome VARCHAR(50),
    sobrenome VARCHAR(50),
    CONSTRAINT empregados_id_cargo_fk FOREIGN KEY(id_cargo) REFERENCES cargos(id)
);
CREATE TABLE cargos(
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE login_empregados(
    id_login INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    id_empregado INT,
    nome_usuario VARCHAR(20),
    senha_usuário VARCHAR(50),
    CONSTRAINT login_empregados_id_empregado_fk FOREIGN KEY(id_empregado) REFERENCES empregados(id)
);

ALTER TABLE empregados CHANGE id_cargo id_previlegio INT;
