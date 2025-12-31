def load_locations(filename):
    locations = {}
    with open(filename, "r") as file:
        for line in file:
            from_location, to_location = line.strip().split(":")
            locations[from_location] = to_location.strip().split(" ")
    return locations


def copy_dictionary(locations):
    locations_copy = locations.copy()
    for from_location, to_locations in locations_copy.items():
        locations_copy[from_location] = locations[from_location].copy()
    return locations_copy


def compress_locations(locations, target):
    compressed_locations = {target: 1}
    locations_copy = copy_dictionary(locations)
    compressed_locations_temp = compressed_locations.copy()

    if target in locations_copy.keys():
        locations_copy.pop(target)

    while len(locations_copy.keys()) > 0:
        compressed_locations_keys = compressed_locations.copy().keys()
        for location_name, location_value in locations_copy.copy().items():
            for compress_location_name in compressed_locations_keys:
                if compress_location_name in location_value:
                    locations_copy[location_name].remove(compress_location_name)
                    if len(locations_copy[location_name]) == 0:
                        locations_copy.pop(location_name)
                        compressed_locations[location_name] = (compressed_locations_temp[
                                                                   location_name] if location_name in compressed_locations_temp else 0) + \
                                                              compressed_locations_temp[compress_location_name]
                    if location_name in compressed_locations_temp:
                        compressed_locations_temp[location_name] += compressed_locations_temp[compress_location_name]
                    else:
                        compressed_locations_temp[location_name] = compressed_locations_temp[compress_location_name]

    return compressed_locations


def remove_locations(locations, locations_to_remove):
    locations_copy = copy_dictionary(locations)

    removed_locations = set()
    for location_key, location_values in locations.items():
        if location_key in locations_to_remove:
            locations_copy.pop(location_key)
        else:
            for location_value in location_values:
                if location_value in locations_to_remove:
                    locations_copy[location_key].remove(location_value)
                    if len(locations_copy[location_key]) == 0:
                        removed_locations.add(location_key)

    if len(removed_locations) > 0:
        return remove_locations(locations_copy, removed_locations)

    return locations_copy


def main():
    locations = load_locations("input.txt")

    compressed_locations = compress_locations(locations, "out")
    without_dac_compressed = compress_locations(remove_locations(locations, "dac"), "out")
    without_fft_compressed = compress_locations(remove_locations(locations, "fft"), "out")
    without_both_compressed = compress_locations(remove_locations(locations, {"dac", "fft"}), "out")

    print("Task1", compressed_locations["you"])
    print("Task2", compressed_locations["svr"] - without_dac_compressed["svr"] - without_fft_compressed["svr"] +
          without_both_compressed["svr"])


if __name__ == "__main__":
    main()
