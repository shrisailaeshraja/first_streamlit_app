{{ config(
    materialized = 'table'
) }}


select
    l_orderkey as order_id,
    l_quantity as quantity,
    l_extendedprice as price
from {{ source('tpch','LINEITEM') }}
