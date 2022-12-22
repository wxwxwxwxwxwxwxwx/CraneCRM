from django.contrib import admin
from django.http import FileResponse
from . models import ExpensisInDocument,Customer,ExpensisInPayment,Payment,Document,Finance,Articles,Customer_ip,Customer_fiz,OrderReport
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from docxtpl import DocxTemplate
from django.http import  HttpResponse
from django.http import FileResponse
import io
from io import BytesIO
import datetime
import csv
from main.number_to_char import num2text, decimal2text
import decimal
import pandas as pd
import os 
from django.utils.html import format_html


@admin.action(description='Скачать документ Юр')
def make_published(modeladmin, request, queryset):
    buffer = generate_document(queryset)
    #return FileResponse (buffer, as_attachment=True, filename = 'template_ur.docx')
    return FileResponse(open('generated_ur.docx', 'rb'))
#Договор для юр.
def generate_document(queryset):
    document = queryset[0]
    expensisInDocument = ExpensisInDocument.objects.filter(Document = document)
    customer = Customer.objects.filter(Document = document)     
    doc = DocxTemplate("template.docx")
    int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
    exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')
    sum_client = decimal2text(
                decimal.Decimal(str(document.Summa_total_Client)),
                int_units=int_units,
                exp_units=exp_units)



    context = {
        "number": document.number,
        "document_date": document.document_date.strftime("%d.%m.%Y"),
        "Address" : customer[0].Address,
        "Phone" : customer[0].Phone,
        "Email" : customer[0].Email,
        "Ks" : customer[0].Ks,
        "Rs" : customer[0].Rs,
        "Inn" : customer[0].Inn,
        "Kpp" : customer[0].Kpp,
        "Bik" : customer[0].Bik,
        "Bank" : customer[0].Bank,
        "Addressk" : customer[0].Addressk,
        "Director" : customer[0].Director,
        "Name" : customer[0].Name, 
        "sum_client": sum_client,
        "SummaclientClient": document.Summa_total_Client,
        "Articles": expensisInDocument[0].Articles,
        "Unit": expensisInDocument[0].Unit,
        "Summa": expensisInDocument[0].Summa,
        "Volume": expensisInDocument[0].Volume,
        "Summaclient": expensisInDocument[0].Summaclient,
        "Summatotal": expensisInDocument[0].Summatotal,
        'expensis': expensisInDocument

    }
   
    
    doc.render(context)
    #doc.save("generated_ur.docx")
   
   
#Документ ИП 
@admin.action(description='Скачать договор ИП')
def make_published_ip(modeladmin, request, queryset):
    buffer = generate_document_ip(queryset)
    #return FileResponse (buffer, as_attachment=True, filename = 'template.docx')
    return FileResponse(open('generated_ur.docx', 'rb'))
def generate_document_ip(queryset):
    document = queryset[0]
    expensisInDocument = ExpensisInDocument.objects.filter(Document = document)
    customer = Customer_ip.objects.filter(Document = document)     
    doc = DocxTemplate("template_ip.docx") 
    context = {
        "number": document.number,
        "document_date": document.document_date.strftime("%d.%m.%Y"),
        "Address" : customer[0].Address,
        "Phone" : customer[0].Phone,
        "Email" : customer[0].Email,
        "Ks" : customer[0].Ks,
        "Rs" : customer[0].Rs,
        "Inn" : customer[0].Inn,
        "Ogrnip" : customer[0].Ogrnip,
        "Bik" : customer[0].Bik,
        "Bank" : customer[0].Bank,
        "Addressk" : customer[0].Addressk,
        "Director" : customer[0].Director,
        "Name" : customer[0].Name, 
        "SummaclientClient": document.Summa_total_Client,
        "Articles": expensisInDocument[0].Articles,
        "Unit": expensisInDocument[0].Unit,
        "Summa": expensisInDocument[0].Summa,
        "Volume": expensisInDocument[0].Volume,
        "Summaclient": expensisInDocument[0].Summaclient,
        "Summatotal": expensisInDocument[0].Summatotal,
        'expensis': expensisInDocument

    }

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "template_ip.docx"

    doc_io = io.BytesIO() # create a file-like object
    doc.save(doc_io) # save data to file-like object
    doc_io.seek(0) # go to the beginning of the file-like object
        
    doc.render(context)
    doc.save("generated_ip.docx")


#Документ Физ лица
@admin.action(description='Скачать договор Физ')
def make_published_fiz(modeladmin, request, queryset):
    buffer = generate_document_fiz(queryset)
    #return FileResponse (buffer, as_attachment=True, filename = 'template.docx')
