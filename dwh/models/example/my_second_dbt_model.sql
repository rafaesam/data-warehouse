-- Active: 1660920241025@@127.0.0.1@3306

-- Use the `ref` function to select from other models

select *
from {{ ref('my_first_dbt_model') }}
where id = 1
