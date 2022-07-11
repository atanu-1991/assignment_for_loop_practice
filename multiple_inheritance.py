class Ineuron:
    company_website = 'https://learn.ineuron.ai/'
    name = 'iNeuron'

    def contact_details(self):
        print("Contact us at", self.company_website)

class OS:
    multi_task = True
    os_name = "Windows OS"
    name = 'atanu'


class Windows(Ineuron, OS):
    def __init__(self):
        if self.multi_task == True:
            print("multi_task")
        print("Name : {}".format(self.name))


windows = Windows()