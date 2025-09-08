DROP DATABASE colecao_livros;

CREATE DATABASE colecao_livros;

USE colecao_livros;
    
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
    CONSTRAINT fk_autor_livro FOREIGN KEY (id_autor) REFERENCES autores(cod_autor));

INSERT INTO livros_adiquiridos (nome_livro, id_autor) VALUES
    ("Cantiga de Pássaros e Serpentes", 1),
    ("Amanhecer na Colheita", 1),
    ("Jogos Vorazes", 1),
    ("Em Chamas", 1),
    ("Esperança", 1),
    ("Eragon", 2),
    ("Thorn", 2),
    ("Brisingir", 2),
    ("Eldest", 2),
    ("Herança", 2),
    ("Murtagh", 2),
    ("The Tea Dragon Society", 4),
    ("A Droga da Amizade", 5);

SELECT * FROM autores;

DROP TABLE livros_adiquiridos;
DROP TABLE autores;