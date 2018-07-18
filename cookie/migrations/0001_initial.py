from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_title', models.CharField(default='ROC Rivor maakt gebruik van cookies', help_text='Bijvoorbeeld: ROC Rivor maakt gebruik van cookies', max_length=255, verbose_name='Titel')),
                ('modal_text', wagtail.core.fields.RichTextField(default='\n            ROC Rivor gebruikt cookies en verzamelt daarmee informatie over jouw gebruik op de website. Dit doen we\n            onder andere om de website te verbeteren, voor social media en om jou relevante informatie en advertenties\n            te laten zien. De cookies zijn bedoeld om je via deze site zo goed mogelijk te bedienen. Door de cookies\n            te accepteren, geef je aan akkoord te zijn met het gebruik van cookies die worden gebruikt door ons en\n            derden. Als je hiermee niet akkoord bent, klik dan op "Weiger cookies".\n            ', verbose_name='Tekst')),
                ('page_title', models.CharField(default='Wij maken gebruik van cookies', help_text='Bijvoorbeeld: Wij maken gebruik van cookies', max_length=255, verbose_name='Titel')),
                ('page_introduction', models.TextField(default='\n            In Nederland is sinds 5 juni 2012 de zogenaamde cookiewet van kracht. De nieuwe cookiewet verplicht\n            websites om bezoekers in detail te informeren over de cookies die tijdens het websitebezoek worden\n            geplaatst en gebruikt.\n            ', verbose_name='Tekst')),
                ('page_text', wagtail.core.fields.RichTextField(default='\n            De website van ROC Rivor maakt gebruik van cookies. Cookies zijn kleine bestanden die je voorkeuren\n            tijdens het surfen onthouden en opslaan op je eigen computer. Een cookie slaat geen persoonsgegevens\n            op en onthoudt alleen je voorkeuren en je interesses op basis van je surfgedrag. Om de website van\n            ROC Rivor te kunnen bekijken, dien je het gebruik van cookies te accepteren of te weigeren.\n            ', verbose_name='Tekst')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Cookie Wall',
            },
        ),
    ]
