from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cnpj_cpf = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message='Telefone deve conter apenas números, com 10 ou 11 dígitos (DDD + número).'
            )
        ]
    )
    endereco = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('analise', 'Em Análise'),
        ('concluido', 'Concluído'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='projetos')
    titulo = models.CharField(max_length=200)
    tipo_servico = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    data_inicio = models.DateField()
    prazo_vencimento = models.DateField()
    responsavel = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Documento(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='documentos')
    nome_arquivo = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    data_upload = models.DateTimeField(auto_now_add=True)
    data_validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_arquivo


class Vencimento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('cumprido', 'Cumprido'),
        ('atrasado', 'Atrasado'),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='vencimentos')
    tipo = models.CharField(max_length=100)
    data_limite = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.projeto.titulo}"
