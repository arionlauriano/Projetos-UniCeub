DROP DATABASE colecao_livros;

CREATE DATABASE colecao_livros;

USE colecao_livros;

CREATE TABLE editoras(
	cod_editora INT AUTO_INCREMENT PRIMARY KEY,
    nome_editora VARCHAR(50));
    
INSERT INTO editoras (nome_editora) VALUES
	("Rocco"),
    ("Altaya"),
    ("Oni Press"),
    ("Universo do Livro"),
    ("Moderna");
    
CREATE TABLE autores(
	cod_autor INT AUTO_INCREMENT PRIMARY KEY,
    nome_autor VARCHAR(50));
    
INSERT INTO autores (nome_autor) VALUES
	("Susanne Collins"),
    ("Christopher Paolini"),
    ("Aghata Christe"),
    ("K. O'Niell"),
    ("Pedro Bandeira");
    
CREATE TABLE livros_adiquiridos(
	cod_livro INT AUTO_INCREMENT PRIMARY KEY,
    nome_livro VARCHAR(50),
    id_autor INT NOT NULL,
    id_editora INT NOT NULL, 
    CONSTRAINT fk_autor_livro FOREIGN KEY (id_autor) REFERENCES autores(cod_autor),
    CONSTRAINT fk_editora_livro FOREIGN KEY (id_editora) REFERENCES editoras(cod_editora));

INSERT INTO livros_adiquiridos (nome_livro, id_autor, id_editora) VALUES
	("Cantiga de Pássaros e Serpentes", 1, 1),
    ("Amanhecer na Colheita", 1, 1),
    ("Jogos Vorazes", 1, 1),
    ("Em Chamas", 1, 1),
    ("Esperança", 1, 1),
    ("Eragon", 2, 1),
    ("Thorn", 2, 1),
    ("Brisingir", 2, 1),
    ("Eldest", 2, 1),
    ("Herança", 2, 1),
    ("Murtagh", 2, 1),
    ("The Tea Dragon Society", 4, 3),
    ("A Droga da Amizade", 5, 5);

SELECT * FROM autores;
    
SELECT * FROM editoras;

DROP TABLE livros_adiquiridos;
DROP TABLE autores;