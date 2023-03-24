-- create a SQL script to create the Postgres database and enable the PostGIS extension.

CREATE DATABASE mydatabase;
\c mydatabase

CREATE EXTENSION postgis;
