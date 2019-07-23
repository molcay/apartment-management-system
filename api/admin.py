from django.contrib import admin

from api.models import Person, Tenant, Guarantor, Landlord, Room, Agreement, AgreementFile

admin.site.register([
    Person,
    Tenant,
    Guarantor,
    Landlord,
    Room,
    Agreement,
    AgreementFile,
])
