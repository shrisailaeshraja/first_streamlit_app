{% macro incremental_macro(column) %}

{% if is_incremental() %}

where {{ column }} > (select max({{ column }}) from {{ this }})

{% endif %}

{% endmacro %}