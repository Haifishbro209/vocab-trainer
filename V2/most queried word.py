from DataBase import *

result = (session.query(Vocab.id,func.count(Query.vocab_id).label("query_count"))
        .join(Query)
        .group_by(Vocab.id)
        .order_by(func.count(Query.id).desc())
        .first()
        )

print(result)