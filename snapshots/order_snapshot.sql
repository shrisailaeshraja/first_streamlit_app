{% snapshot order_snapshot  %}

{{ config(
    target_schema = 'DBT_SCHEMA',
    unique_key = 'order_id',
    strategy = 'timestamp',
    updated_at = 'order_date'
) }}


select * from {{ ref("stg_orders") }}


{% endsnapshot %}