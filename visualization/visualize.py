from evalys.jobset import JobSet
import matplotlib.pyplot as plt
import json
import numpy as np

js = JobSet.from_csv("../visualization/output/imt_jobs.csv")
js.plot(with_details=True)

#Loading spaces load log.
with open('../visualization/output/storages_load.json') as f:
    loads = json.load(f)

x_axis = loads["time"]
index = np.arange(len(x_axis))
del loads["time"]
y_axis = loads["qb0_disk"]
fig, subplots = plt.subplots(3, 1, sharex=True)
current_plot = 0
min_size = 0
max_size = 0

#Compute max storage size
for storageSpace, load in loads.items():
    if max(load) > max_size:
        max_size = max(load)

# Generating graph for each storage space
for storageSpace, load in loads.items():
    subplots[current_plot].set_title(storageSpace)
    subplots[current_plot].set_xlabel("time in ms")
    subplots[current_plot].set_ylabel("load in bytes")
    subplots[current_plot].set_ylim(min_size, max_size)
    subplots[current_plot].bar(index, load, align="edge", width=1)
    current_plot += 1

plt.xticks(index, x_axis)
plt.show()