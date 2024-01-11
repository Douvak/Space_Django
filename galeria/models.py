from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    opcoes_de_categoria = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False,blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_de_categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    publicado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos/%Y/%M/%d/', blank=True,)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    

    def __str__(self):
        return self.nome