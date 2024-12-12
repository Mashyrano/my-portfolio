from django.contrib import admin
from Base.models import About
from Base.models import Skill
from Base.models import Education
from Base.models import Project


# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)