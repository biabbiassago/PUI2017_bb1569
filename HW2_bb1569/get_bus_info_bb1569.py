from __future__ import print_function
import pylab as pl
import json
import numpy as np
import urllib.request as urllib
import os
import sys

if len(sys.argv) ==4:
	MTA_KEY=sys.argv[1]
	BUS_LINE=sys.argv[2]
	output_csv=sys.argv[3]
else:
	print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")

fout = open(output_csv, "w")
fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+MTA_KEY+"&VehicleMonitoringDetailLevel=calls&LineRef="+BUS_LINE
response=urllib.urlopen(url)
datamta=response.read().decode("utf-8")
datamta=json.loads(datamta)

vehicleact=datamta["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
busnum=np.size(vehicleact)

print("Bus Line %s"%(BUS_LINE))
print("Number of Active Buses: %i" %(busnum))

for b in range(0,busnum):
	loc=(vehicleact[b]["MonitoredVehicleJourney"]["VehicleLocation"])
	lat=loc["Latitude"]
	lon=loc["Longitude"]
	#print("Bus %i is at latitude %f and longitude %f"%(b+1,lat,lon))
	if np.size(vehicleact[b]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']) == 0:
		StopName = 'N/A'
	else:
		StopName = vehicleact[b]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
	if np.size(vehicleact[b]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']) == 0:
		StopStatus = 'N/A'
	else:
		StopStatus=vehicleact[b]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']


	fout.write('{},{},{},{}\n'.format(lat,lon,StopName,StopStatus))




