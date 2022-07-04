import logging
logging.basicConfig(filename="lists.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')

class Lists:
    logging.info("Accessing List Class")
    def __init__(self,lst):
        self.lst = lst


    def extract_list(self):
        logging.info("Extracting List Entity from extract_list method")
        try:
            for i in self.lst:
                if type(i) == list:
                    print(i)

            logging.info("List Extracct Successfull")

        except Exception as e:
            logging.exception(e,"Please enter a valid list")


    def sum_numericdata_fromlist(self):
        logging.info("calculating sum of integer value from list")
        sum = 0
        try:
            for i in self.lst:
                if type(i) == list or type(i) == dict or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j

                if type(i) == dict:
                    for key,values in i.items():
                        if type(key) == int:
                            sum = sum + key
                        elif type(values) == values:
                            sum = sum + values

            print(sum)
            logging.info("Summation of integer value from list is successgull")
            logging.info("sum of list entity is %s",sum)

        except Exception as e:
            logging.exception(e)



    def odd_values_out_fromlist(self):
        logging.info("Method to filter out odd values from the list")
        try:
            print(self.lst)
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            if(j%2 == 0):
                                i.remove(j)

            print(self.lst)
            logging.info("Odd values out from the list is successfull")

        except Exception as e:
            logging.exception(e)


    def extract_ineuron(self):
        logging.info("Method to extract 'ineuron' from the list")
        try:
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if j == "ineuron":
                            print(j)

                if type(i) == dict:
                    for k, v in i.items():
                        if v == "ineuron":
                            print(v)

            logging.info("'ineuron' is extracted successfully")
        except Exception as e:
            logging.exception(e)


    def num_occurance(self):
        logging.info("Method to count nnumber of ooccurence")
        try:
            num_list = []
            txt_list = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            num_list.append(j)
                        else:
                            txt_list.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        if type(v) == int:
                            num_list.append(v)
                        else:
                            txt_list.append(v)

            for num in set(num_list):
                print(num, ":", num_list.count(num))
            for txt in set(txt_list):
                print(txt, ":", txt_list.count(txt))

            logging.info("number_occurence method is executed successfully")

        except Exception as e:
            logging.exception(e)

    def multiplication(self):
        logging.info("method to find out multiplication of all numeric value in the individual collection inside dataset")
        try:
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    mul = 1
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                        else:
                            mul = ""
                    print(mul)

                if type(i) == dict:
                    mul = 1
                    for k, v in i.items():
                        if type(v) == int:
                            mul = mul * v
                    print(mul)

            logging.info("Multiplication is executed successfully")
        except Exception as e:
            logging.exception(e)

    def unwrap_list(self):
        logging.info("method to unwrape all the collection inside collection and create a flat list")
        try:
            new_list = []

            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        new_list.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        new_list.append(v)

            print(new_list)

            logging.info("Unwrapp all the collection data inside list is successfull")
        except Exception as e:
            logging.exception(e)

    def revers_list(self):
        logging.info("Reversing a list")
        try:
            new_lst = self.lst[::-1]
            print(new_lst)
            logging.info("Reverse a list is successfull")
        except Exception as e:
            logging.exception(e)

listObj = Lists([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
listObj.extract_list()
listObj.sum_numericdata_fromlist()
listObj.odd_values_out_fromlist()
listObj.extract_ineuron()
listObj.num_occurance()
listObj.multiplication()
listObj.unwrap_list()
listObj.revers_list()