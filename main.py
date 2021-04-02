import random
from datetime import datetime, timedelta
import uuid


mock_data = [
    {"id": "xxxx-xxxx-xxxx-xxxx", "event": "impressions", "timestamp": 00000000000}
]

mock_for_test = []
event_type = [
    "impressions",
    "video_start",
    "video_25",
    "video_50",
    "video_75",
    "video_completed",
]
random_hours = [3, 4, 5, 6, 8]

for x in range(6):
    # random hours + GMT+1
    timestamp = (
        datetime.now()
        + timedelta(hours=1)
        + timedelta(hours=random.choice(random_hours))
    )
    dict_mock = {
        "id": str(uuid.uuid4())[4:23],
        "event": random.choice(event_type),
        "timestamp": int(timestamp.timestamp()),
    }
    mock_for_test.append(dict_mock)
print(mock_for_test)


def refactor_input():
    hours = {}
    for mock in mock_for_test:
        date_from_timestamp = datetime.fromtimestamp(mock.get("timestamp"))
        data_from_event = [
            {"event": mock.get("event"), "timestamp": str(date_from_timestamp)}
        ]
        if hours.get(date_from_timestamp.hour):
            app = list(hours.get(date_from_timestamp.hour))
            app.append(data_from_event[0])
            hours[f"{date_from_timestamp.hour}h"] = app
        else:
            hours[f"{date_from_timestamp.hour}h"] = data_from_event
    return hours


h = refactor_input()
print("hours")
print(h)
