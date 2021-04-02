import uuid
import random
from datetime import datetime, timedelta

mock_for_test = []

mock_data = [
    {"id": "xxxx-xxxx-xxxx-xxxx", "event": "impressions", "timestamp": 00000000000}
]

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
