from django.db import models #

class News(models.Model): #
    title = models.CharField(max_length=255) #заголовок (типа varchar) только на django как charfield
    content = models.TextField(blank=True) #контент поле-текстовое
    created_on = models.DateTimeField(auto_now_add=True) #дата создания базы данных
    update_on = models.DateTimeField(auto_now=True) #
    status = models.BooleanField(default=False) #по стоку идет True (по умолчанию)
    photo = models.ImageField(upload_to="") #загрузка фотографии по пути "..."
