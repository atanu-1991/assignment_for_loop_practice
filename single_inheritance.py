class Ineuron:
    company_website = 'https://learn.ineuron.ai/'
    name = 'iNeuron'

    def contact_details(self):
        print("Contact us at", self.company_website)


class DataScience(Ineuron):
    def __init__(self):
        self.year_of_establishment = 2018

    def est_details(self):
        print("{0} company was established in {1}".format(self.name, self.year_of_establishment))


ds = DataScience()
ds.est_details()