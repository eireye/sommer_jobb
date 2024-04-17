#Noen funksjoner som kan åpne stor sasfil i chunks og kun gi tilbake en sammensatt fil med de kolonnene man ønsker. For å spare plass om nødvendig

import pandas as pd
import numpy as np

def preprocess_chunk(chunk):
    # Fjern unødvendige kolonner
    kolonner_som_skal_beholdes = [] # Lag liste av kolonnene som skal brukes/trengs
    chunk = chunk[kolonner_som_skal_beholdes]
        
    return chunk



def df(path_to_df):


    chunk_size = 1000000  # Velg ønsket chunk size
    chunks = pd.read_sas(path_to_df, encoding='latin1', chunksize=chunk_size)
    processed_chunks = [preprocess_chunk(chunk) for chunk in chunks]
    
    df = pd.concat(processed_chunks, ignore_index=True)
    return df
    

    
