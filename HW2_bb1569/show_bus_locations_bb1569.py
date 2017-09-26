from __future__ import print_function
import pylab as pl
import json
import urllib.request as urllib
import os
import sys


if len(sys.argv) ==3:
	MTA_KEY=sys.argv[1]
	BUS_LINE=sys.argv[2]
else:
	print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE>")


url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+MTA_KEY+"&VehicleMonitoringDetailLevel=calls&LineRef="+BUS_LINE
print(url)
response=urllib.urlopen(url)
datamta=response.read().decode("utf-8")
datamta=json.loads(datamta)


#to run with code saved locally:

#with open('vehicle-monitoring.json') as data:
	#datamta=json.load(data)


vehicleact=datamta["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
busnum=len(vehicleact)
#print(busnum)
#print(type(busnum))

print("Bus Line %s"%(BUS_LINE))
print("Number of Active Buses: %i" %(busnum))


for b in range(busnum):
	loc=(vehicleact[b]["MonitoredVehicleJourney"]["VehicleLocation"])
	#print(type(loc['Longitude'])) to check what type lat and long are.
	print("Bus %i is at latitude %f and longitude %f"%(b+1,loc["Latitude"],loc["Longitude"]))

