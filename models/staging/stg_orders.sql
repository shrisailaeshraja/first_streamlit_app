{{ config(
    materialized = "table") }}

Select
    o_orderkey as order_id,
    o_custkey as customer_id,
    o_orderdate as order_date,
    o_totalprice as total_price
from {{ source('tpch','ORDERS') }}