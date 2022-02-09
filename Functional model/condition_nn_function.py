class fn_model(torch.nn.Module):
    def __init__(self, tnh=False):
        super(fn_model, self).__init__()
        self.tnh = tnh
        self.linear1 = torch.nn.Linear(x_train.shape[1], 50)
        self.linear2 = torch.nn.Linear(50, 1)
    def forward(self, x):
        if self.tnh:
            layer1 = F.tanh(self.linear1(x))
        else:
            layer1 = F.relu(self.linear1(x)) 
        out_put = F.relu(self.linear2(layer1))
        return out_put
model = fn_model(True)