def generate_document_fiz(queryset):
    document = queryset[0]
    expensisInDocument = ExpensisInDocument.objects.filter(Document = document)
    customer = Customer_fiz.objects.filter(Document = document)      
    doc = DocxTemplate("template_fiz.docx") 
    context = {
        "number": document.number,
        "document_date": document.document_date.strftime("%d.%m.%Y"),
        "Address" : customer[0].Address,
        "Phone" : customer[0].Phone,
        "Email" : customer[0].Email,
        "Ks" : customer[0].Ks,
        "Rs" : customer[0].Rs,
        "Inn" : customer[0].Inn,
        "Kpp" : customer[0].Kpp,
        "Bik" : customer[0].Bik,
        "Bank" : customer[0].Bank,
        "Addressk" : customer[0].Addressk,
        "Director" : customer[0].Director,
        "Name" : customer[0].Name, 
        "SummaclientClient": document.Summa_total_Client,
        "Articles": expensisInDocument[0].Articles,
        "Unit": expensisInDocument[0].Unit,
        "Summa": expensisInDocument[0].Summa,
        "Volume": expensisInDocument[0].Volume,
        "Summaclient": expensisInDocument[0].Summaclient,
        "Summatotal": expensisInDocument[0].Summatotal,
        'expensis': expensisInDocument

    }

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = "template_fiz.docx"

    doc_io = io.BytesIO() # create a file-like object
    doc.save(doc_io) # save data to file-like object
    doc_io.seek(0) # go to the beginning of the file-like object
        
    doc.render(context)
    doc.save("generated_fiz.docx")



@admin.action(description='Скачать таблицу excel')
def generate_excel(modeladmin, request, queryset):
    document = queryset[0]
    expensisInDocument = ExpensisInDocument.objects.filter(Document = document)

    with open('names.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['Статья', 'Ед.изм','Объем','Сумма','Сумма итого'])
        print(expensisInDocument)
        for expensis in expensisInDocument:
            print(expensis)
            spamwriter.writerow([expensis.Articles,str(expensis.Unit).replace('.',','),str(expensis.Volume).replace('.',','),str(expensis.Summaclient).replace('.',','),str(expensis.Summatotal).replace('.',',')])
        
        spamwriter.writerow(['','','','Итого:', str(document.Summa_total_Client).replace('.',',')])
        
    return FileResponse(open('names.csv', 'rb'))
    



class ExpensisInDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Document', 'Articles',  'Summa')
    list_display_links = ('id', 'Document', 'Articles')
    

class CustomerAdmin(admin.ModelAdmin):
    model = Customer


class Customer_ipAdmin(admin.ModelAdmin):
    model = Customer_ip


class Customer_fizAdmin(admin.ModelAdmin):
    model = Customer_fiz
    

class ExpensisInPaymentInline(admin.TabularInline):
    model = ExpensisInPayment


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    inlines = [ExpensisInPaymentInline]
    list_display = ('number', 'date', 'summ_plan', 'date_plan', 'summ_fact', 'date_fact','colored_state')
    list_display_links = ('number', 'date', 'summ_plan', 'date_plan', 'summ_fact', 'date_fact')
    

class ExpensisInDocumentInline(admin.TabularInline):
    model = ExpensisInDocument
    

class DocumentAdmin(admin.ModelAdmin):
    #change_form_template = "admin_change_form_document_ready.html"
    model = Document
    inlines = [ExpensisInDocumentInline]
    actions = [make_published, generate_excel, make_published_ip, make_published_fiz]
    pass


class FinanceAdmin(ImportExportModelAdmin):
    model = Finance
    list_display = ( 'Document','summa','status', 'date')
    pass

#plan_fact
@admin.action(description='Скачать план/факт анализ')
def generate_plan_fact(modeladmin, request, queryset):
    document = queryset[0]
    expensisInDocument = ExpensisInDocument.objects.filter(Document = document)

    with open('names.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['Статья', 'Ед.изм','Объем','Сумма','Сумма итого'])
        print(expensisInDocument)
        for expensis in expensisInDocument:
            print(expensis)
            spamwriter.writerow([expensis.Articles,str(expensis.Unit).replace('.',','),str(expensis.Volume).replace('.',','),str(expensis.Summaclient).replace('.',','),str(expensis.Summatotal).replace('.',',')])
        
        spamwriter.writerow(['','','','Итого:', str(document.Summa_total_Client).replace('.',',')])
        
    return FileResponse(open('names.csv', 'rb'))


class OrderReportAdmin(admin.ModelAdmin):
    model = OrderReport
    list_display = ( 'date_at','date_to')
    list_editable = ('date_at','date_to')
    actions = [generate_plan_fact]
    pass




       
    

admin.site.register(Payment, PaymentAdmin)    
admin.site.register(Articles)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Customer)
admin.site.register(Customer_ip)
admin.site.register(Customer_fiz)
admin.site.register(ExpensisInDocument, ExpensisInDocumentAdmin)
admin.site.register(Finance, FinanceAdmin)
admin.site.register(OrderReport)

