import logging
logging.basicConfig(filename="dicts.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')

class Dicts:
    logging.info("Accessing Dicts Class")
    def __init__(self,lsts):
        self.lsts = lsts

    def extract_dict(self):
        logging.info("Extracting dict entity from extract_dict method")
        try:
            for i in self.lsts:
                if type(i) == dict:
                    print(i)
        except Exception as e:
            logging.exception(e,"Please enter a valid list")


    def keyNum(self):
        logging.info("Method to find key number in dictionary")
        try:
            for i in self.lsts:
                if type(i) == dict:
                    print("Number of keys in dict element is", len(i))

                    logging.info("key number is %s",len(i))

        except Exception as e:
            logging.exception(e)


dictObj = Dicts([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])

dictObj.extract_dict()
dictObj.keyNum()