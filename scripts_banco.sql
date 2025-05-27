show databases;

CREATE database Projeto_sustentabilidade;
USE Projeto_sustentabilidade;

CREATE TABLE ProjetoDeSustentabilidade( 
  ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  DataEntrada VARCHAR (50) NOT NULL,
  LitrosConsumidos VARCHAR (50) NOT NULL,
  KWHConsumido VARCHAR (50) NOT NULL, 
  KgNaoReciclaveis VARCHAR (50) NOT NULL, 
  PorcentagemResiduos VARCHAR (50) NOT NULL, 
  MeioDeTransporte VARCHAR (250)
  );
  
CREATE TABLE Manipulacao_Dados( 
  ID_Usuario INT NOT NULL,
  Nivel_LitrosConsumidos VARCHAR (50) NOT NULL,
  Nivel_KWHConsumido VARCHAR (50) NOT NULL, 
  Nivel_KgNaoReciclaveis VARCHAR (50) NOT NULL, 
  Nivel_MeioDeTransporte VARCHAR (50) NOT NULL
  );
  
ALTER TABLE Manipulacao_Dados
ADD CONSTRAINT fk_usuario
FOREIGN KEY (ID_Usuario)
REFERENCES ProjetoDeSustentabilidade (ID);

DELETE FROM Manipulacao_Dados WHERE ID_Usuario = 4;
DELETE FROM ProjetoDeSustentabilidade WHERE ID = 5;

ALTER TABLE ProjetoDeSustentabilidade
MODIFY LitrosConsumidos FLOAT,
MODIFY KWHConsumido FLOAT,
MODIFY KgNaoReciclaveis FLOAT,
MODIFY PorcentagemResiduos FLOAT;



show tables;
SELECT * FROM projetodesustentabilidade;
SELECT * FROM manipulacao_dados; 	
SHOW DATABASES;
DROP DATABASE projetosustentabilidade;