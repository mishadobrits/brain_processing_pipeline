from scipy.spatial import distance_matrix
from utils import config, read_npy, write_npy
import numpy as np


data = read_npy("data1.npy")

method = config["calculate_distance_matrix"]["method"]
allowed_methods = ["cosine dist", "angle", "mse", "l2 norm"]

rt = []
for cur_record in data:
    record_to_append = cur_record
    cur_data = record_to_append.pop("data")
    if method == allowed_methods[0]:
        value = 1 - np.corrcoef(cur_data)
    elif method == allowed_methods[1]:
        value = np.acos(np.corrcoef(cur_data))
    # elif method == "wasserstein":
    #     pass
    elif method in "mse" or "l2 norm": 
        cur_data = np.array(cur_data)
        value = np.square(np.abs(cur_data[:, None, :] - cur_data[None, :, :])).mean(axis=2) # distance_matrix(cur_data, cur_data)
        if method == "l2 norm":
            value = np.sqrt(value)
    else:
        assert method in allowed_methods, "Incorrect method for calculating distance_matrix: {method}. Should be one of {allowed_methods}"
    
    record_to_append["distance_matrix"] = value
    rt.append(record_to_append)

write_npy("distance_matrix.npy", rt)