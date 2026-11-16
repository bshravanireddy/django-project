from django.contrib import admin
from .models import css, javascript, python
from .models import html

admin.site.register(python)
admin.site.register(html)
admin.site.register(css)
admin.site.register(javascript)

