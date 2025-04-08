from DataBase import session, Vocab, Query
from random import sample
import numpy as np

def smoothedError(vocabId):
    alpha = 0.5 
    queries =session.query(Query).filter_by(vocab_id = vocabId).all()
    try:
        time_error_List = []
        for query in queries:
            time_error = (query.timestamp,query.error_rate) #e.g {1.0, datetime.datetime(2025, 2, 26, 7, 14, 8, 409424)}
            time_error_List.append(time_error)
        time_error_List.sort() #liste ist von alt nach neu sortiert
        smoothedError = time_error_List[0][1]
        for q in range(1,len(time_error_List)):
            error = time_error_List[q][1]
            smoothedError = alpha * error + (1-alpha)*smoothedError
        return smoothedError
    except IndexError:
        return 0
def smartReturn(size):
    randomSize = int(size/3)
    smartSize = int(size/3)*2
    all_vocab = session.query(Vocab).all()
    weights = []
    for vocab in all_vocab:
        weights.append(smoothedError(vocab.id))
    print(weights)
    chosen_vocab = np.random.choice(all_vocab, size=int(smartSize), replace=False, p=np.array(weights) / sum(weights)) + randomReturn(randomSize)
    
    chosen_vocab_list  = []
    for word in chosen_vocab:
        obj = {"french": word.french,
               "german": word.german,
               "id": word.id}
        chosen_vocab_list.append(obj)
    print(chosen_vocab_list)
    return chosen_vocab_list

def randomReturn(size): 
    all_vocab = session.query(Vocab).all()
    chosen_vocab  = sample(all_vocab,size)
    vocab_list  = []
    for word in chosen_vocab:
        obj = {"french": word.french,
               "german": word.german,
               "id": word.id}
        vocab_list.append(obj)
    return vocab_list

if __name__ == "__main__":
    smartReturn(5)




