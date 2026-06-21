import chromadb
import pandas as pd
import uuid

class Portfolio:
    def __init__(self, file_path = 'app/resources/my_portfolio.csv' ):
        self.file = file_path
        self.data = pd.read_csv(self.file)
        self.client = chromadb.PersistentClient('vectorstore')
        self.collections = self.client.get_or_create_collection(name = 'my_collections')
    
    def load_portfolio(self):
        if not self.collections.count():
            for _, row in self.data.iterrows():
                self.collections.add(documents=row['Techstack'], metadatas = {"links": row['Links']}, ids=[str(uuid.uuid4())])
        
    def query_links(self, skills):
        return self.collections.query(query_texts = skills, n_results = 2).get('metadatas', [])
            