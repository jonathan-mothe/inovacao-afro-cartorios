import pandas as pd
from django.core.management.base import BaseCommand

from api.models import Estado


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        if Estado.objects.exists():
            print("Objeto já existe.")
        else:
            data = pd.read_csv('Cartorios_utf8.csv',
                             delimiter=';', header=0, index_col=False)

            dadosDIC = data.to_dict('records')

            for item in dadosDIC:
                try:
                    Estado.objects.get(sigla=item['UF'])
                    print('UF já existe')
                except:
                    obj = Estado()
                    obj.sigla = item['UF']
                    obj.save()
                    print('UF salva')

        print('\n Estados carregados com sucesso!')