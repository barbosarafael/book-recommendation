import numpy as np

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