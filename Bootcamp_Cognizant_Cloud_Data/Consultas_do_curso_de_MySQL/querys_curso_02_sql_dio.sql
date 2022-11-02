/* Conteudo curso 2 de MySQL da dio */

USE mysql_dio;

/* Criando Tabelas */
CREATE TABLE videos (
	id_video INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    author VARCHAR(30),
    title VARCHAR(30),
    likes INT,
    dislikes INT
);

CREATE TABLE author (
	id_author INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    born DATE
);

CREATE TABLE seo (
	id_seo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(30)
);

CREATE TABLE playlist (
	id_playlist INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name_pl VARCHAR(30)
);

CREATE TABLE videos_playlist(
	id_vp INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fk_videos INT,
    fk_playlist INT
);

/* Inserindo valores nas Tabelas */
INSERT INTO videos (author, title, likes, dislikes) VALUES('Edyane', 'Sobre Clube da luta', 1342, 3);
INSERT INTO videos (author, title, likes, dislikes) VALUES('Lucas', 'Machine Learning', 530, 15);
INSERT INTO videos (author, title, likes, dislikes) VALUES('Edyane', 'HTML e CSS', 521, 10);
INSERT INTO videos (author, title, likes, dislikes) VALUES('Luiz', 'Boku no hero', 324, 5);
INSERT INTO videos (author, title, likes, dislikes) VALUES('Lucas', 'Fabrica de donuts', 589, 2);
INSERT INTO videos (fk_author, title, likes, dislikes) VALUES(2, 'Wim hof', 219, 12);

INSERT INTO author (name, born) VALUES ('Edyane', '1995/01/04');
INSERT INTO author (name, born) VALUES ('Lucas', '2000/10/09');
INSERT INTO author (name, born) VALUES ('Luiz', '2009/05/02');
INSERT INTO author (name, born) VALUES ('Alves', '2001/08/22');

INSERT INTO seo (category) VALUES ('Programação');
INSERT INTO seo (category) VALUES ('Filmes/Animes');
INSERT INTO seo (category) VALUES ('Videos');

INSERT INTO playlist(name_pl) VALUES ('Passatempo');
INSERT INTO playlist(name_pl) VALUES ('Estudo');
INSERT INTO playlist(name_pl) VALUES ('Mix de videos');

INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(1 ,1) ;
INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(4 ,1) ;
INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(2 ,2) ;
INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(3 ,2) ;
INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(5 ,3) ;
INSERT INTO videos_playlist(fk_videos, fk_playlist) VALUES(6 ,3) ;

/* Select das Tabelas */
SELECT * FROM videos;
SELECT * FROM author; 
SELECT * FROM seo;
SELECT * FROM playlist;
SELECT * FROM videos_playlist;
SELECT * FROM videos JOIN author ON videos.fk_author = author.id_author;
SELECT videos.title , author.name FROM videos JOIN author ON videos.fk_author = author.id_author;
SELECT * FROM videos JOIN seo on videos.fk_seo = seo.id_seo;
SELECT videos.title, seo.category FROM videos JOIN seo on videos.fk_seo = seo.id_seo;
SELECT videos.title, seo.category, author.name FROM videos JOIN seo on videos.fk_seo = seo.id_seo
	JOIN author on videos.fk_author = author.id_author;
SELECT * from playlist JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
	JOIN videos ON videos.id_video = videos_playlist.fk_videos;
SELECT playlist.name_pl, videos.title FROM playlist 
	JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
	JOIN videos ON videos.id_video = videos_playlist.fk_videos;
    
SELECT playlist.name_pl, videos.title, author.name
	FROM playlist 
	JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
	JOIN videos ON videos_playlist.fk_videos = videos.id_video
    JOIN author ON author.id_author = videos.fk_author;

/*--------------------*/

/* Updates do database */
SET SQL_SAFE_UPDATES=0;
UPDATE videos SET author=' ';
UPDATE videos set author = 1 WHERE id_video=1;
UPDATE videos set author = 1 WHERE id_video=3;
UPDATE videos set author = 1 WHERE id_video=5;
UPDATE videos set author = 2 WHERE id_video=2;
UPDATE videos set author = 3 WHERE id_video=4;
UPDATE videos set fk_seo = 2  WHERE id_video=1;
UPDATE videos set fk_seo = 1  WHERE id_video=2;
UPDATE videos set fk_seo = 1  WHERE id_video=3;
UPDATE videos set fk_seo = 2 WHERE id_video=4;
UPDATE videos set fk_seo = 3 WHERE id_video=5;
UPDATE videos set fk_seo = 3 WHERE id_video=6;

UPDATE playlist set fk_author = 4 Where id_playlist = 1;
UPDATE playlist set fk_author = 2 Where id_playlist = 2;
UPDATE playlist set fk_author = 1 Where id_playlist = 3;

/* alterações na tabela */
alter table videos drop column author;
alter table videos add column author INT after id_video;
alter table videos change `author` `fk_author` INT not null;
alter table `videos` add CONSTRAINT `fk_author` 
	foreign key(`fk_author`) 
	REFERENCES `author`(`id_author`)
    ON DELETE CASCADE ON UPDATE CASCADE;
alter table `videos` add `fk_seo` INT NOT NULL AFTER `title`;
alter table `videos` ADD CONSTRAINT `fk_seo`
	FOREIGN KEY (`fk_seo`)
    REFERENCES `seo` (`id_seo`)
	ON DELETE CASCADE ON UPDATE CASCADE;
alter table `playlist` add `fk_author` int not null;






