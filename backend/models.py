from sentence_transformers import SentenceTransformer, CrossEncoder
import torch


bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

cross_encoder_small = CrossEncoder(
    'cross-encoder/ms-marco-MiniLM-L-2-v2' if torch.cuda.is_available() else 'cross-encoder/ms-marco-TinyBERT-L-2-v2')
cross_encoder_large = CrossEncoder(
    'cross-encoder/ms-marco-MiniLM-L-12-v2' if torch.cuda.is_available() else 'cross-encoder/ms-marco-MiniLM-L-6-v2')
