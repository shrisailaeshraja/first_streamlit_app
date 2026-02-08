{% macro select_cols(col_list) %}

{% for cols in col_list %}
{{cols}}{% if not loop.last() %},{% endif %}

{% endfor %}


{% endmacro %}