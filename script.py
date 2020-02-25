import torch

def main(batch_size):
    x = torch.randn(batch_size)
    print(x.sum().item())
    print(x.shape)