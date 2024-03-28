import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','CBVProject3.settings')

import django
django.setup()

from testapp.models import CompanyModel

from random import *

from faker import Faker

faker=Faker()

def phonenum():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fcompany=faker.random_element(elements=('wipro','accenture','tcs','capgemini','deloitte','TECH-MAHINDRA','TEITO-EVERY','COGINIZIENT'))
        feid=randint(1001,9999)
        fename=faker.name()
        fesal=randint(25000,100000)
        fephn=phonenum()
        femail=faker.email()
        emp_record=CompanyModel.objects.get_or_create(
            company=fcompany,
            eid=feid,
            ename=fename,
            esal=fesal,
            ephn=fephn,
            eemail=femail
        )

n = int(input('Enter number of employees:'))
populate(n)
print(f'{n} Records inserted successfully..........')

