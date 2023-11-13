from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    allowed_exensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        with open(path, 'r') as fid:
            for line in fid.readlines():
                if line != '':
                    data = line.split(' - ')
                    quotes.append(QuoteModel(data[0], data[1]))
        return quotes