from django import template 
import datetime 
register = template.Library()

def cutter(value, arg): 
    return value[:arg] 
register.filter('mytruncate', cutter) 


@ register.simple_tag 
def current_time(format_string): 
    return datetime.datetime.now().strftime(format_string) 