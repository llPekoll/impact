import csv
from datetime import datetime

csv_output = "events.csv"


def refactor_input(mock_for_test):
    hours = {}
    for mock in mock_for_test:
        date_from_timestamp = datetime.fromtimestamp(mock.get("timestamp"))
        data_from_event = [
            {"event": mock.get("event"), "timestamp": str(date_from_timestamp)}
        ]
        if hours.get(date_from_timestamp.hour):
            app = list(hours.get(date_from_timestamp.hour))
            app.append(data_from_event[0])
            hours[date_from_timestamp.hour] = app
        else:
            hours[date_from_timestamp.hour] = data_from_event
    return hours


def div_by_10(event_list):
    for key, value in event_list.items():
        for items in value:
            items["constance_mult"] = items["event"] + " multiply by 0.1"
    return {"success": True}


def csv_export(event_list):
    with open(csv_output, "w") as f:
        w = csv.DictWriter(f, event_list.keys())
        w.writeheader()
        for key, value in event_list.items():
            for v in event_list[key]:
                w.writerow({key: v})
    return csv_output


def get_ids(entry):
    return {keys.get("id") for keys in entry}
