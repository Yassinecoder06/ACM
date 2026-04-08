place_zone = {}
place_record = {}
zone_record = {}
n = int(input())

for _ in range(n):
    place, zone = input().split()
    place_zone[place] = zone
    zone_record[zone] = 0

q = int(input())
for _ in range(q):
    place, record = input().split()
    record = int(record)
    zone_record[place_zone[place]] += record

print(max(zone_record, key=zone_record.get))

a = sorted(zone_record, key=zone_record.get)
print(a)