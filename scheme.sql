

CREATE TABLE test_db.city ( 
	id                   int  NOT NULL    PRIMARY KEY,
	name                 varchar(100)      
 ) engine=InnoDB;


CREATE TABLE test_db.property ( 
	id                   int  NOT NULL    PRIMARY KEY,
	address              varchar(120)      ,
	id_city              int      ,
	price                bigint      ,
	description          text      ,
	year                 int      
 ) engine=InnoDB;

ALTER TABLE test_db.property ADD CONSTRAINT fk_property_city FOREIGN KEY ( id_city ) REFERENCES test_db.city( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;


CREATE TABLE test_db.inmueble_like ( 
	id                   int  NOT NULL    PRIMARY KEY,
	property_id          int      ,
	total                int      ,
	CONSTRAINT unq_inmueble_like_property_id UNIQUE ( property_id ) 
 ) engine=InnoDB;

ALTER TABLE test_db.inmueble_like ADD CONSTRAINT fk_inmueble_like_property FOREIGN KEY ( property_id ) REFERENCES test_db.property( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;


CREATE TABLE test_db.`status` ( 
	id                   int  NOT NULL    PRIMARY KEY,
	name                 varchar(32)      ,
	label                varchar(64)      
 ) engine=InnoDB;


CREATE TABLE test_db.status_history ( 
	id                   int  NOT NULL    PRIMARY KEY,
	property_id          int      ,
	status_id            int      ,
	update_date          datetime      
 ) engine=InnoDB;

ALTER TABLE test_db.status_history ADD CONSTRAINT fk_status_history_property FOREIGN KEY ( property_id ) REFERENCES test_db.property( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE test_db.status_history ADD CONSTRAINT fk_status_history_status FOREIGN KEY ( status_id ) REFERENCES test_db.`status`( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE TABLE test_db.history_like ( 
	id                   int  NOT NULL    PRIMARY KEY,
	user_id              int      ,
	inmueble_like_id     int      
 ) engine=InnoDB;

ALTER TABLE test_db.history_like ADD CONSTRAINT fk_history_like_inmueble_like FOREIGN KEY ( inmueble_like_id ) REFERENCES test_db.inmueble_like( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

