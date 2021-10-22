from django.db import models


class Estado(models.Model):

    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.sigla


class Cartorios(models.Model):
    cnpj = models.CharField(max_length=50, null=True, blank=True)
    cns = models.CharField(max_length=50, null=True, blank=True)
    data_instalacao = models.DateField(null=True, blank=True)
    nome_oficial = models.CharField(max_length=700, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=700, null=True, blank=True)
    nome_titular = models.CharField(max_length=400, null=True, blank=True)
    nome_substituto = models.CharField(max_length=400, null=True, blank=True)
    nome_juiz = models.CharField(max_length=400, null=True, blank=True)
    ultima_atualizacao = models.DateField(null=True, blank=True)
    horario_funcionamento = models.CharField(max_length=300, null=True, blank=True)
    area_abrangencia = models.CharField(max_length=700, null=True, blank=True)
    atribuicoes = models.CharField(max_length=700, null=True, blank=True)
    comarca = models.CharField(max_length=255, null=True, blank=True)
    entrancia = models.CharField(max_length=50, null=True, blank=True)
    observacao = models.CharField(max_length=700, null=True, blank=True)

    email = models.EmailField(max_length=254, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    home_page = models.CharField(max_length=100, null=True, blank=True)
    fax= models.CharField(max_length=100, null=True, blank=True)

    endereco = models.CharField(max_length=700, null=True, blank=True)
    bairro = models.CharField(max_length=300, null=True, blank=True)
    municipio = models.CharField(max_length=300, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    uf = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_oficial

    class Meta:
        verbose_name_plural = 'Cartorios'
