{{ config(
    materialized = 'table'
) }}


select
    c.customer_id,
    c.customer_name,
    c.nation_id,
    cm.country_name

    from {{ ref("stg_customers") }} c
    left join {{ ref("country_mapping") }} cm
   on c.nation_id = cm.nation_id