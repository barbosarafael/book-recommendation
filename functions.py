import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def save_sparse_csr(filename, array):
    """
    Função para salvar sparse_matrix 
    Retirado de: https://stackoverflow.com/a/8980156
    """    
    np.savez(filename, data=array.data, indices=array.indices,
             indptr=array.indptr, shape=array.shape)

def load_sparse_csr(filename):
    """
    Função para carregar o sparse_matrix 
    Retirado de: https://stackoverflow.com/a/8980156
    """
    loader = np.load(filename)
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),
                      shape=loader['shape'])

def filter_list_ordered(df: pd.DataFrame, col: str, list_filter: list):

    ind = [df.index[df[col] == i].tolist() for i in list_filter]

    flat_ind = [item for sublist in ind for item in sublist]

    df1 = df.reindex(flat_ind)

    return df1