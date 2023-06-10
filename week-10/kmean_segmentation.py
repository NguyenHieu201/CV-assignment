import cv2
from sklearn.cluster import KMeans
import numpy as np

img_path = "./input/phong-nam-valley-cao-bang1.jpg"
img = cv2.imread(img_path)

b, g, r = cv2.split(img)
color_feature = np.stack([b.flatten(), g.flatten(), r.flatten()])
color_feature = color_feature.T

n_clusters = 8
kmeans = KMeans(n_clusters=n_clusters, n_init=10, max_iter=300)

# fit kmeans
kmeans.fit(color_feature)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# assign new color to pixel
for i in range(n_clusters):
    color_feature[np.where(labels == i)] = centroids[i]



