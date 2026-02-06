from embedding_utils.Embedding import Embedding
import ollama


class OllamaEmbedding(Embedding):
    def __init__(self, model_name: str, num_dimensions: int):
        super().__init__(model_name, num_dimensions)

    def embed(self, texts) -> str:
        r = ollama.embed(model=self.model_name, input=texts)
        return r["embeddings"][0]
