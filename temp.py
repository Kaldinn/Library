import csv


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

    query = ""

    for book in table:

        query += f"""
            INSERT INTO [lib].[books]
            ([title], [authors], [publication_year], [image_url], [small_image_url])
            VALUES(
                '{book['title']}',
                '{book['authors']}',
                {book['publication_year']},
                '{book['image_url']}',
                '{book['small_image_url']}'
            );
        """

with open(file="query.sql", mode="w", encoding="utf-16") as file:
    file.write(query)
    
    
