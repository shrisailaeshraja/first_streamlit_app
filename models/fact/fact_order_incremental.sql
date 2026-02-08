{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
) }}

with orders as (

    select *
    from {{ ref('stg_orders') }}

),

lineitems as (

    select *
    from {{ ref('stg_lineitems') }}

),

order_metrics as (

    select
        o.order_id,
        o.customer_id,
        o.order_date,
        o.total_price,

        sum(l.quantity) as total_quantity,
        sum(l.price) as total_lineitem_price

    from orders o
    left join lineitems l
        on o.order_id = l.order_id

    group by
        o.order_id,
        o.customer_id,
        o.order_date,
        o.total_price
)

select *
from order_metrics

{{ incremental_macro('order_date') }}