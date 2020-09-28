from django.db import models

# Create your models here.
class Question(models.Model): #L'objet Question (d'un sondage) contient une question et une date de publication
    question_text = models.CharField(max_length=200) #CharField -> champs de caractères
    pub_date = models.DateTimeField('date published') #DateTimeField -> champs date et heure


class Choice(models.Model): #L'objet Choice contient un texte représentant le choix et le décompte des votes
                            #Chaque choix est associé à une Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #1. Créer ou modifier les modèles ici
    #2. Commande 'py manage.py makemigrations' pour créer des migrations associées aux modèles
    #3. Commande 'py manage.py migrate' pour appliquer les créations/modifications à la base de données