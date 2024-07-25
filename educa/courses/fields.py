from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        # Сохраняем список полей, по которым будет производиться фильтрация
        self.for_fields = for_fields
        # Инициализация родительского класса
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        # model_instance - экземпляр модели, который мы пытаемся сохранить
        # self.attname - это поле order в этой модели
        # Если значение для поля order не было задано, устанавливаем сами
        if getattr(model_instance, self.attname) is None:
            try:
                # Получаем все объекты модели, экземпляр которой хотим сохр-ть
                qs = self.model.objects.all()
                # Если поля для фильтрации заданы
                if self.for_fields:
                    # создаем словарь с названием полей из for_fields
                    # и значений из создаваемого экземпляра модели.
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    # фильтруем объекты модели по данному словарю
                    qs = qs.filter(**query)
                # Находим объект с наибольшим значением для текущего поля
                last_item = qs.latest(self.attname)
                # Определяем значение для order last_item + 1
                value = last_item.order + 1
            except ObjectDoesNotExist:
                # Если нет объектов, определяем значение для order -> 0
                value = 0
            # Устанавливаем значение для order
            setattr(model_instance, self.attname, value)
            return value
        else:
            # Если значение order было задано, вызываем метод родит класса
            return super().pre_save(model_instance, add)

