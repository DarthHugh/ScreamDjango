from django.db import models
from basico.choices import StatusKanBan


# List of estimations to a ProductBacklog Item
'''
class EstimationsPBitems(models.Model):
    numer = models.IntegerField(default=100)
    def __str__(self):
        result = ("%s" % (self.numer))
        return result
'''

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=200, verbose_name='Descrição')

    def __str__(self):
        return self.name

# Items for a Product
# Has a collection of Estimations
class ProductBacklogItem(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    estimations = models.PositiveIntegerField(default=100)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StatusKanBan.choices, validators=[StatusKanBan.validator], default=StatusKanBan.toDo) #where it is on the Kanban Chart FAZER UM ENUM
    def __str__(self):
        return self.title

class AceptanceRequirement(models.Model):
    description = models.CharField(max_length=50, verbose_name='Descrição')
    realized = models.BooleanField(verbose_name='Realizado', default=False)
    pbItem = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE)

# Has a collection of ProductBacklogItems
class Sprint(models.Model):
    description = models.CharField(max_length=200, verbose_name='Descrição')
    pbItem = models.ManyToManyField(ProductBacklogItem, verbose_name='Product Backlog', null=True)
    status = models.CharField(max_length=20, choices=StatusKanBan.choices, validators=[StatusKanBan.validator],
                              default=StatusKanBan.toDo)  # where it is on the Kanban Chart / Choice is like a ENUM
    initialDate = models.DateField(verbose_name='Data inicial')

class Activity(models.Model):
    description = models.CharField(max_length=200, verbose_name='Descrição')
    status = models.CharField(max_length=20, choices=StatusKanBan.choices, validators=[StatusKanBan.validator],
                              default=StatusKanBan.toDo)
    pbItem = models.ForeignKey(ProductBacklogItem)
    sprint = models.ForeignKey(Sprint)




