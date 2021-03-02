# Dave.AI 

## Key Features 
This project is based on Python. It can be used as a sample backend for customer data processing.


## The key features are:
1) Given 2 CSV, it'll merge the data from both the files.
2) If a customer exists in both the CSVs, it'll consider two.csv is the latest available data and one.csv is the older data set.  
3) Sort the data based on the first name.
4) Finaly, will create a JSON file of JSON Objects of sorted data


Project structure
------------

    .
    ├── main.py                      > Main file which contains all the functionality to run the app and save the final JSON file.
    ├── config.py                    > Enviornment file storing both the file path
    ├── README.md                    > The top-level README for developers using this project.
    ├── requirements.txt             > All the requirements which is needed to run this project.
    ├── result.json                  > Output json file.
    ├── CSVs
        ├── one.csv 
        ├── two.csv 
        


--------
## Testing

  - This can run on Windows / Linux(Ubuntu 20.04) system.
  - It is advised to create a virtual enviornment if you have existing conflicts with python & other libraries/packages installtions.

## Quickstart
  - Install all necessary dependencies for this project from requirements.txt
    - Run `pip install -r requirements.txt` for installing dependencies. 
  - Please change parameters accordingly in (config.py) config file. (File_1 as `one.csv` and File_2 as `two.csv`)
  - Run app.py file in for turn on the API.
    - Run `python main.py`
  - You'll see you final result will be created as `result.json`.
