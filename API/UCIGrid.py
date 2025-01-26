import numpy as np

def generate_grid(lat_start, lat_end, lng_start, lng_end, grid_size):
    lat_range = np.arange(lat_start, lat_end, grid_size)
    lng_range = np.arange(lng_start, lng_end, grid_size)
    grid = [(lat, lng) for lat in lat_range for lng in lng_range]
    return grid

# Define UCI campus bounds and grid size
lat_start, lat_end = 33.643010689327156, 33.647603652014766  # test, might be wrong
lng_start, lng_end = -117.84728151352283, -117.83593481657893  # test, might be wrong
grid_size = 0.001

uci_grid = generate_grid(lat_start, lat_end, lng_start, lng_end, grid_size)
print(f"Total grid points: {len(uci_grid)}")
# print(generate_grid(lat_start, lat_end, lng_start, lng_end, grid_size))
