----------CRIAÇÃO----------
-- TABELAS CLIENTE

--    CREATE    --
CREATE TABLE fone_cliente (
numero      VARCHAR2(14) NOT NULL,
codigo_cli  NUMBER NOT NULL
);

CREATE TABLE cliente (
codigo      NUMBER NOT NULL,
nome        VARCHAR2(60) NOT NULL,
rua         VARCHAR2(80) NOT NULL,
nr          NUMBER(4) NOT NULL,
bairro      VARCHAR2(50) NOT NULL,
complemento VARCHAR2(100) NULL,
cidade      VARCHAR2(50) NOT NULL,
uf          VARCHAR2(2) NOT NULL,
cep         VARCHAR2(10) NOT NULL
);

CREATE TABLE pf (
codigo_cli      NUMBER NOT NULL,
cnpf            VARCHAR2(14) NOT NULL,
rg              VARCHAR2(10) NOT NULL,
data_nascimento DATE NOT NULL
);

CREATE TABLE pj (
codigo_cli    NUMBER NOT NULL,
cnpj          VARCHAR2(19) NOT NULL,
ie            VARCHAR2(10) NOT NULL,
nome_fantasia VARCHAR2(60) NOT NULL
);

--    CONSTRAINTS   --
ALTER TABLE cliente
ADD CONSTRAINT pk_cliente PRIMARY KEY (codigo);

ALTER TABLE fone_cliente
ADD CONSTRAINT pk_fone_cliente  PRIMARY KEY (numero)
ADD CONSTRAINT fk_fone          FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo);

ALTER TABLE pf
ADD CONSTRAINT pk_cliente_pf    PRIMARY KEY (codigo_cli)
ADD CONSTRAINT fk_pf_clicliente FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo);

ALTER TABLE pj
ADD CONSTRAINT pk_cliente_pj PRIMARY KEY (cnpj)
ADD CONSTRAINT fk_pj_cliente FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo);


-- TABELAS VENDEDORES

--    CREATE    --
CREATE TABLE fone_vendedor (
numero        VARCHAR2(14) NOT NULL,
matricula_ven NUMBER NOT NULL
);

CREATE TABLE vendedor (
matricula NUMBER NOT NULL,
nome      VARCHAR2(60) NOT NULL,
cnpf      VARCHAR2(14) NOT NULL
);

--    CONSTRAINTS   --
ALTER TABLE vendedor
ADD CONSTRAINT pk_vendedor PRIMARY KEY (matricula);

ALTER TABLE fone_vendedor
ADD CONSTRAINT pk_fone_vendedor PRIMARY KEY (numero)
ADD CONSTRAINT fk_fone_vendedor FOREIGN KEY (matricula_ven) REFERENCES vendedor(matricula);


-- TABELAS PRODUTO E PEDIDO

--    CREATE    --
CREATE TABLE produto (
codigo      NUMBER NOT NULL,
descricao   VARCHAR2(80) NOT NULL,
unid_medida VARCHAR2(10) NOT NULL
);

CREATE TABLE item_produto (
codigo_pro      NUMBER NOT NULL,
numero_ped      NUMBER(6) NOT NULL,
quantidade      NUMBER(5) NOT NULL,
preco_unitario  NUMBER(5,2) NOT NULL,
valor_item      NUMBER(7,2) NULL
);

CREATE TABLE pedido (
numero        NUMBER(6) NOT NULL,
data          DATE NOT NULL,
prazo_entrega DATE NULL,
rua           VARCHAR2(80) NULL,
nr            NUMBER(4) NULL,
bairro        VARCHAR2(50) NULL,
complemento   VARCHAR2(100) NULL,
cidade        VARCHAR2(100) NULL,
uf            VARCHAR2(2) NULL,
cep           VARCHAR2(10) NULL,
total_fatura  NUMBER(8,2) NULL,
codigo_cli    NUMBER NOT NULL,
matricula_ven NUMBER NOT NULL
);

--    CONSTRAINTS    --
ALTER TABLE produto
ADD CONSTRAINT pk_produto PRIMARY KEY (codigo);

ALTER TABLE pedido
ADD CONSTRAINT pk_pedido        PRIMARY KEY (numero)
ADD CONSTRAINT fk_ped_cliente   FOREIGN KEY (codigo_cli) REFERENCES cliente(codigo)
ADD CONSTRAINT fk_ped_vendedor  FOREIGN KEY (matricula_ven) REFERENCES vendedor(matricula);

ALTER TABLE item_produto
ADD CONSTRAINT fk_item_pedido FOREIGN KEY (numero_ped) REFERENCES pedido(numero)
ADD CONSTRAINT fk_item_produto FOREIGN KEY (codigo_pro) REFERENCES produto(codigo);


-- TABLES PRATELEIRA E ESTOQUE

--    CREATE    --
CREATE TABLE prateleira (
codigo        NUMBER(3) NOT NULL,
descrição     VARCHAR2(50) NOT NULL,
numero_secoes NUMBER(2) NOT NULL
);

