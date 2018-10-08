from django.db import models

# Create your models here.

class Professor(models.Model):
    def __str__(self):
        return 'Nome: ' + self.nome + ' E-mail: ' + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        if self.login == '':
          raise Exception('Professor sem login')
        if self.email == '':
            self.email = 'email nao fornecido'
        professores_login = Professor.objects.filter(login = self.login)
        if len(professores_login) > 0:
            raise Exception('login repetido')
        super(Professor, self).save()


class Disciplina(models.Model):
    def __str__(self):
        return 'Nome: ' + self.nome + ' Ementa: ' + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

    def save(self):
        disciplina_dobrada = Disciplina.objects.filter(nome = self.nome)
        if len(disciplina_dobrada) > 0:
            raise Exception('disciplina repetido')
        super(Disciplina, self).save()


class DisciplinaOfertada(models.Model):

    def __str__(self):
        return 'Curso: ' + self.curso + ' Turma: ' + self.turma +  ' ano: ' + self.ano +  ' Semestre: ' + self.semestre + ' professor: ' + self.professor +  ' disciplina: ' + self.disciplina
        
    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida

    def save(self):
        cursovalido = ['ADS', 'SI', 'BD']
        if self.curso not in cursovalido:
            disciplina_invalida = Disciplina.objects.filter(curso = self.curso)
            if len(disciplina_invalida) > 0:
                raise Exception('disciplina invalida')

            turma_dobrado = DisciplinaOfertada.objects.filter(turma = self.turma)
            if len(turma_dobrado)>0:
                ano_dobrado = DisciplinaOfertada.objects.filter(curso = self.ano)
                if len(ano_dobrado)>0:
                    semestre_dobrado = DisciplinaOfertada.objects.filter(semestre = self.semestre)
                    if len(semestre_dobrado)>0:
                        professor_dobrado = DisciplinaOfertada.objects.filter(professor = self.professor)
                        if len(professor_dobrado)>0:
                            disciplina_dobrado = DisciplinaOfertada.objects.filter(curso = self.disciplina)
                            if len(disciplina_dobrado)>0:
                                 raise Exception('disciplina dobrada')    

        super(DisciplinaOfertada, self).save()
