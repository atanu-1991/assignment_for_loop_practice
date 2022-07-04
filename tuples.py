import logging
logging.basicConfig(filename="tuples.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')

class Dicts:
    logging.info("Accessing Tuples Class")
    def __init__(self,lsts):
        self.lsts = lsts

    logging.info("Extracting dict entity from extract_tuple method")
    def extract_tuple(self):
        try:
            for i in self.lsts:
                if type(i) == tuple:
                    print(i)
        except Exception as e:
            logging.exception(e,"Please enter a valid dictionary")
