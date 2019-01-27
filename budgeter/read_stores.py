
import os
import csv

"""Import store data from csv file into dictionary."""

# directory for the data files
data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

def get_store_data(csvf="Stores_dict.csv"):
    """Get the store data from a csv file.

    Parameters
    ----------
    csvf : str
        Name of csv file in the data directory.
        Defaults to Stores_dict.csv.

    Returns
    -------
    stores : dict
        Dictionary where keys are store categories
        and values are lists of store names in the
        given category.

    """
    stores = {}
    with open(os.path.join(data_dir, csvf), "r") as f:
        fo = csv.reader(f)
        for line in fo:
            stores[line[0]] = line[1:]
    return stores

def get_store_category(store_name, csvf="Store_dict.csv"):
    """Returns the store category.

    Parameters
    ----------
    store_name : str
        Name of the store.
    csvf : str
        Name of store csv file. Defaults to
        Stores_dict.csv.

    """
    data = get_store_data(csvf)
    for category in data:
        if store_name in data[category]:
            return category
    return None
