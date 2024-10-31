# myproject/app/models.py

from django.db import models

# Takımlar (Teams)
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Personel (Personnel)
class Personnel(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, related_name="personnel", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.team.name}"

# Parçalar (Parts)
class Part(models.Model):
    PART_TYPES = [
        ('wing', 'Kanat'),
        ('body', 'Gövde'),
        ('tail', 'Kuyruk'),
        ('avionics', 'Aviyonik')
    ]
    AIRCRAFT_TYPES = [
        ('tb2', 'TB2'),
        ('tb3', 'TB3'),
        ('akinci', 'AKINCI'),
        ('kizilelma', 'KIZILELMA')
    ]

    type = models.CharField(max_length=20, choices=PART_TYPES)
    aircraft_type = models.CharField(max_length=20, choices=AIRCRAFT_TYPES)
    team = models.ForeignKey(Team, related_name="parts", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='available')

    def __str__(self):
        return f"{self.get_type_display()} for {self.get_aircraft_type_display()}"

# Uçaklar (Aircraft)
class Aircraft(models.Model):
    type = models.CharField(max_length=20, choices=Part.AIRCRAFT_TYPES)
    parts = models.ManyToManyField(Part, related_name="aircrafts")
    assembled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_type_display()} - Assembled: {self.assembled}"
