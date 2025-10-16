DROP SCHEMA db_auto;
CREATE SCHEMA db_auto;
USE db_auto;

-- Criação de Tabelas
CREATE TABLE montadora (
id_mont INT AUTO_INCREMENT PRIMARY KEY,
sgl_mont VARCHAR(10) NOT NULL,
nome_mont VARCHAR(50) NOT NULL
);

CREATE TABLE modelo (
id_mod INT AUTO_INCREMENT PRIMARY KEY,
nome_mod VARCHAR(50) NOT NULL,
cod_mont INT NOT NULL
);

CREATE TABLE versao (
id_vers INT AUTO_INCREMENT PRIMARY KEY,
nome_vers VARCHAR(30) NOT NULL,
vlr_mod DECIMAL(10,2) NOT NULL,
img_mod VARCHAR(50),
cod_mod INT NOT NULL
);

CREATE TABLE compra (
id_comp INT AUTO_INCREMENT PRIMARY KEY,
data_comp DATE NOT NULL,
cod_nf_comp VARCHAR(30) NOT NULL,
total_comp DECIMAL(10,2),
cod_cli INT NOT NULL,
cod_vers INT NOT NULL
);

CREATE TABLE cliente (
id_cli INT AUTO_INCREMENT PRIMARY KEY,
nome_cli VARCHAR(50) NOT NULL,
data_nasc_cli DATE NOT NULL,
cod_uf INT NOT NULL,
cep_cli CHAR(9) NOT NULL,
end_cli TEXT NOT NULL
);

CREATE TABLE uf (
id_uf INT AUTO_INCREMENT PRIMARY KEY,
sgl_uf CHAR(2) NOT NULL,
nome_uf VARCHAR(20) NOT NULL
);

-- Constraints Montadora, Modelo e Versão
ALTER TABLE modelo
ADD CONSTRAINT fk_mont_mod FOREIGN KEY (cod_mont) REFERENCES montadora(id_mont);

ALTER TABLE versao
ADD CONSTRAINT fk_mod_vers FOREIGN KEY (cod_mod) REFERENCES modelo(id_mod);


-- Constraints Compra, Cliente e UF
ALTER TABLE compra 
ADD CONSTRAINT fk_vers_comp FOREIGN KEY (cod_vers) REFERENCES versao(id_vers),
ADD CONSTRAINT fk_cli_comp FOREIGN KEY (cod_cli) REFERENCES cliente(id_cli);

ALTER TABLE cliente
ADD CONSTRAINT fk_uf_cli FOREIGN KEY (cod_uf) REFERENCES uf(id_uf); 