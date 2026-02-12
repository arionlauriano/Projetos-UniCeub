CREATE DATABASE mercadinho;

USE mercadinho;

-- Criação de tabelas cliente

CREATE TABLE cliente (
codigo INTEGER AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(60) NOT NULL,
rua VARCHAR(80) NOT NULL,
nr INTEGER(4) NOT NULL,
bairro VARCHAR(50) NOT NULL,
complemento VARCHAR(100) NULL,
cidade VARCHAR(50) NOT NULL,
uf VARCHAR(2) NOT NULL,
cep VARCHAR(10) NOT NULL
);

CREATE TABLE fone_cliente (
numero VARCHAR(14) PRIMARY KEY,
codigo_cli INTEGER NOT NULL,
CONSTRAINT fk_cli_fone FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo)
);

CREATE TABLE PF (
codigo_cli INTEGER NOT NULL,
cnpf VARCHAR(14) NOT NULL,
rg VARCHAR(10) NOT NULL,
data_nascimento DATE NOT NULL,
CONSTRAINT fk_cli_pf FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo)
);

CREATE TABLE PJ (
codigo_cli INTEGER NOT NULL,
cnpj VARCHAR(19) NOT NULL,
ie VARCHAR(10) NOT NULL,
nome_fantasia VARCHAR(60) NOT NULL,
CONSTRAINT fk_cli_pj FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo)
);

-- criação tabelas vendedores

CREATE TABLE vendedor (
matricula INTEGER PRIMARY KEY,
nome VARCHAR(60) NOT NULL,
CNPF VARCHAR(14) NOT NULL
);

CREATE TABLE fone_vendedor (
numero VARCHAR(14) PRIMARY KEY,
matricula_ven  INTEGER NOT NULL,
CONSTRAINT fk_vend_fone FOREIGN KEY (matricula_ven) REFERENCES vendedor(matricula)
);

-- criação tabelas preteleira

CREATE TABLE prateleira (
codigo INTEGER(3) PRIMARY KEY,
descricao VARCHAR(50) NOT NULL,
numero_sessoes INTEGER(2) NOT NULL
);

-- feito no workbench