import random

NUM_QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUMBERS_PER_LINE = 6

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUMBERS_PER_LINE))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

if __name__ == "__main__":
    main()
