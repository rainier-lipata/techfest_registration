print("Welcome to TechFest Registration System!")
print("Event organized by Rainier Lipata of APPDAET BTCS1")
''' event_organizer = input("How many participants will register?: ") '''

# Part 2 Task 1
participants_count = []

participants_count = int(input("How many participants will register?: "))

if participants_count <= 0:
    print("Invalid number of participants.")
    exit()
else:
    print("Registered participants!")

# Part 2 Task 2
participants = []
for i in range(participants_count):
    name = input(f"Enter participant name #{i + 1}: ")
    track = input(f"Enter chosen track for {name}: ")

    record = {
        "name": name,
        "track": track
    }
    participants.append(record)

print("\nRegistered Participants:")
for i, participants in enumerate(participants, start=1):
    print(f"{i}. {participants['name']} - {participants['track']}")


participants = [
    {"name": "Ana", "track": "Cybersecurity"},
    {"name": "Mark", "track": "Data"},
    {"name": "Ana", "track": "Cybersecurity"},
    {"name": "Liza", "track": "Data"},
    {"name": "Ana", "track": "Cybersecurity"},

]


offer_tracks = {p["track"] for p in participants}

if len(offer_tracks) < 2:
    print("Not enough variety in tracks.")
else:
    print("Tracks offered in this event:", ", ".join(offer_tracks))


names = [p["name"] for p in participants]
duplicates = set([name for name in names if names.count(name) > 1])

if duplicates:
    for name in duplicates:
        print(f"\nDuplicate name found: {name}")

from collections import Counter

track_counts = Counter(p["track"] for p in participants)

print("\nParticipants per track:")
for track, count in track_counts.items():
    print(f"{track}: {count}")




'''

participants = [
    {f"name": f"{participants}", "track": ""},
    {"name": f"{participants}, "track": "Data"},
    {"name": f"{participants}, "track": "Cybersecurity"}
]

set_offer =[{f'CyberSecurity {participants}', f'Data{participants}', f'GameDev{participants}'}]
for set_offers in set_offer:
    print(set_offers)

set_difference = set(participants).difference(participants)
if set_difference:
    print("Enough participants!")
    for set_difference in set_difference:
        print(set_difference)
    else:
        print("Not enough variety in tracks.")
'''


