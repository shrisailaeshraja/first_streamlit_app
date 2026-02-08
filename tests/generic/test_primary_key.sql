{% test primary_key(model,column_name) %}

with validation as (
    select {{ column_name }} as primar_key,
    count(1) as occurrences

    from {{ model }}
    group by 1
)

select * from validation 
where occurrences > 1

{% endtest %}