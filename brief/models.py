from django.db import models
from multiselectfield import MultiSelectField

class Ecommerce(models.Model):

    GOODS_QUANTITY_CHOICES = [
        "100", "500", "1000", "10000", "100000", "другое"
    ]
    GQ_CHOICES = sorted([(item, item) for item in GOODS_QUANTITY_CHOICES])
    MONEY_CHOICES = [
        "Рубли", "Доллары", "Евро", "Другое"
    ]
    M_CHOICES = sorted([(item, item) for item in MONEY_CHOICES])
    EXCHANGE_RATE_CHOICES = [
        "Вручную", "Автоматически", "Другое"
    ]
    ER_CHOICES = sorted([(item, item) for item in EXCHANGE_RATE_CHOICES])
    DISCOUNT_TYPE_CHOICES = [
        "По группам пользователей", "Промокоды", "Накопительные скидки", 
        "Скидки от суммы заказа", "На группы товаров", "Другое"
    ]
    DT_CHOICES = sorted([(item, item) for item in DISCOUNT_TYPE_CHOICES])
    REGISTRATION_NEED_CHOICES = [
        "Нет, достаточно корзины для незарегистрированного пользователя", "Регистрация по e-mail",
          "Регистрация по sms", "Другое"
    ]
    RN_CHOICES = sorted([(item, item) for item in REGISTRATION_NEED_CHOICES])
    PAY_TYPE_CHOICES = [
        "Онлайн-оплата", "По счету", "Квитанция", "Наличным курьеру", "Другое"
    ]
    PT_CHOICES = sorted([(item, item) for item in PAY_TYPE_CHOICES])
    DELIEVERY_TYPE_CHOICES = [
        "Самовывоз", "Транспортная компания", "Свои пункты выдачи", "Другое"
    ]
    DelT_CHOICES = sorted([(item, item) for item in DELIEVERY_TYPE_CHOICES])
    ORDER_PRIEM_CHOICES = [
        "Заказы поступают на email менеджера и вся дальнейшая обработка заказов ведется в оффлайн режиме",
        "На email менеджера поступает уведомление, а обработка заказов ведется на сайте ",
        "Интеграция с другими системами",
        "Другое"
    ]
    OP_CHOICES = sorted([(item, item) for item in ORDER_PRIEM_CHOICES])
    UTOCHNENIE_CHOICES = [
        ('1', "Новости\Блог"), ('2', "Контактная информация"), ('3',"Интерактивная карта проезда"),('4', "Статьи (полезная информация)"),
        ('5',"Индивидуальные параметры товаров для каждой группы (длина, ширина, высота и тд)"),
        ('6', "Онлайн-оплата товаров"), ('7', "Корзина покупок"), ('8', "Сравнение товаров в интернет-магазине"),
        ('9', "WishList (Список желаний)"), ('10',"Поиск по сайту"), ('11', "Поиск товаров по параметрам"),
        ('12', "Акции"), ('13',"Скидки"), ('14',"Банеры"), ('15',"Партнеры"), ('16',"Онлайн-консультант"), ('17',"Онлайн-заявки и формы заказа с сайта"),
        ('18',"Интеграция сайта с социальными сетями"), ('19',"Геопривязка к городам"), 
        ('20',"Онлайн-формирование документов (счетов для оплаты и прочее)"), ('21',"Печать чеков")

        ]
    DESIGN_CHOICES = [
        "Логотип", "Фирменный стиль, брэндбук", "Цветовая гамма", "Фото, видео, другое", "Другое"
    ]
    D_CHOICES = sorted([(item, item) for item in DESIGN_CHOICES])
    company_name = models.CharField(max_length=200)
    old_site = models.CharField(max_length=200)
    orientation = models.TextField() #направление интернет-магазина
    trading = models.TextField() #вид торговли
    advantages = models.TextField() #конкурентные преимущества
    competitors = models.TextField() #конкуренты
    #количество товаров
    customers = models.TextField() #целевая аудитория покупателей
    locations = models.TextField() #какой охват территории
    trade_object = models.TextField() #предмет продажи
    goods_quantity = models.CharField(max_length=200, choices = GQ_CHOICES, default ="100")
    category_quantity = models.TextField() #количество категорий
    characters_item = models.TextField() #характеристики товаров

    #цены и скидки
    money = models.CharField(max_length=200, choices= M_CHOICES, default = "Рубли")
    Setup_exchange_rate = models.CharField(max_length=200, choices=ER_CHOICES, default = "Вручную")
    price_type = models.TextField()
    discount_type = models.CharField(max_length=200, choices=DT_CHOICES, default="По группам пользователей")

    #регистрация покупателей
    registration_need = models.CharField(max_length=200, choices=RN_CHOICES, default= "Регистрация по e-mail")
    #оплата
    pay_type = models.CharField(max_length=200, choices=PT_CHOICES, default="Онлайн-оплата")
    #доставка
    type_delievery = models.CharField(max_length=200, choices= DelT_CHOICES, default="Транспортная компания")

    #обработка заказов
    order_priem = models.CharField(max_length=200, choices=OP_CHOICES)

    #дополнительная функциональность
    utochnenie = MultiSelectField(max_length=255, choices=UTOCHNENIE_CHOICES, max_choices=10)

    #дизайн
    design = MultiSelectField(max_length=255, choices =D_CHOICES,max_choices=5)
    
    good_examples = models.TextField()
    bad_examples = models.TextField()
    additional_wishes = models.TextField()
    wish_work_hours = models.TextField()
    files = models.FileField(upload_to='files/')

    #контактная информация
    name = models.TextField()
    phone_number = models.TextField()
    e_mail = models.EmailField()
    soglasie = models.BooleanField(default=False)
    def __str__(self):
        return self.company_name
    
class test(models.Model):
    files = models.FileField()
# Create your models here.
