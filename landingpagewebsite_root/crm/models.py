from django.db import models

# Create your models here.
class StatusCrm(models.Model):
      Status_name = models.CharField(max_length=200, verbose_name='Название статуса')


def __str__(self):
    return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=20, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete= models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Тексте комента')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата комента')

    def __str__(self):
        return self.ComentCrm

    class Meta:
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменты'