-- Active: 1660920241025@@127.0.0.1@3306
{{ config(materialized='table') }}

SELECT *
 FROM  traffic_table_
where type = ' Car'
