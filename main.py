import json
import pandas as pd
from config import File_1, File_2


def dave_pipeline(File_1, File_2):
    df_1 = pd.read_csv(File_1)
    df_2 = pd.read_csv(File_2)

    # merge both file
    df = pd.concat([df_1, df_2], ignore_index=True)

    # Deduplication of entries by keeping the latest entry
    final = df.drop_duplicates(
        subset={"first_name", "last_name"}, keep="last", inplace=False
    )

    # Sort the data based on the first name
    final_sort = final.sort_values("first_name").reset_index(drop=True)

    # record of the final data to a json file
    record = final_sort.to_dict("records")

    with open("result.json", "w") as fout:
        json.dump(record, fout)


if __name__ == "__main__":
    dave_pipeline(File_1, File_2)
