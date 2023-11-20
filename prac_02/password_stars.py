def main():
    num_scores = int(input("Enter the number of scores to generate: "))
    scores = generate_random_scores(num_scores)
    write_results_to_file(scores)
    print(f"{num_scores} scores and their results have been written to results.txt")

    # Printing specific scores
    print("Printing specific scores:")
    specific_scores = [66, 4, 92, 51]
    for score in specific_scores:
        status = determine_score_status(score)
        print(f"{score} is {status}")
