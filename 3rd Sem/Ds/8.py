import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a Basemap instance
m1 = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=60, llcrnrlon=-130, urcrnrlon=10)
m2 = Basemap(projection='merc', llcrnrlat=10, urcrnrlat=50, llcrnrlon=30, urcrnrlon=90)

# Load geographic data for European and American cities
lats1 = [51.5074, 40.7128, 34.0522, 48.8566]
lons1 = [-0.1278, -74.0060, -118.2437, 2.3522]
names1 = ['London', 'New York', 'Los Angeles', 'Paris']
# Load geographic data for Indian cities
lats2 = [28.6139, 19.0760, 13.0827, 17.3850]
lons2 = [77.2090, 72.8777, 80.2707, 78.4867]
names2 = ['New Delhi', 'Mumbai', 'Chennai', 'Bangalore']


# Plot the geographic data for European and American cities
m1.drawcoastlines()
m1.drawcountries()
m1.scatter(lons1, lats1, latlon=True, marker='o', color='red', label='Cities')
plt.title('Geographic Data Visualization - North America')
plt.legend()
plt.show()

# Plot the geographic data for Indian cities
m2.drawcoastlines()
m2.drawcountries()
m2.scatter(lons2, lats2, latlon=True, marker='s', color='blue', label='Cities')
plt.title('Geographic Data Visualization - India')
plt.legend()
plt.show()