import glob
import os
from sqlalchemy import create_engine

class Marketplace:
    def __init__(self)-> None:
        self.image_path = glob.glob('smaller_images/*.jpg')
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = '' # Change it for your AWS endpoint
        USER = 'postgres'
        PASSWORD = ''
        PORT = 5432
        DATABASE = 'postgres'
        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")


    def murg(self, index):
        image_path = self.image_path[index]
        base=os.path.basename(image_path)
        path = os.path.splitext(base)[0]
        print(path)

        cur = self.engine.execute(f"SELECT * FROM products WHERE id='{path}'")
        return cur.fetchone()



        #return image, class_index


go = Marketplace()
go.__getitem__(4)
go.murg(4)
