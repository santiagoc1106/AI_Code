from fastai.text.all import *
from fastai.callback.progress import ShowGraphCallback

if __name__ == '__main__':
    # Path to the IMDB dataset
    path = untar_data("https://raw.githubusercontent.com/santiagoc1106/AI_Code/main/data_1.tar")
    
    # # DataBlock setup
    
    
    # # Create data loaders
    # dls = imdb.dataloaders(path, bs = 512)

    # # Create a text classifier learner
    # # learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)

    # dls_lm = TextDataLoaders.from_folder(path, is_lm=True, valid_pct=0.1)

    # learn = language_model_learner(dls_lm, AWD_LSTM, metrics=[accuracy, Perplexity()], path=path, wd=0.1).to_fp16()

    # TEXT = "Spider-man"
    # N_WORDS = 100
    # N_SENTENCES = 1
    # preds = [learn.predict(TEXT, N_WORDS, temperature=0.75) 
    #      for _ in range(N_SENTENCES)]
    
    # print("\n".join(preds))



