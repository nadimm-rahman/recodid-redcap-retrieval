#!/usr/bin/python3
import pandas as pd
import argparse


def get_args():
    """
    Handle script arguments
    :return: Script arguments
    """
    parser = argparse.ArgumentParser(description="Script to process survey results")
    parser.add_argument('-f', '--file', help='Raw redCAP survey results file', type=str, required=True)
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    redcap = pd.read_csv(args.file, sep=",", header=0)

    columns = redcap.columns
    subset = redcap[redcap.record_id != 0]      # Get the data section of the file data frame

    # Iterate over the data frame and check for non-zero values and list what column these appear in
    # for label, row in subset.iterrows():
    #     print(row.record_id)        # Record ID being searched
    #     for index, value in row.items():
    #         if value == 1:
    #             print(index)        # The column where a non-zero value were found

    for label, row in subset.iterrows():
        for index, value in row.items():
            if index == "record_id":
                print("*" * 100)
                print("NEW RECORD:" +str(value))
            elif index in ['name_first', 'name_last', 'email']:
                print(index, value)
            elif value != 0:
                if str(value) != "nan":
                    print(index, value)