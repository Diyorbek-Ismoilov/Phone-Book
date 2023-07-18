from django.http import HttpResponse
from .models import Contact


def download_xml(request):
    # Генерация XML-файла
    xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_data += '<ContactData>\n'
    xml_data += '    <Group Id="1" Name="Default" Ring="Auto" Description="">\n'

    contacts = Contact.objects.all()
    n = 0
    for contact in contacts:
        if contact.MobileNumber is None:
            contact.MobileNumber = ''
        if contact.OtherNumber is None:
            contact.OtherNumber = ''
        n += 1
        xml_data += f'        <Contact Id="{n}" Line="0" DisplayName="{contact.DisplayName}" OfficeNumber="{contact.OfficeNumber}" MobileNumber="{contact.MobileNumber}" OtherNumber="{contact.OtherNumber}" Ring="Auto" Photo="" />\n'

    xml_data += '    </Group>\n'
    xml_data += '</ContactData>\n'

    # Отправка файла для скачивания
    response = HttpResponse(xml_data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="contacts.xml"'
    return response


def view_xml(request):
    # Генерация XML-файла
    xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_data += '<ContactData>\n'
    xml_data += '    <Group Id="1" Name="Default" Ring="Auto" Description="">\n'

    contacts = Contact.objects.all()
    n = 0
    for contact in contacts:
        if contact.MobileNumber is None:
            contact.MobileNumber = ''
        if contact.OtherNumber is None:
            contact.OtherNumber = ''
        n += 1
        xml_data += f'        <Contact Id="{n}" Line="0" DisplayName="{contact.DisplayName}" OfficeNumber="{contact.OfficeNumber}" MobileNumber="{contact.MobileNumber}" OtherNumber="{contact.OtherNumber}" Ring="Auto" Photo="" />\n'

    xml_data += '    </Group>\n'
    xml_data += '</ContactData>\n'

    # Отображение XML-файла в браузере
    response = HttpResponse(xml_data, content_type='text/txt; charset=utf-8')
    return response
