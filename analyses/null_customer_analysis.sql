select count(*) from {{ ref('dim_customer') }}
where customer_email is null;