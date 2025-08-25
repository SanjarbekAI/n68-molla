from django.db import models


class ResultModel(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    sign = models.CharField(max_length=1)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.sign} {self.num2} = {self.result}"

    class Meta:
        verbose_name = 'result'
        verbose_name_plural = 'results'
