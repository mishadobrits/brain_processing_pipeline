from utils import config, read_npy, write_npy
import numpy as np


def process_data(data):
    new_data = []
    for i, elem in enumerate(data):
        fft_value = np.fft.fft(elem["data"], axis=0)
        if method == allowed_methods[0]:
            pass
        elif method == allowed_methods[1]:
            fft_value = np.abs(fft_value)
        elif method == allowed_methdos[2]:
            fft_value = fft_value / np.abs(fft_value)
        else:
            error_msg = f"Incorrect method for doing fourier transform: {current_method}. Should been one of {allowed_methods}"
            assert current_method in allowed_methods, error_msg
        elem["data"] = fft_value
        new_data.append(elem)
    
    return new_data


method = config["fourier_transform"]["method"]
allowed_methods = ["simple fft", "fft + abs", "fft + norm"]

data = read_npy("data.npy")

if config["fourier_transform"]["enable"]:
    data = process_data(data)

write_npy("data1.npy", data)