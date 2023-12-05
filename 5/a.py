# pylint: disable-all
import os

cwd = os.getcwd()

with open(f"{cwd}/5/input", "r") as file:
    input_data = file.read().split("\n")

with open(f"{cwd}/5/testInput", "r") as file:
    test_data = file.read().split("\n")


class Seed:
    def __init__(self, seedNumber):
        self.seedNumber = seedNumber

    def __repr__(self):
        return f"SeedNumber: {self.seedNumber}\n"


class Mapping:
    def __init__(self, destinationRangeStart, sourceRangeStart, rangeLength):
        self.sourceRangeStart = sourceRangeStart
        self.destinationRangeStart = destinationRangeStart
        self.rangeLength = rangeLength
        self.indexDifference = destinationRangeStart - sourceRangeStart

    def getDestinationFromSourceOrNone(self, source):
        if (source >= self.sourceRangeStart and source <= self.sourceRangeStart + self.rangeLength):
            return source + self.indexDifference
        return None

    def __repr__(self) -> str:
        return f"SourceRangeStart: {self.sourceRangeStart}\nDestinationRangeStart: {self.destinationRangeStart}\nRangeLength: {self.rangeLength}\nIndexDifference: {self.indexDifference}\n\n"


class Map:
    def __init__(self, name):
        self.name = name
        self.mappings = []
        pass

    def addMapping(self, mapping):
        self.mappings.append(mapping)

    def getDestinationFromSource(self, source):
        for mapping in self.mappings:
            destination = mapping.getDestinationFromSourceOrNone(source)
            if (destination != None):
                return destination
        return source

    def __repr__(self):
        return f"{self.name}, mappingCount: {len(self.mappings)}\n\n"


def read_input(input):
    maps = {}
    seeds = []

    seedToSoilMap = Map("seedToSoilMap")
    soilToFertilizerMap = Map("soilToFertilizerMap")
    fertilizerToWaterMap = Map("fertilizerToWaterMap")
    waterToLightMap = Map("waterToLightMap")
    lightToTemperatureMap = Map("lightToTemperatureMap")
    temperatureToHumidityMap = Map("temperatureToHumidityMap")
    humidityToLocationMap = Map("humidityToLocationMap")

    prevMap = seedToSoilMap

    for line in input:
        if (line == ""):
            continue

        if (line[0].isdigit()):
            destinationRangeStart, sourceRangeStart, rangeLength = line.strip().split()
            currMapping = Mapping(sourceRangeStart=int(sourceRangeStart), destinationRangeStart=int(
                destinationRangeStart), rangeLength=int(rangeLength))
            prevMap.addMapping(currMapping)

        # Update which map should be written to
        elif (line.startswith("seeds")):
            seedsInLine = line.split(":")[1].strip().split()
            for seed in seedsInLine:
                seeds.append(Seed(int(seed)))
            continue

        elif (line.startswith("soil-to-fertilizer")):
            prevMap = soilToFertilizerMap
            # print("switched to soil-to-fertilizer")

        elif (line.startswith("fertilizer-to-water")):
            prevMap = fertilizerToWaterMap
            # print("switched to fertilizer-to-water")

        elif (line.startswith("water-to-light")):
            prevMap = waterToLightMap
            # print("switched to water-to-light")

        elif (line.startswith("light-to-temperature")):
            prevMap = lightToTemperatureMap
            # print("switched to light-to-temperature")

        elif (line.startswith("temperature-to-humidity")):
            prevMap = temperatureToHumidityMap
            # print("switched to temperature-to-humidity")

        elif (line.startswith("humidity-to-location")):
            prevMap = humidityToLocationMap
            # print("switched to humidity-to-location")

    maps["seedToSoilMap"] = seedToSoilMap
    maps["soilToFertilizerMap"] = soilToFertilizerMap
    maps["fertilizerToWaterMap"] = fertilizerToWaterMap
    maps["waterToLightMap"] = waterToLightMap
    maps["lightToTemperatureMap"] = lightToTemperatureMap
    maps["temperatureToHumidityMap"] = temperatureToHumidityMap
    maps["humidityToLocationMap"] = humidityToLocationMap

    return seeds, maps


def run(input):
    seeds, maps = read_input(input)

    locations = []

    for seed in seeds:
        print(f"seed: {seed.seedNumber}")
        soil = maps["seedToSoilMap"].getDestinationFromSource(seed.seedNumber)
        print(f"soil: {soil}")
        fertilizer = maps["soilToFertilizerMap"].getDestinationFromSource(soil)
        print(f"fertilizer: {fertilizer}")
        water = maps["fertilizerToWaterMap"].getDestinationFromSource(
            fertilizer)
        print(f"water: {water}")
        light = maps["waterToLightMap"].getDestinationFromSource(water)
        print(f"light: {light}")
        temperature = maps["lightToTemperatureMap"].getDestinationFromSource(
            light)
        print(f"temperature: {temperature}")
        humidity = maps["temperatureToHumidityMap"].getDestinationFromSource(
            temperature)
        print(f"humidity: {humidity}")
        location = maps["humidityToLocationMap"].getDestinationFromSource(
            humidity)
        locations.append(location)
    return min(locations)


print(run(input_data))
