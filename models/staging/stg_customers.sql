{{ config(
    materialized = "table"
) }}

select
    c_custkey as customer_id,
    c_name as customer_name,
    c_nationkey as nation_id

    from {{ source('tpch','CUSTOMER') }}
