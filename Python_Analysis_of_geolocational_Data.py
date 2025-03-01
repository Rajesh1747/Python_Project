def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:
            parts = line.strip().split(',')
            data.append((float(parts[0]), float(parts[1])))
    return data

def summary_statistics(data):
    lats, lons = zip(*data)
    return {
        "latitude": (min(lats), max(lats), sum(lats)/len(lats)),
        "longitude": (min(lons), max(lons), sum(lons)/len(lons))
    }

def plot_data(data):
    for lat, lon in data:
        print(f"Point at ({lat}, {lon})")

if __name__ == "__main__":
    file_path = input("Enter path to CSV file: ")
    data = load_data(file_path)
    print("Summary Statistics:", summary_statistics(data))
    plot_data(data)