CREATE TABLE estoque (
data_entrada  DATE NOT NULL,
codigo_pro    NUMBER NOT NULL,
codigo_pra    NUMBER(3) NOT NULL,
quantidade    NUMBER(5) NOT NULL,
data_validade DATE NULL
);

CREATE TABLE capacidade_estoque (
codigo_pro NUMBER NOT NULL,
codigo_pra NUMBER(3) NOT NULL,
quantidade NUMBER(5) NOT NULL
);

--    CONSTRAINTS   --
ALTER TABLE prateleira 
ADD CONSTRAINT pk_prateleira PRIMARY KEY (codigo);

ALTER TABLE estoque 
ADD CONSTRAINT pk_estoque         PRIMARY KEY (data_entrada)
ADD CONSTRAINT fk_est_prateleira  FOREIGN KEY (codigo_pra) REFERENCES prateleira(codigo)
ADD CONSTRAINT fk_est_produto     FOREIGN KEY (codigo_pro) REFERENCES produto(codigo);

ALTER TABLE capacidade_estoque 
ADD CONSTRAINT fk_cap_est_prateleira  FOREIGN KEY (codigo_pra) REFERENCES prateleira(codigo)
ADD CONSTRAINT fk_cap_est_produto     FOREIGN KEY (codigo_pro) REFERENCES produto(codigo);



----------EXERCÍCIO DE DDL - PARTE 3----------
--    1   --
ALTER TABLE pedido 
ADD CONSTRAINT ck_numero_pedido CHECK (numero BETWEEN 1 AND 99999);

--    2   --
CREATE UNIQUE INDEX ind_cnpf_pf
ON pf (cnpf DESC);

CREATE UNIQUE INDEX ind_cnpj_pj
ON pj(cnpj DESC);

--    3   --
CREATE SEQUENCE seq_item_id
START WITH 1 INCREMENT BY 2;



----------EXERCÍCIO DE DDL - PARTE 5----------
--    1   --
COMMENT ON TABLE item_produto                   IS 'Registra a interação de produtos com os pedidos.';

COMMENT ON COLUMN item_produto.codigo_pro       IS 'Chave estrangeira referente ao código do produto.';

COMMENT ON COLUMN item_produto.numero_ped       IS 'Chave estrangeira referente ao número do pedido.';

COMMENT ON COLUMN item_produto.quantidade       IS 'Armazena a quantidade de produtos por item de pedido.';

COMMENT ON COLUMN item_produto.preco_unitario   IS 'Armazena o valor unitário de cada produto.';

COMMENT ON COLUMN item_produto.valor_item       IS 'Armazena o valor somado dos produtos como o valor de um item.';




----------EXERCÍCIO DE DML - INSERT - PARTE 1----------
--    CLIENTE   --
INSERT INTO cliente 
  SELECT * FROM demo.cliente;
  
INSERT INTO fone_cliente
  SELECT * FROM demo.fone_cliente;

INSERT INTO pf
  SELECT * FROM demo.pf;
  
INSERT INTO pj
  SELECT * FORM demo.pj;
  
--    VENDEDOR    --
INSERT INTO vendedor
  SELECT * FROM demo.vendedor;
  
INSERT INTO fone_vendedor
  SELECT * FROM demo.fone_vendedor;
  
--    PRODUTO E PEDIDO    --
INSERT INTO produto
  SELECT * FROM demo.produto;
  
INSERT INTO pedido
  SELECT * FROM demo.pedido;
  
--    PRATELEIRAS E ESTOQUE   --
INSERT INTO prateleira
  SELECT * FROM demo.prateleira;
  
INSERT INTO estoque
  SELECT * FROM demo.estoque;
  
INSERT INTO capacidade_estoque
  SELECT * FROM demo.capacidade_estoque;
  
  
  
  
----------EXERCÍCIO DE DML - INSERT - PARTE 2----------
--    1   --
INSERT INTO item_produto 
  SELECT  207     AS codigo_pro,
          numero  AS numero_ped,
          100     AS quantidade,
          10.00   AS preco_unitario,
          NULL
  FROM pedido
  WHERE MOD(numero,2)=0
    AND TO_CHAR(data, 'YYYY')<2018;
    
--    2   --
INSERT INTO item_produto
  SELECT  206     AS codigo_pro,
          numero  AS numero_ped,
          50      AS quantidade,
          12.00   AS preco_unitario,
          NULL
  FROM pedido
  WHERE MOD(numero,2)!=0
    AND TO_CHAR(data, 'YYYY')=2018;
    
--    3   --
INSERT INTO item_produto
  SELECT  207     AS codigo_pro,
          numero  AS numero_ped,
          150     AS quantidade,
          14.00   AS preco_unitario,
          NULL
  FROM pedido
    WHERE MOD(numero,2)=0
      AND TO_CHAR(data, 'YYYY')=2018;

--    4   --
INSERT INTO item_produto
  SELECT  206     AS codigo_pro,
          numero  AS numero_ped,
          200     AS quantidade,
          8.00    AS preco_unitario,
          NULL
  FROM pedido
    WHERE MOD(numero,2)!=0
      AND TO_CHAR(data, 'YYYY')<2018;
      
