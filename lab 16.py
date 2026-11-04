import torch
import torch.nn as nn
import torch.optim as optim

class SimpleFFNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleFFNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

torch.manual_seed(42)
X = torch.randn(100, 4)
y = torch.randint(0, 2, (100,)).float().unsqueeze(1)

model = SimpleFFNN(input_dim=4, hidden_dim=8, output_dim=1)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.SGD(model.parameters(), lr=0.05)

epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

# THIS LINE IS REQUIRED TO SHOW THE OUTPUT:
print(f"Training completed successfully! Final Loss: {loss.item():.4f}")
