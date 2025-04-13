from django.utils.safestring import SafeString
from django.utils.html import escape

safe_string:  SafeString = SafeString('<strong>Hello</strong>')
print(safe_string)

unsafe_string: str = '<strong>Hello</strong>'
print(escape(unsafe_string))