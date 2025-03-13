from DataBase import session, Vocab, Query
from random import sample

def smoothedError(vocabId):
    queries =session.query(Query).filter_by(vocab_id = vocabId).all()
    time_error_List = []
    for query in queries:
        time_error = (query.timestamp,query.error_rate) #e.g {1.0, datetime.datetime(2025, 2, 26, 7, 14, 8, 409424)}
        time_error_List.append(time_error)
    time_error_List.sort() #liste ist von alt nach neu sortiert
    print(time_error_List)
def randomReturn(size): #only 33% random
    all_vocab = session.query(Vocab).all()
    choosen_vocab  = sample(all_vocab,int(size))
    for vocab in all_vocab:
        smoothedError(vocab.id)
    vocab_list  = []
    for word in choosen_vocab:
        obj = {"french": word.french,
               "german": word.german,
               "id": word.id}
        vocab_list.append(obj)
    return vocab_list

if __name__ == "__main__":
    randomReturn(90)





