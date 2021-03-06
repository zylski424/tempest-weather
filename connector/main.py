from structs.stations import Stations
from structs.observations import Observations
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--backfill", help="Backfill entire database",action="store_true")
parser.add_argument("--backfillAll", help="Backfill entire database",action="store_true")
parser.add_argument("--daily", help="Run daily calculations",action="store_true")


args = parser.parse_args()

stations = Stations()
observations = Observations(stations.stationId)

if args.backfillAll:
	observations.backFillAll(stations.deviceId)
	observations.dailyBackfill(stations.deviceId,Full = True)

elif args.daily:
	observations.dailyBackfill(stations.deviceId,Full = False)

elif args.backfill:
	observations.backFill(stations.deviceId)
else:
	observations.uploadCurrent()
