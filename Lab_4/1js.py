import json
with open("/Users/user/Desktop/PP2/Lab_4/sample-data.json", "r") as f:
    data = json.load(f)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    descr = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    print(f"{dn:50} {descr:3} {speed:7} {mtu}")