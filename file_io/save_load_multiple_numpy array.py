import os.path as osp
import numpy as np
import pandas as pd
import json


def save_multiple_numpy_array_to_file():
    data_dir = "./"
    filename = "multiple_numpy_array.txt"
    data_path = osp.join(data_dir, filename)

    rows = []
    row_head = ["targets", "pursuers"]
    rows.append(row_head)

    targets = np.array([[0, 1], [0, 3], [1, 1], [1, 3]])
    pursuers = np.array([[0, 0], [0, 2], [1, 0], [1, 2]])
    rows.append([targets.tolist(), pursuers.tolist()])
    rows.append([targets.tolist(), pursuers.tolist()])

    with open(data_path, "w") as output_file:
        for row in rows:
            output_file.write("\t".join(map(str, row)) + "\n")
            output_file.flush()
        pass


def load_multiple_numpy_array_to_file():
    data_dir = "./"
    filename = "multiple_numpy_array.txt"
    data_path = osp.join(data_dir, filename)

    data = pd.read_table(data_path)
    print(data)

    # KEY CODE:
    # Convert
    # s = "[[0, 1], [0, 3], [1, 1], [1, 3]]"
    # to list
    # json.loads(s) -> [[0, 0], [0, 2], [2, 0], [2, 2]]
    # and then to numpy array.
    targets = list(map(lambda x: np.array(json.loads(x)), data["targets"]))
    pursuers = list(map(lambda x: np.array(json.loads(x)), data["pursuers"]))
    print("targets:\n", targets)
    print("pursuers:\n", pursuers)

    pass


if __name__ == "__main__":
    # save_multiple_numpy_array_to_file()
    load_multiple_numpy_array_to_file()
    pass

