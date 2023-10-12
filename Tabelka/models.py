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

PARING_SCORE_CHOICES = (
    (-3, "-3"),
    (-2, "-2"),
    (-1, "-1"),
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3")
)

class Armys(models.Model):
    army = models.CharField(max_length=16, choices=ARMIES_CHOICE)

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


class Team_of_5(models.Model):
    name = models.CharField(max_length=64)
    op1 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    op2 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    op3 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    op4 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    op5 = models.CharField(max_length=16, choices=ARMIES_CHOICE)
    p11 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p12 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p13 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p14 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p15 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p21 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p22 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p23 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p24 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p25 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p31 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p32 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p33 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p34 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p35 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p41 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p42 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p43 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p44 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p45 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p51 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p52 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p53 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p54 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    p55 = models.IntegerField(choices=PARING_SCORE_CHOICES)
    tournament = models.ForeignKey(Tournaments5v5, on_delete=models.CASCADE, related_name='tourney5')
