import json
from datetime import datetime

print("BMW Inventory Monitor")

sample_vehicle = {
    "vin": "WB523CF06SCS95806",
    "price": 58270,
    "mileage": 15483,
    "dealer": "BMW of Bloomfield Hills",
    "timestamp": str(datetime.now())
}

with open("inventory.json", "w") as f:
    json.dump([sample_vehicle], f, indent=2)

print("File written.")
