from datetime import datetime, date, timedelta

import pandas as pd
from django.core.management.base import BaseCommand
from pandas._libs import json

from api.models import Cartorios, Estado


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        estados = Estado.objects.all()

        data = pd.read_csv('Cartorios_utf8.csv', delimiter=';',
                         header=0, index_col=False)

        dadosDIC = json.loads(data.to_json(orient='records'))

        for item in estados:

            for k in dadosDIC:

                cep = str(k['CEP']).replace('.0', "")

                c = Cartorios()
                c.nome_titular =  k['Nome do Titular']
                c.cnpj = k['CNPJ']
                c.cns =  k['CNS']
                c.nome_fantasia = k['Nome Fantasia']
                c.nome_oficial =  k['Nome Oficial']
                try:
                    c.data_instalacao = datetime.strptime(k['Data de Instalação'], '%d/%m/%Y').date()
                except:
                    pass

                try:
                    c.ultima_atualizacao = datetime.strptime(k['Última Atualização'], '%d/%m/%Y').date()
                except:
                    pass

                c.endereco = str(k['Endereço'])
                c.cep = cep
                c.bairro = str(k['Bairro'])
                c.municipio = str(k['Município'])
                c.uf = Estado.objects.get(id=item.id)

                c.nome_juiz = k['Nome do Juiz']
                c.nome_substituto = k['Nome do Substituto']
                c.home_page = k['Homepage']
                c.email = k['Email']
                c.telefone = k['Telefone']
                c.fax = k['Fax']
                c.observacao = k['Observação']
                c.horario_funcionamento = k['Horário de Funcionamento']
                c.area_abrangencia = k['Área de Abrangência']
                c.atribuicoes = k['Atribuições']
                c.comarca = k['Comarca']
                c.entrancia = k['Entrância']

                c.save()

        print('\n Cartórios carregados com sucesso!')