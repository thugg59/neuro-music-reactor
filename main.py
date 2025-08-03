from player.controller import play_music_based_on_wave
import random
import time

waves = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']

def main():
    print("🧠 Simulating EEG-to-artist mapping...\n")
    while True:
        wave = random.choice(waves)
        print(f"Detected wave: {wave}")
        play_music_based_on_wave(wave)
        time.sleep(1)

if __name__ == "__main__":
    main()

