This is a pseudo code describing the implementation of the k-means clustering
algorithm using the data from a metroself.

Such an analysis could expose some of the hidden clustering or user-preferences
that are hidden in the data.
a
N = 15 # Number of Clusters, A parameter that can be played with.
MaxLat = # Maximum Latitude idenitifying a region
MinLat = # Minimum Latitude idenitifying a region
MaxLon = # Maximum Longitude idenitifying a region
MinLon = # Minimum Longitude idenitifying a region
la_d = MaxLat-MinLat
lo_d = MaxLon-MinLon
Lats_rand = np.random.random(N)*la_d+MinLat
Long_rand = np.random.random(N)*lo_d+MinLon

centroids = zip (Lats_rand,Long_rand) # random points within the lon and lat ranges.

num_centers = N;

def distance(point,pos):
    #compute distance between a point and one of the centroids of cluster.
    return distance

# Function returns centroid of a group of points
def calculate_centroid(data):
    cent = []
    for i in N:
        #query data to find all points with centroid for that cluster
        # cluster_i = {$match:{'cluster_number':i}}

        #a simple approximation for the centroid can be mean of
        #latitudes and logitudes for cluster_i since the region of interest
        #pipe_cent=[cluster_i,{$avg:'pos'}]
        # run query and aggregate average position of cluster i .

        cent.append(cent_i)
    return cent

# function to compute new centroid
def is_close_to(centroids,data):
    d = []
    for i in range(0,len(centroids)):
        for j in len(data):
        d[i] =distance(centroid[i],data.pos[j]):
        dmin = min(d);
        ind = find the index
        $set('cluster_number',centroid[ind])
    centroid = calculate_centroid(data)
    return data

K = Number of iterations of the k-means clustering algorithm
for i in range(0,K):
    data = is_close_to(centroid,data)

# Plotting function that takes data and plots the latitude and logitude on a make_pipeline
# and colors each cluster based on cluster_number.
def map_plot(data):
