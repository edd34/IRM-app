from django.core.management.base import BaseCommand
from django.core.management import call_command
from components.alert_table.models import AlertTable
from components.localisation.models import Localisation
from components.traffic_alert.models import TrafficAlert


class Command(BaseCommand):
    help = "export database"

    def handle(self, *args, **kwargs):
        inst_at = AlertTable.objects.get_or_create(
            category="Information", alert_type="Manifestation", alert_subtype="Mariage"
        )
        AlertTable.objects.get_or_create(category="Information", alert_type="Manifestation", alert_subtype="Manzaraka")
        AlertTable.objects.get_or_create(category="Information", alert_type="Manifestation", alert_subtype="Marche")
        AlertTable.objects.get_or_create(category="Information", alert_type="Manifestation", alert_subtype="Grève")
        AlertTable.objects.get_or_create(
            category="Information", alert_type="Signalisation", alert_subtype="Feux temporaire"
        )
        AlertTable.objects.get_or_create(category="Information", alert_type="Signalisation", alert_subtype="Dos d'âne")
        AlertTable.objects.get_or_create(category="Information", alert_type="Chaussée", alert_subtype="Nid de poule")
        AlertTable.objects.get_or_create(
            category="Information", alert_type="Chaussée", alert_subtype="Arbre sur la chaussée"
        )
        AlertTable.objects.get_or_create(category="Information", alert_type="Chaussée", alert_subtype="Gravillon")
        AlertTable.objects.get_or_create(category="Information", alert_type="Chaussée", alert_subtype="Route barrée")
        AlertTable.objects.get_or_create(category="Danger", alert_type="Agression", alert_subtype="Caillassage")
        AlertTable.objects.get_or_create(category="Danger", alert_type="Accident", alert_subtype="Accident")
        AlertTable.objects.get_or_create(
            category="Danger", alert_type="Travaux", alert_subtype="Travaux sur la chaussée"
        )

        inst_loc = Localisation.objects.get_or_create(city="Kawéni", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Mtsapéré", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Kavani", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Passamainty", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Mamoudzou", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Vahibé", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Tsoundzou 1", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Tsoundzou 2", municipality="Mamoudzou", postalcode="")
        Localisation.objects.get_or_create(city="Majicavi-Koropa", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Koungou", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Longoni", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Trévani", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Majicavo Lamir", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Kangani", municipality="Koungou", postalcode="")
        Localisation.objects.get_or_create(city="Dzaoudzi", municipality="Labattoir", postalcode="")
        Localisation.objects.get_or_create(city="Labattoir", municipality="Labattoir", postalcode="")
        Localisation.objects.get_or_create(city="Tsararano", municipality="Dembéni", postalcode="")
        Localisation.objects.get_or_create(city="Dembéni", municipality="Dembéni", postalcode="")
        Localisation.objects.get_or_create(city="Iloni", municipality="Dembéni", postalcode="")
        Localisation.objects.get_or_create(city="Hajangoua", municipality="Dembéni", postalcode="")
        Localisation.objects.get_or_create(city="Ongojou", municipality="Dembéni", postalcode="")
        Localisation.objects.get_or_create(city="Combani", municipality="Tsingoni", postalcode="")
        Localisation.objects.get_or_create(city="Tsingoni", municipality="Tsingoni", postalcode="")
        Localisation.objects.get_or_create(city="Miréréni", municipality="Tsingoni", postalcode="")
        Localisation.objects.get_or_create(city="Mroalé", municipality="Tsingoni", postalcode="")
        Localisation.objects.get_or_create(city="Pamandzi", municipality="Pamandzi", postalcode="")
        Localisation.objects.get_or_create(city="Dzoumogné", municipality="Bandraboua", postalcode="")
        Localisation.objects.get_or_create(city="Bandraboua", municipality="Bandraboua", postalcode="")
        Localisation.objects.get_or_create(city="Handrema", municipality="Bandraboua", postalcode="")
        Localisation.objects.get_or_create(city="Bouyouni", municipality="Bandraboua", postalcode="")
        Localisation.objects.get_or_create(city="Mtsangamboua", municipality="Bandraboua", postalcode="")

        Localisation.objects.get_or_create(city="Sada", municipality="Sada", postalcode="")
        Localisation.objects.get_or_create(city="Mangajou", municipality="Sada", postalcode="")

        Localisation.objects.get_or_create(city="Mtsamboro", municipality="Mtsamboro", postalcode="")
        Localisation.objects.get_or_create(city="Mtsahara", municipality="Mtsamboro", postalcode="")
        Localisation.objects.get_or_create(city="Hamjago", municipality="Mtsamboro", postalcode="")

        Localisation.objects.get_or_create(city="Bandrélé", municipality="Bandrélé", postalcode="")
        Localisation.objects.get_or_create(city="Mtsamoudou", municipality="Bandrélé", postalcode="")
        Localisation.objects.get_or_create(city="Nyambadao", municipality="Bandrélé", postalcode="")
        Localisation.objects.get_or_create(city="Dapani", municipality="Bandrélé", postalcode="")
        Localisation.objects.get_or_create(city="Hamouro", municipality="Bandrélé", postalcode="")
        Localisation.objects.get_or_create(city="Bambo-Est", municipality="Bandrélé", postalcode="")

        Localisation.objects.get_or_create(city="Poroani", municipality="Chirongui", postalcode="")
        Localisation.objects.get_or_create(city="Tsimkoura", municipality="Chirongui", postalcode="")
        Localisation.objects.get_or_create(city="Chirongui", municipality="Chirongui", postalcode="")
        Localisation.objects.get_or_create(city="Miréréni", municipality="Chirongui", postalcode="")
        Localisation.objects.get_or_create(city="Mramadoudou", municipality="Chirongui", postalcode="")
        Localisation.objects.get_or_create(city="Malamani", municipality="Chirongui", postalcode="")

        Localisation.objects.get_or_create(city="Ouangani", municipality="Ouangani", postalcode="")
        Localisation.objects.get_or_create(city="Barakani", municipality="Ouangani", postalcode="")
        Localisation.objects.get_or_create(city="Kahani", municipality="Ouangani", postalcode="")
        Localisation.objects.get_or_create(city="Coconi", municipality="Ouangani", postalcode="")

        Localisation.objects.get_or_create(city="Bouéni", municipality="Bouéni", postalcode="")
        Localisation.objects.get_or_create(city="Mzouazia", municipality="Bouéni", postalcode="")
        Localisation.objects.get_or_create(city="Moinatrindri", municipality="Bouéni", postalcode="")
        Localisation.objects.get_or_create(city="Hagnoundrou", municipality="Bouéni", postalcode="")
        Localisation.objects.get_or_create(city="Bambo-Ouest", municipality="Bouéni", postalcode="")
        Localisation.objects.get_or_create(city="Mbouanatsa", municipality="Bouéni", postalcode="")

        Localisation.objects.get_or_create(city="M'tsangamouji", municipality="M'tsangamouji", postalcode="")
        Localisation.objects.get_or_create(city="Chembényoumba", municipality="M'tsangamouji", postalcode="")
        Localisation.objects.get_or_create(city="Mliha", municipality="M'tsangamouji", postalcode="")

        Localisation.objects.get_or_create(city="Acoua", municipality="Acoua", postalcode="")
        Localisation.objects.get_or_create(city="Mtsangadoua", municipality="Acoua", postalcode="")

        Localisation.objects.get_or_create(city="Kani-Kéli", municipality="Kani-Kéli", postalcode="")
        Localisation.objects.get_or_create(city="Choungui", municipality="Kani-Kéli", postalcode="")
        Localisation.objects.get_or_create(city="Kanibé", municipality="Kani-Kéli", postalcode="")
        Localisation.objects.get_or_create(city="Mbouini", municipality="Kani-Kéli", postalcode="")
        Localisation.objects.get_or_create(city="Mronabéja", municipality="Kani-Kéli", postalcode="")
        Localisation.objects.get_or_create(city="Passy-Kéli", municipality="Kani-Kéli", postalcode="")

        TrafficAlert.objects.get_or_create(
            lat=-12.84872320,
            lon=45.11295290,
            alert_id=inst_at[0],
            localisation_id=inst_loc[0],
            localisation_description="test localisation description",
            report_description="test report description",
        )
