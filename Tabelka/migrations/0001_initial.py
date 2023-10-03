# Generated by Django 4.2.5 on 2023-10-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament5v5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('player1', models.CharField(max_length=64)),
                ('player2', models.CharField(max_length=64)),
                ('player3', models.CharField(max_length=64)),
                ('player4', models.CharField(max_length=64)),
                ('player5', models.CharField(max_length=64)),
                ('p1', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdome of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('p2', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdome of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('p3', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdome of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('p4', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdome of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('p5', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdome of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('date', models.DateField()),
            ],
        ),
    ]
