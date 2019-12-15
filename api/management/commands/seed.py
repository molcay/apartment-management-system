import json

from django.core.management.base import BaseCommand

from api.models import Landlord, Room, Tenant, ApartInfo


class Command(BaseCommand):
    help = 'Seed initial data to db'
    data_path = 'seed_data/data.json'

    def handle(self, *args, **options):
        self.stdout.write('Database seeding...')
        self._seed()
        self.stdout.write('Database populated.')

    def _seed(self):
        data = self._read_data_file()
        if len(Landlord.objects.all()) == 0 and len(Room.objects.all()) == 0:
            landlords = {}
            for landlord in data['landlords']:
                instance = Landlord(**landlord)
                instance.save()
                landlords[landlord['title']] = instance
                print(instance)

            for room in data['rooms']:
                room['landlord'] = landlords[room['landlord']]
                room['size'] = float(room['size'].replace(',', '.'))
                instance = Room(**room)
                instance.save()
                print(instance)

        if len(Tenant.objects.all()) == 0:
            for tenant in data['tenants']:
                instance = Tenant(**tenant)
                instance.save()
                print(instance)

        if len(ApartInfo.objects.all()) == 0:
            apart = data['apart']
            instance = ApartInfo(**apart)
            instance.save()
            print(apart)

    def _read_data_file(self):
        with open(self.data_path, 'r') as file:
            data = json.loads(file.read())

        return data
