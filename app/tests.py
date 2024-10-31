# baykarbackend/app/tests.py

from django.test import TestCase
from .models import Team, Personnel, Part, Aircraft

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Kanat Takımı")

    def test_team_creation(self):
        """Takımın düzgün oluşturulduğunu test eder"""
        self.assertEqual(self.team.name, "Kanat Takımı")
        self.assertEqual(Team.objects.count(), 1)


class PersonnelModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Gövde Takımı")
        self.personnel = Personnel.objects.create(name="Ahmet", team=self.team)

    def test_personnel_creation(self):
        """Personelin doğru şekilde oluşturulduğunu test eder"""
        self.assertEqual(self.personnel.name, "Ahmet")
        self.assertEqual(self.personnel.team.name, "Gövde Takımı")
        self.assertEqual(Personnel.objects.count(), 1)


class PartModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Kuyruk Takımı")
        self.part = Part.objects.create(type="tail", aircraft_type="tb2", team=self.team)

    def test_part_creation(self):
        """Parçanın doğru şekilde oluşturulduğunu test eder"""
        self.assertEqual(self.part.type, "tail")
        self.assertEqual(self.part.aircraft_type, "tb2")
        self.assertEqual(self.part.team.name, "Kuyruk Takımı")
        self.assertEqual(Part.objects.count(), 1)


class AircraftModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Aviyonik Takımı")
        self.part = Part.objects.create(type="avionics", aircraft_type="akinci", team=self.team)
        self.aircraft = Aircraft.objects.create(type="akinci")
        self.aircraft.parts.add(self.part)

    def test_aircraft_creation(self):
        """Uçağın doğru şekilde oluşturulduğunu ve parça eklenebildiğini test eder"""
        self.assertEqual(self.aircraft.type, "akinci")
        self.assertTrue(self.part in self.aircraft.parts.all())
        self.assertEqual(Aircraft.objects.count(), 1)


class AircraftAssemblyTest(TestCase):
    def setUp(self):
        # Gerekli takımlar ve parçalar oluşturuluyor
        self.wing_team = Team.objects.create(name="Kanat Takımı")
        self.body_team = Team.objects.create(name="Gövde Takımı")
        self.tail_team = Team.objects.create(name="Kuyruk Takımı")
        self.avionics_team = Team.objects.create(name="Aviyonik Takımı")

        # Her takım için ilgili parçalar oluşturuluyor
        self.wing_part = Part.objects.create(type="wing", aircraft_type="tb3", team=self.wing_team)
        self.body_part = Part.objects.create(type="body", aircraft_type="tb3", team=self.body_team)
        self.tail_part = Part.objects.create(type="tail", aircraft_type="tb3", team=self.tail_team)
        self.avionics_part = Part.objects.create(type="avionics", aircraft_type="tb3", team=self.avionics_team)

        # Uçak oluşturuluyor
        self.aircraft = Aircraft.objects.create(type="tb3")

    def test_assembly(self):
        """Uçağın tüm parçalar eklenerek monte edilebildiğini test eder"""
        self.aircraft.parts.add(self.wing_part, self.body_part, self.tail_part, self.avionics_part)
        self.assertEqual(self.aircraft.parts.count(), 4)
        self.assertFalse(self.aircraft.assembled)

        # Parçalar eklendikten sonra uçağı monte ediyoruz
        if self.aircraft.parts.count() == 4:
            self.aircraft.assembled = True
            self.aircraft.save()

        self.assertTrue(self.aircraft.assembled)
