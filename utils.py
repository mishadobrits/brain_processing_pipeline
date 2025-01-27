import re
import yaml
import os
import numpy as np
import pprint


def parse_filename(filename):
    pattern = r'^sub-([^_]+)_ses-d([^_]+)_task-rest_run-([^_]+)_atlas-([^.]+)\.csv$'
    match = re.match(pattern, filename)
    
    if not match:
        raise ValueError("Invalid filename format")
    
    return {
        'subject_id': match.group(1),
        'sessions_id': match.group(2),
        'run_id': match.group(3),
        'atlas_name': match.group(4)
    }


def generate_config_str(config):
    config_str = ""
    if config["fourier_transform"]["enable"]:
        config_str += f'fourier transform: {config["fourier_transform"]["method"]}\n'
    
    config_str += f'distance: {config["calculate_distance_matrix"]["method"]}'
    return config_str

def read_npy(name):
    with open(f"vars/{name}", "rb") as f:
        return np.load(f, allow_pickle=True)


def write_npy(name, data):
    with open(f"vars/{name}", "wb") as f:
        return np.save(f, data)


os.makedirs("vars/images", exist_ok=True)

with open("params.yaml", "r") as f:
    config = yaml.load(f, yaml.SafeLoader)
config_str = generate_config_str(config)


if __name__ == "__main__":
    print("Configuration:")
    pprint.pp(config)
    print()