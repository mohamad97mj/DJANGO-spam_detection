# word based filter
class PrimaryFilter():

    def __init__(self, filter_list):
        self.filter_list = filter_list

    def filter(self, text):
        return text not in self.filter_list
