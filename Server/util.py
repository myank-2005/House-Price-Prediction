# import json
# import pickle 
# # import sklearn 


# __locations=None
# __data_columns=None
# __model=None

# def get_location_names():
#     return __locations

# def load_saved_artifcates():
#     print("Loading Saved artificats...starts")
#     global __data_columns
#     global __locations

#     with open("./Server/artifacts/columns.json","r") as f:
#         __data_columns=json.load(f)['data_columns']
#         __location=__data_columns[3:]

#     with open("./Server/artifacts/House_Price_Prediction.pickle","rb") as f:
#         __model=pickle.load(f)
#     print("loading saved artifacts...done")  #10:34
         

# if __name__ == "__main__":
#     load_saved_artifcates()
#     print(get_location_names()) 


import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
        try:
            loc_index = __data_columns.index(location.lower())
        except:
            loc_index=-1
        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        return round(__model.predict([x]) [0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading Saved artifacts...starts")
    global __data_columns
    global __locations
    global __model

    # Load columns.json
    with open("./Server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        print(f"Loaded data columns: {__data_columns}")
        __locations = __data_columns[3:]   # Assign to __locations, not __location

    # Load the model
    with open("./Server/artifacts/House_Price_Prediction.pickle", "rb") as f:
        __model = pickle.load(f)
    
    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())  # This should now print the list of locations
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 2))
    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('Kalhalli',1000, 2, 2))
    print(get_estimated_price('Ejipura',1000, 2, 2))

