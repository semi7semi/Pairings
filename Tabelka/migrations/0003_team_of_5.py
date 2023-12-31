# Generated by Django 4.2.5 on 2023-10-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tabelka', '0002_tournaments5v5_delete_tournament5v5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_of_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('op1', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdom of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('op2', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdom of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('op3', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdom of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('op4', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdom of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('op5', models.CharField(choices=[('BH', 'Beast Herds'), ('DL', 'Demonic Legion'), ('DE', 'Dread Elves'), ('DH', 'Dvarwen Holds'), ('EoS', 'Empire of Sonnstahl'), ('HE', 'Highborn Elves'), ('ID', 'Infernal Dwarves'), ('KoE', 'Kingdom of Equitaine'), ('OK', 'Ogre Khans'), ('OG', 'Orcs and Goblins'), ('SA', 'Saurian Ancients'), ('SE', 'Sylvan Elves'), ('UD', 'Undying Dynasties'), ('VC', 'Vampire Covenant'), ('VS', 'Vermin Swarm'), ('WDG', 'Warriors of the Dark Gods')], max_length=16)),
                ('p11', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p12', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p13', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p14', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p15', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p21', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p22', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p23', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p24', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p25', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p31', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p32', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p33', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p34', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p35', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p41', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p42', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p43', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p44', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p45', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p51', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p52', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p53', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p54', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('p55', models.IntegerField(choices=[(-3, '-3'), (-2, '-2'), (-1, '-1'), (0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tourney5', to='Tabelka.tournaments5v5')),
            ],
        ),
    ]
