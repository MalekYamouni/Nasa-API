import requests
import json

limit = 10 # Datensätze
days = 500 # Zeitraum

#Api auf NASA Homepage
url = f"https://eonet.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}&source=InciWeb&status=open"
# Die Daten mit dem Modul requests gegettet
r = requests.get(url)
# Die Daten in ein json-Format gepackt
events_data = r.json()

# with open öffnet und schließt die Datenbank automatisch
# json.dumps läd alles ab und danach steht was abgeladen werden soll "events_data"
with open("events.json","w") as f:
    f.write(json.dumps(events_data, indent=10))

# jetzt wird eine neue Variable erstellt und ihr werden dann von events_data die "events" gegeben
event_list = events_data["events"]

# jetzt wird von jedem Element in event_list der Datensatz mit dem Begriff "title" ausgegeben
for event in event_list:
    print(event["title"])