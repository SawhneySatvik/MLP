import numpy as np

def split_train_test_data(data, test_ratio):
    np.random.seed(42)
    
    shuffled_indices = np.random.permutation(len(data))
    
    test_set_size = int(len(data)*test_ratio)
    
    test_indices = shuffled_indices[: test_set_size]
    train_indices = shuffled_indices[test_set_size :]
    
    return data.iloc[train_indices], data.iloc[test_indices]