import torch

from gia.model.embedding import Embeddings


def test_embeddings():
    embedding_layer = Embeddings(embedding_dim=32, vocab_size=32, nb_bins=8, max_nb_observation_tokens=7)
    tokens = torch.randint(0, 1024, (10, 7))
    tokens[:, 3] = 32 + 8  # separator token
    embeddings = embedding_layer(tokens)
    assert embeddings.shape == (10, 7, 32)
