from main.filters.fasttext_filter.model import Model
from main.filters.fasttext_filter.settings import Settings

Settings.do_the_prerequisites()


class FasttextFilter():

    def train(self):
        bio_model = Model(rebuild_model=True)
        # bio_model.load_model()
        bio_model.test()
        bio_model.predict_all()
        bio_model.save_results()

    def load(self):
        bio_model = Model(rebuild_model=False)
        return bio_model
