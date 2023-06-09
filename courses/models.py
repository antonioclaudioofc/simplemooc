from django.db import models
from django.urls import reverse
from django.conf import settings


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

# Create your models here.


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data De Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em ', auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('courses:details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-name']


class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário', related_name='enrollments',
        on_delete = models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name='Curso', related_name='enrollments',
        on_delete = models.CASCADE
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em',  auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'))