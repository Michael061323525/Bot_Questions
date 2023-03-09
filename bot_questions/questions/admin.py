from django.contrib import admin
from questions.models import Question
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Регистрирует модель вопроса."""
    pass
