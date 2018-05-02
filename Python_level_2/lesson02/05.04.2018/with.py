
fl = open("file.txt")
fl.read(1024)
fl.close()

#############################################################################

with open("file.txt") as fl:

    fl.read(1024)

#############################################################################

class CWith():

    def __enter__(self):

        # self.db

        self.db.start_transaction()
        
        return self.db.cursor()

    def __exit__(self, err, value, tb):

        self.db.commit()

conn = CWith()

with conn as cursor:

    cursor.update(...)

