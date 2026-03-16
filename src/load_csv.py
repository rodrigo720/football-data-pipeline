import kagglehub
import os
from pathlib import Path
import shutil

OUTPUT_PATH = Path(f"/data/raw")

def main():
    OUTPUT_PATH.mkdir(parents=True,exist_ok=True)

    temp_path = kagglehub.dataset_download("marcoduca/dataset-partite-di-calcio")

    contatore=0

    for file in os.listdir(temp_path):    #scorro in tutte le liste dei soli NOMI che sono situate nella directory
        #le mie coordinate
        source_path = os.path.join(temp_path,file)  #da dove prendo i file situate in temp_path
        destination_file = OUTPUT_PATH/file         #dove lo metto di destinazione

        shutil.copy2(source_path,destination_file)
        contatore+=1

        print(f"il file {contatore} si è spostato nella cartella {destination_file}")


if __name__=="__main__":
    main()