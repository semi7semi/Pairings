from django.db import models


ARMIES_CHOICE = (
    ("BH", "Beast Herds"),
    ("DL", "Demonic Legion"),
    ("DE", "Dread Elves"),
    ("DH", "Dvarwen Holds"),
    ("EoS", "Empire of Sonnstahl"),
    ("HE", "Highborn Elves"),
    ("ID", "Infernal Dwarves"),
    ("KoE", "Kingdom of Equitaine"),
    ("OK", "Ogre Khans"),
    ("OG", "Orcs and Goblins"),
    ("SA", "Saurian Ancients"),
    ("SE", "Sylvan Elves"),
    ("UD", "Undying Dynasties"),
    ("VC", "Vampire Covenant"),
    ("VS", "Vermin Swarm"),
    ("WDG", "Warriors of the Dark Gods")
)


class Tournaments5v5(models.Model):
    name = models.CharField(max_length=64)
    player1 = models.CharField(max_length=64)
    player2 = models.CharField(max_length=64)
    player3 = models.CharField(max_length=64)
    player4 = models.CharField(max_length=64)
    player5 = models.CharField(max_length=64)
    p1 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    p2 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    p3 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    p4 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    p5 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    date = models.DateField()

    date.editable = True
