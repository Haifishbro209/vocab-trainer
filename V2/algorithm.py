from DataBase import session, Vocab
from random import sample
# Beispiel: Alle Vokabeln auslesen
def randomReturn(size):
    all_vocab = session.query(Vocab).all()
    choosen_vocab  = sample(all_vocab,size)
    vocab_list  = []
    for word in choosen_vocab:
        obj = {"french": word.french,
               "german": word.german}
        vocab_list.append(obj)
    print(vocab_list)
    return vocab_list
if __name__ == "__main__":
    pass



