-- Biometri ToDo
DROP DATABASE app_despesas;
CREATE DATABASE app_despesas;
USE app_despesas;

-- Cadastro e Login

CREATE TABLE usuario (
	id_usuario NUMERIC PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
	nome VARCHAR(100) NOT NULL
);

CREATE TABLE login (
    login_usuario VARCHAR(100) PRIMARY KEY, 
    senha VARCHAR(20) NOT NULL
);

-- Categorias

CREATE TABLE categorias (
	id_categoria NUMERIC PRIMARY KEY,
	nome_cat VARCHAR(30) NOT NULL,
    descricao_cat VARCHAR(100) NOT NULL,
    limite_despesa NUMERIC NULL
);

-- Adição dos Cartões e Formas de Pagamento

CREATE TABLE FORMA_PAGAMENTO(
	id_pag NUMERIC PRIMARY KEY,
	metodo VARCHAR(20) NOT NULL
	);
    
INSERT INTO FORMA_PAGAMENTO (id_pag, metodo) VALUES 
(1, "Cartão de Débito"),
(2, "Cartão de Crédito"),
(3, "PIX");

CREATE TABLE INFO_CARTAO (
	id_cartao INT AUTO_INCREMENT PRIMARY KEY,
    apelido_cartao VARCHAR(30) NOT NULL,
    operadora VARCHAR(30) NOT NULL,
    limite_ NUMERIC NOT NULL,
    tipo NUMERIC,
    id_usuario NUMERIC
	);

CREATE TABLE REGI_DESPESA (
    id_despesa NUMERIC PRIMARY KEY,
    id_usuario NUMERIC NOT NULL,
	id_cat NUMERIC NOT NULL,
    id_metodo NUMERIC NOT NULL,
    id_cartao INT NULL,
    descricao VARCHAR(300),
    data_d DATE NOT NULL
);

-- Chaves estrangeiras

ALTER TABLE login
ADD CONSTRAINT fk_login_email FOREIGN KEY (login_usuario) REFERENCES usuario(email);

ALTER TABLE INFO_CARTAO
ADD CONSTRAINT fk_cart_metodo FOREIGN KEY (tipo) REFERENCES FORMA_PAGAMENTO(id_pag),
ADD CONSTRAINT fk_cart_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario);

ALTER TABLE REGI_DESPESA
ADD CONSTRAINT fk_desp_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
ADD CONSTRAINT fk_desp_cat FOREIGN KEY (id_cat) REFERENCES categorias(id_categoria),
ADD CONSTRAINT fk_desp_met FOREIGN KEY (id_metodo) REFERENCES FORMA_PAGAMENTO(id_pag),
ADD CONSTRAINT fk_desp_cartao FOREIGN KEY (id_cartao) REFERENCES INFO_CARTAO(id_cartao);






