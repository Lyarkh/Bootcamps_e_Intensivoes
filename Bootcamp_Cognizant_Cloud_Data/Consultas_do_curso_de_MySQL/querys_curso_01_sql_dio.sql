/* conteudo do curso introdutório de MySQL */


USE mysql_dio; /* para selecionar o banco de dados */

CREATE TABLE pessoas(
	nome VARCHAR(20),
    nascimento DATE
);

INSERT INTO pessoas(nome, nascimento) VALUES ("Nathally", "1990-05-22");

INSERT INTO pessoa(nome, nascimento) VALUES ("Lucas", "2000/10/09");
INSERT INTO pessoa(nome, nascimento) VALUES ("Edyane", "1995/01/04");
INSERT INTO pessoa(nome, nascimento) VALUES ("Luiz", "2009/05/02");
INSERT INTO pessoa(nome, nascimento) VALUES ("Claudio", "2003/12/12");
INSERT INTO pessoa(nome, nascimento) VALUES ("Fernado", "1951/12/1");

select * from pessoa;

delete from pessoa where id=3;

update pessoa set nome ='Lucas Emanuel' where id=4;

select * from pessoa order by nome; /* para pegar de forma decrescente utilize ´desc´ */

ALTER TABLE `pessoa` ADD `genero` VARCHAR(1) NOT NULL AFTER `nascimento`;

UPDATE  pessoa SET genero='F' WHERE id=1;
UPDATE  pessoa SET genero='F' WHERE id=5;
UPDATE  pessoa SET genero='M' WHERE id=4;
UPDATE  pessoa SET genero='M' WHERE id=6;
UPDATE  pessoa SET genero='M' WHERE id=7;
UPDATE  pessoa SET genero='M' WHERE id=8;

SELECT COUNT(id), genero from pessoa GROUP BY genero;



