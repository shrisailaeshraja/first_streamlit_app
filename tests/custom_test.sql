{{ config(
    severity = 'error'
) }}

select customer_id,count(*) from {{ ref("fact_order_incremental") }} 
group by 1
having count(*) > 1
