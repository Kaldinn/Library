from db_manager import ServerSQL as chuj
from config import lib_db

def get_all():

    with open(file="books.tsv", mode="r", encoding="utf-16") as file:
        
        lines = [
            line.split("\t")
            for line in file.readlines()
        ][2:]
        

        table = [
            {
                "title": row[9].replace("'", "''"),
                "authors": row[7].replace("'", "''"),
                "publication_year": int(float(row[8])) if row[8] else 0,
                "image_url": row[21],
                "small_image_url": row[22].replace("\n", "")
            }
            for row in lines
        ]
        return table
    
    print(table)

        