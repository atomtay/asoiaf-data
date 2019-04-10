from django.db import models

# Create your models here.

GENDERS = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Unknown', 'UNKNOWN')
)

DEATHS = (
    ('Age', 'AGE'),
    ('Animal', 'ANIMAL'),
    ('Arrow/bolt', 'ARROW/BOLT'),
    ('Asphyxiation', 'ASPHYXIATION'),
    ('Beheading', 'BEHEADING'),
    ('Childbirth', 'CHILDBIRTH'),
    ('Crushing', 'CRUSHING'),
    ('Dark magic', 'DARKMAGIC'),
    ('Drowning', 'DROWNING'),
    ('Falling', 'FALLING'),
    ('Fire', 'FIRE'),
    ('Hanging', 'HANGING'),
    ('Head trauma', 'HEADTRAUMA'),
    ('Illness', 'ILLNESS'),
    ('Impalement', 'IMPALEMENT'),
    ('Poisoning', 'POISONING'),
    ('Slain (axe)', 'SLAINAXE'),
    ('Slain (mace)', 'SLAINMACE'),
    ('Slain (sword)', 'SLAINSWORD'),
    ('Slain (scythe)', 'SLAINSCYTHE'),
    ('Stabbing', 'STABBING'),
    ('Starvation', 'STARVATION'),
    ('Throat cut', 'THROATCUT'),
    ('Unknown', 'UNKNOWN'),
    ('White Walkers/Wights/Others', 'WHITEWALKERSWIGHTSOTHERS'),
    ('Wound infection', 'WOUNDINFECTION')
)


class Book(models.Model):
    title = models.CharField(max_length=100, default='', primary_key=True)
    num_of_chapters = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100, default='', primary_key=True)
    gender = models.CharField(
        max_length=7, choices=GENDERS, default='Unknown')

    def __unicode__(self):
        return self.name


class Nobility(models.Model):
    name = models.OneToOneField(
        Character, on_delete=models.CASCADE, primary_key=True)
    house = models.CharField(max_length=100, default='Unknown')

    def __unicode__(self):
        return self.name


class Death(models.Model):
    name = models.OneToOneField(
        Character, on_delete=models.CASCADE, primary_key=True)
    manner_of_death = models.CharField(
        max_length=100, default='Unknown', choices=DEATHS)

    def __unicode__(self):
        return self.name


class Book_of_Death(models.Model):
    name = models.OneToOneField(
        Character, on_delete=models.CASCADE, primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Chapter_of_Death(models.Model):
    name = models.OneToOneField(
        Character, on_delete=models.CASCADE, primary_key=True)
    chapter_number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
