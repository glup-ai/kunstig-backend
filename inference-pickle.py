import pickle

model_path = './trained_models/network-snapshot-010200.pkl'

def load_model():
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
        print(loaded_model)

if __name__ == "__main__":
    load_model()