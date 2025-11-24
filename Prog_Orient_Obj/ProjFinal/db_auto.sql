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
vlr_vers DECIMAL(10,2) NOT NULL,
img_vers VARCHAR(500) NULL,
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

-- Inserts para Testes
INSERT INTO uf (sgl_uf, nome_uf) VALUES
('AC', 'Acre'),
('AL', 'Alagoas'),
('AP', 'Amapá'),
('AM', 'Amazonas'),
('BA', 'Bahia'),
('CE', 'Ceará'),
('DF', 'Distrito Federal'),
('ES', 'Espírito Santo'),
('GO', 'Goiás'),
('MA', 'Maranhão'),
('MT', 'Mato Grosso'),
('MS', 'Mato Grosso do Sul'),
('MG', 'Minas Gerais'),
('PA', 'Pará'),
('PB', 'Paraíba'),
('PR', 'Paraná'),
('PE', 'Pernambuco'),
('PI', 'Piauí'),
('RJ', 'Rio de Janeiro'),
('RN', 'Rio Grande do Norte'),
('RS', 'Rio Grande do Sul'),
('RO', 'Rondônia'),
('RR', 'Roraima'),
('SC', 'Santa Catarina'),
('SP', 'São Paulo'),
('SE', 'Sergipe'),
('TO', 'Tocantins');

INSERT INTO montadora (sgl_mont, nome_mont) VALUES
('VW', 'Volkswagen'),
('GM', 'General Motors'),
('FORD', 'Ford'),
('FIAT', 'Fiat'),
('TOYOTA', 'Toyota');

INSERT INTO modelo (nome_mod, cod_mont) VALUES
('Gol', 1),
('Onix', 2),
('Ka', 3),
('Argo', 4),
('Corolla', 5);

INSERT INTO versao (nome_vers, vlr_vers, cod_mod) VALUES
('1.0 MPI', 65990.00, 1),
('1.6 MSI', 82500.00, 1),
('LT 1.0', 78000.00, 2),
('RS Turbo', 105500.00, 2),
('SE 1.5', 69990.00, 3),
('FreeStyle', 88900.00, 3),
('1.3 Firefly', 75990.00, 4),
('Trekking', 93500.00, 4),
('GLi', 145000.00, 5),
('Altis Premium', 185900.00, 5);

INSERT INTO cliente (nome_cli, data_nasc_cli, cod_uf, cep_cli, end_cli) VALUES
('Ana Silva', '1985-06-15', 25, '01001-000', 'Av. Paulista, 1000 - Bela Vista'),
('Bruno Santos', '1990-01-20', 19, '20040-030', 'Rua Sete de Setembro, 50 - Centro'),
('Carla Oliveira', '1978-11-03', 13, '30110-008', 'Av. Afonso Pena, 2500 - Savassi'),
('Daniel Costa', '2000-03-28', 5, '40010-000', 'Praça Castro Alves, 1 - Centro'),
('Elaine Pereira', '1995-09-10', 16, '80020-090', 'Rua XV de Novembro, 800 - Centro');

INSERT INTO compra (data_comp, cod_nf_comp, total_comp, cod_cli, cod_vers) VALUES
('2023-10-01', 'NF-20231001-001', 185900.00, 1, 10), -- Ana Silva compra Corolla Altis
('2023-10-05', 'NF-20231005-002', 82500.00, 2, 2), -- Bruno Santos compra Gol 1.6 MSI
('2023-10-10', 'NF-20231010-003', 105500.00, 3, 4), -- Carla Oliveira compra Onix RS Turbo
('2023-10-15', 'NF-20231015-004', 75990.00, 4, 7), -- Daniel Costa compra Argo 1.3 Firefly
('2023-10-20', 'NF-20231020-005', 69990.00, 5, 5); -- Elaine Pereira compra Ka SE 1.5