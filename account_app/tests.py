from django.test import TestCase

# Create your tests here.
{% extends 'base.html' %}
{% load static %}
{% block title %}
 edit account
{% endblock %}

{% block content %}
<div class="container mt-5">
    <h2 class="mb-4"> وایرایش اطلاعات کاربری</h2>
    <form action="" method="post">
        {% csrf_token %}
        <div class="form-group mb-3">
            {{myform3.username.label_tag}}
            {{myform3.username}}
        </div>
        <div class="form-group mb-3">
            {{myform3.first_name.label_tag}}
            {{myform3.first_name}}
        </div>
        <div class="form-group mb-3">
            {{myform3.last_name.label_tag}}
            {{myform3.last_name}}
        </div>
        <div class="form-group mb-3">
            {{myform3.email.label_tag}}
            {{myform3.email}}
        </div>
        <button type="submit" class="btn btn-success">ذخیره</button>
    </form>
</div>
{% endblock %}