from os import listdir
from os.path import isfile, join
from pathlib import Path
from utils import config, parse_filename, write_npy
import numpy as np
import pandas
import ast


data = []
for group in config['dataset_filtering']["groups"]:
    path = Path(f"{config['dataset_filtering']['path_to_dataset_folder']}/{group}")
    csv_file_list = [f for f in listdir(path) if isfile(path / f) and f.endswith(".csv")]

    for csv_file in csv_file_list:
        csv_data = pandas.read_csv(path / csv_file)
        if csv_data.shape != ast.literal_eval(config['dataset_filtering']['allowed_shape']):
            continue

        csv_data = csv_data.drop("Unnamed: 0", axis=1)
        new_elem = parse_filename(csv_file)
        new_elem["group"] = group
        new_elem["data"] = csv_data
        data.append(new_elem)

write_npy("data.npy", data)