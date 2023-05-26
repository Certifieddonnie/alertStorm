-- A Script to setup your database.
-- MySQL Server

CREATE DATABASE weatheralert CHARACTER SET UTF8;

CREATE USER admin@localhost IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON weatheralert.* TO admin@localhost;

FLUSH PRIVILEGES;