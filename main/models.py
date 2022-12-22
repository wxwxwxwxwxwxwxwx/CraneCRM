from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Count, Sum , Min, Max, Avg, F
from django.db.models.functions import Coalesce
from django.utils.html import format_html
 

class  Articles(models.Model):
    title = models.CharField(verbose_name ='Наименование', max_length=100)
    Unit_articles = models.CharField(verbose_name ='Ед. изм',null=True, max_length=30)
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    SummaArticles = models.FloatField(verbose_name ='Сумма', blank=True, null=True)
    Type_articles = models.BooleanField(verbose_name ='Материалы', default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "справочник статей"
        verbose_name_plural = "Справочник статьи"

        
class  Document(models.Model):
    number = models.CharField(verbose_name ='Номер документа', max_length=100)
    document_date = models.DateTimeField(null=True,verbose_name = 'Дата документа')
    Summa_total_Client = models.FloatField(verbose_name='Итого по сумме для клиента',null=True,blank=True)
    Summa_total_Articles = models.FloatField(verbose_name='Итого по сумме статьей',null=True,blank=True)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

        
    def save(self, *args, **kwargs):
        aggregate_summ_articles = ExpensisInDocument.objects.filter(Document = self).aggregate(Sum('Summa')) 
        aggregate_summ_total = ExpensisInDocument.objects.filter(Document = self).aggregate(Sum('Summatotal')) 
        self.Summa_total_Articles = aggregate_summ_articles['Summa__sum']
        self.Summa_total_Client = aggregate_summ_total['Summatotal__sum']
        super().save(*args, **kwargs) 

          
        
class  ExpensisInDocument(models.Model):
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    Articles = models.ForeignKey('Articles', on_delete = models.DO_NOTHING, verbose_name = 'Статья', null=True)
    Unit = models.CharField(verbose_name = 'Ед.изм', max_length=5, null=True)
    Summa = models.FloatField(verbose_name='Сумма внутреннего учета', blank=True, null=True)
    Volume = models.FloatField(verbose_name='Объем',  null=True)
    Summaclient = models.FloatField(verbose_name='Сумма для клиента',null=True)
    Summatotal = models.DecimalField(verbose_name='Сумма итого',null=True,decimal_places=1 ,max_digits=30,blank=True,)
    class Meta:
        verbose_name = "Статья в документах"
        verbose_name_plural = "Статьи в документах"
        
    def save(self, *args, **kwargs):
        self.Summatotal = self.Volume * self.Summaclient
        super().save(*args, **kwargs)
        return self.Summatotal

       

          
class  Payment(models.Model):
    number = models.PositiveBigIntegerField(verbose_name ='Номер')
    date = models.DateTimeField(null=True, blank=True, verbose_name = 'Дата документа')
    summ_plan = models.FloatField(verbose_name ='Сумма план')
    date_plan = models.DateField(null=True, blank=True, verbose_name = 'Дата план')
    summ_fact = models.FloatField(verbose_name ='Сумма факт')
    date_fact =  models.DateField(null=True, blank=True, verbose_name = 'Дата факт')
    class Meta:
        verbose_name = "Платежи"
        verbose_name_plural = "Платежи"



    @property
    def colored_state(self):
        color = ''
        name = ''
        if self.summ_plan <= self.summ_fact:
            color = 'blue'
            name = 'Успех'
        if self.summ_plan >= self.summ_fact:
            color = 'red'
            name = 'Минус'

        return format_html(
                '<small style="padding: 3px; border-radius: 3px; background-color: {}; color: white; white-space: nowrap;">{}</small>',
                color,
                name,
            )    
    colored_state.fget.short_description = 'Статус'            


class ExpensisInPayment(models.Model):
    Payment = models.ForeignKey('Payment', on_delete = models.DO_NOTHING, verbose_name = 'Платежи',null=True)
    Articles = models.ForeignKey('Articles', on_delete = models.DO_NOTHING, verbose_name = 'Статья', null=True)
    Document = models.ForeignKey('Document', on_delete = models.PROTECT,db_constraint=False, verbose_name = 'Документ',null=True)
    Summa_total = models.DecimalField(max_length=30,max_digits=10, decimal_places=3, verbose_name = 'Сумма',null=True)
    Summa_total_client = models.DecimalField(max_length=30,max_digits=10, decimal_places=3, verbose_name  ='Сумма клиент',null=True)
    class Meta:
        verbose_name = "Статья в платеже"
        verbose_name_plural = "Статьи в платеже"   

            
class Customer(models.Model):
    Name = models.CharField(verbose_name ='Наименование клиента', max_length=200, null=True)
    Full_director = models.CharField(verbose_name ='Директор', max_length=200, null=True)
    Phone = models.CharField(max_length=200,verbose_name = 'Телефон', null=True)
    Email = models.EmailField(max_length=200,verbose_name = 'Email', null=True)
    Date_created = models.DateTimeField(auto_now_add=True,verbose_name = 'Дата созания', null=True)
    Address = models.CharField(max_length=200,verbose_name = 'Адресс юредический', null=True)
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    Ks = models.BigIntegerField(verbose_name ='К/C',  null=True)
    Rs = models.BigIntegerField(verbose_name ='Р/С',  null=True)
    Inn = models.BigIntegerField(verbose_name ='ИНН',  null=True)
    Kpp = models.BigIntegerField(verbose_name ='КПП',  null=True)
    Bik = models.BigIntegerField(verbose_name ='БИК',null=True)
    Bank =  models.CharField(max_length=200,verbose_name = 'Банк', null=True)
    Addressk = models.CharField(max_length=200,verbose_name = 'Адресс корреспонденции', null=True)
    Director = models.CharField(max_length=200,verbose_name = 'Фамилия И.О руководителя', null=True)
    file = models.FileField(upload_to='chapters/%Y/%m/%D',blank = True, max_length=100000, null=True, verbose_name = 'Договор') 
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Клиент ЮР"
        verbose_name_plural = "Клиенты ЮР"  


class Customer_ip(models.Model):
    Name = models.CharField(verbose_name ='ФИО предпринимателя', max_length=200, null=True)
    Phone = models.CharField(max_length=200,verbose_name = 'Телефон', null=True)
    Email = models.EmailField(max_length=200,verbose_name = 'Email', null=True)
    Date_created = models.DateTimeField(auto_now_add=True,verbose_name = 'Дата созания', null=True)
    Address = models.CharField(max_length=200,verbose_name = 'Адресс юредический', null=True)
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    Ks = models.BigIntegerField(verbose_name ='К/C',   null=True)
    Rs = models.BigIntegerField(verbose_name ='Р/С',  null=True)
    Inn = models.BigIntegerField(verbose_name ='ИНН',  null=True)
    Ogrnip = models.BigIntegerField(verbose_name ='ОГРН ИП',  null=True)
    Bik = models.BigIntegerField(verbose_name ='БИК',null=True)
    Bank =  models.CharField(max_length=200,verbose_name = 'Банк', null=True)
    Addressk = models.CharField(max_length=200,verbose_name = 'Адресс корреспонденции', null=True)
    Director = models.CharField(max_length=200,verbose_name = 'Фамилия И.О руководителя', null=True)
    file = models.FileField(upload_to='chapters/%Y/%m/%D',blank = True, max_length=100000, null=True, verbose_name = 'Договор') 
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Клиент ИП"
        verbose_name_plural = "Клиенты ИП" 


class Customer_fiz(models.Model):
    Name = models.CharField(verbose_name ='ФИО физического лица', max_length=200, null=True)
    Phone = models.CharField(max_length=200,verbose_name = 'Телефон', null=True)
    Email = models.EmailField(max_length=200,verbose_name = 'Email', null=True)
    Date_created = models.DateTimeField(auto_now_add=True,verbose_name = 'Дата созания', null=True)
    Address = models.CharField(max_length=200,verbose_name = 'Адрес регистрации', null=True)
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    Issued_by =  models.CharField(max_length=200,verbose_name = 'Кем выдан паспорт', null=True)
    Rs = models.BigIntegerField(verbose_name ='Р/С',  null=True)
    Seria = models.BigIntegerField(verbose_name ='Серия',  null=True)
    Nomer = models.BigIntegerField(verbose_name ='Номер',  null=True)
    Inn = models.BigIntegerField(verbose_name ='ИНН',  null=True)
    Bik = models.BigIntegerField(verbose_name ='БИК',null=True)
    Bank =  models.CharField(max_length=200,verbose_name = 'Банк', null=True)
    Director = models.CharField(max_length=200,verbose_name = 'Фамилия И.О физического лица', null=True)
    file = models.FileField(upload_to='chapters/%Y/%m/%D',blank = True, max_length=100000, null=True, verbose_name = 'Договор') 
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Клиент Физ"
        verbose_name_plural = "Клиенты Физ"         
        

class  Finance(models.Model):
    STATUS = (
        ('plan', 'План'),
        ('fact', 'Факт'),
    )
    status = models.CharField(max_length=15,verbose_name='Тип платежа', default='approval', choices=STATUS)
    summa = models.FloatField(verbose_name ='Сумма',null=True,blank = True,)
    title = models.CharField(verbose_name ='Наименование',blank = True, max_length=100)
    Document = models.ForeignKey('Document', on_delete = models.DO_NOTHING, verbose_name = 'Документ',null=True)
    date = models.DateField(null=True, verbose_name = 'Дата')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Платеж от клиентов"
        verbose_name_plural = "Платежи от клиентов"

class OrderReport(models.Model):
    Name = models.CharField(verbose_name ='Название отчета', max_length=200, null=True)
    date_at = models.DateField(null=True, blank=True, default=None, verbose_name = 'Дата  от')
    date_to = models.DateField(null=True, blank=True, default=None, verbose_name = 'Дата  до')
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "План/Факт анализ"
        verbose_name_plural = "План/Факт анализ"        









    