from main.filters.fasttext_filter.model import Model
from main.filters.fasttext_filter.settings import Settings
from main.filters.utils import *

Settings.do_the_prerequisites()


class FasttextFilter():

    def __init__(self):
        self.bio_model = Model()

    def train(self):
        self.bio_model.train_supervised(auto=True, save=True)
        self.bio_model.test()
        self.bio_model.predict_all()
        self.bio_model.save_results()

    def load(self):
        self.bio_model.load_model()

    def predict(self, text):
        Logger.info("Predicting using fasttext model ...")
        return self.bio_model.predict(text)
