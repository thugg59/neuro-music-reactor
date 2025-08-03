import random
import time

def generate_mock_brainwave():
    """Simulates a brainwave state every second."""
    states = ['Calm', 'Focused', 'Stressed', 'Sleepy']
    while True:
        state = random.choice(states)
        yield state
        time.sleep(1)

if __name__ == "__main__":
    for signal in generate_mock_brainwave():
        print(f"Simulated brain state: {signal}")
