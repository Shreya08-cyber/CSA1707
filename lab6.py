class VacuumCleaner:
    def __init__(self, location, status):
        self.location = location  # 'A' or 'B'
        self.status = status      # Dictionary storing room statuses

    def act(self):
        print(f"Current Location: {self.location} | Status: {self.status}")
        if self.status[self.location] == 'Dirty':
            print(f"-> Location {self.location} is Dirty. Cleaning...")
            self.status[self.location] = 'Clean'
        else:
            print(f"-> Location {self.location} is Clean. Moving to the other room...")
            self.location = 'B' if self.location == 'A' else 'A'

# Run simulation
vacuum = VacuumCleaner('A', {'A': 'Dirty', 'B': 'Dirty'})
for i in range(4):
    print(f"\n--- Step {i+1} ---")
    vacuum.act()
