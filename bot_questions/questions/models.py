from django.db import models


class Question(models.Model):
    """Модель, которая отвечает за вопросы в боте."""

    content = models.CharField(verbose_name="Текст Вопроса",
                               max_length=300)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Вопрос пользователя"
        verbose_name_plural = "Вопросы пользователя"