--    5   --
INSERT INTO item_produto
  SELECT  208     AS codigo_pro,
          numero  AS numero_ped,
          80      AS quantidade,
          18.00   AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NULL
      AND nr            IS NULL
      AND bairro        IS NULL
      AND complemento   IS NULL
      AND cidade        IS NULL
      AND uf            IS NULL
      AND cep           IS NULL
      AND TO_CHAR(data, 'YYYY')=2017;
      
--    6   --
INSERT INTO item_produto
  SELECT  208     AS codigo_pro,
          numero  AS numero_ped,
          70      AS quantidade,
          20.00   AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NULL
      AND nr            IS NULL
      AND bairro        IS NULL
      AND complemento   IS NULL
      AND cidade        IS NULL
      AND uf            IS NULL
      AND TO_CHAR(data, 'YYYY')=2018;
      
--    7   --
INSERT INTO item_produto
  SELECT  202     AS codigo_pro,
          numero  AS numero_ped,
          60      AS quantidade,
          15      AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NOT NULL
      AND nr            IS NOT NULL
      AND bairro        IS NOT NULL
      AND complemento   IS NOT NULL
      AND cidade        IS NOT NULL
      AND uf            IS NOT NULL
      AND cep           IS NOT NULL
      AND MOD(TO_CHAR(prazo_entrega, 'DD'),2)!=0;
      
--    8   --
INSERT INTO item_produto
  SELECT  205     AS codigo_pro,
          numero  AS numero_ped,
          90      AS quantidade,
          11.50   AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NOT NULL
      AND nr            IS NOT NULL
      AND bairro        IS NOT NULL
      AND complemento   IS NOT NULL
      AND cidade        IS NOT NULL
      AND uf            IS NOT NULL
      AND cep           IS NOT NULL
      AND MOD(TO_CHAR(data, 'DD'),2)=0;
      
--    9   --
INSERT INTO item_produto
  SELECT  203     AS codigo_pro,
          numero  AS numero_ped,
          550     AS quantidade,
          21.35   AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NOT NULL
      AND nr            IS NOT NULL
      AND bairro        IS NOT NULL
      AND complemento   IS NOT NULL
      AND cidade        IS NOT NULL
      AND uf            IS NOT NULL
      AND cep           IS NOT NULL
      AND MOD(TO_CHAR(data, 'DD'),2)!=0;
      
--    10    --
INSERT INTO item_produto
  SELECT  204     AS codigo_pro,
          numero  AS numero_ped,
          150     AS quantidade,
          21.35   AS preco_unitario,
          NULL
  FROM pedido
    WHERE rua           IS NULL
      AND nr            IS NULL
      AND bairro        IS NULL
      AND complemento   IS NULL
      AND cidade        IS NULL
      AND uf            IS NULL
      AND cep           IS NULL
      AND MOD(TO_CHAR(data, 'DD'),2)=0;
      
      
      
      
----------EXERCÍCIO DE DML - UPDATE---------
--    1   --
UPDATE item_produto 
SET quantidade = quantidade * 2
  WHERE numero_ped<20
    AND numero_ped>50
    AND codigo_pro BETWEEN 203 AND 205;
      
--    2   --
UPDATE item_produto
SET quantidade = quantidade + 15
  WHERE numero_ped IN (SELECT numero FROM pedido
    WHERE MOD(codigo_cli,2)!=0
      AND MOD(matricula_ven,2)=0);
      
--    3   --
UPDATE item_produto
SET preco_unitario = preco_unitario - 0.50
  WHERE MOD(numero_ped,3)=0;
  
--    4   --
UPDATE item_produto
SET valor_item = preco_unitario * quantidade;

--    5   --
UPDATE pedido p
SET total_fatura = (SELECT SUM(valor_item)
                    FROM item_produto
                    WHERE numero_ped=p.numero);
                    
                    
                    
                    
---------EXERCÍCIO DE DML - DELETE----------
--    1   --     > deletar os itens dependentes da table item_produto dos pedidos correspondentes
DELETE FROM item_produto
WHERE numero_ped IN ( SELECT numero
                      FROM pedido
                      WHERE MOD(numero,2)!=0
                        AND matricula_ven = 102
                        AND rua IS NOT NULL);
                        
DELETE FROM pedido
WHERE MOD(numero,2)=1
  AND matricula_ven = 102
  AND rua IS NOT NULL;
  
SELECT * FROM pedido
WHERE MOD(numero,2)!=0
  AND matricula_ven = 102
  AND rua IS NOT NULL;
  
SELECT FROM item_produto
WHERE numero_ped IN ( SELECT numero
                      FROM pedido
                      WHERE MOD(numero,2)!=0
                        AND matricula_ven = 102
                        AND rua IS NOT NULL);
  
--    2   --
DELETE FROM item_produto
WHERE numero_ped IN ( SELECT numero
                      FROM pedido
                      WHERE data = (  SELECT MAX(data)
                                      FROM pedido)
);

SELECT * FROM item_produto
WHERE numero_ped IN ( SELECT numero
                      FROM pedido
                      WHERE data = (  SELECT MAX(data)
                                      FROM pedido)
);

--    3   --
ROLLBACK;