import sys
from markov import identify_speaker
import pandas as pd
import time
import seaborn as sns
import matplotlib as plt

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <max-k> <runs>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, max_k, runs = sys.argv[1:]
    max_k = int(max_k)
    runs = int(runs)

    # Reading in speaker text files
    with open(filenameA) as speakerA:
        speakerA = speakerA.read()
    with open(filenameB) as speakerB:
        speakerB = speakerB.read()
    with open(filenameC) as speakerC:
        speakerC = speakerC.read()

    # Creating dataset
    data = []
    for use_hashtable in ["True", "False"]:
        for k_val in range(1, max_k + 1):
            for run in range(1, runs + 1):

                start = time.perf_counter()
                prob_result = identify_speaker(
                    speakerA, speakerB, speakerC, k_val, use_hashtable
                )
                elapsed = time.perf_counter() - start

                if use_hashtable == "True":
                    hashtable_or_dict = "Hashtable"
                else:
                    hashtable_or_dict = "Dictionary"

                data.append([hashtable_or_dict, k_val, run, elapsed])

    # Creating dataframe
    markov_results = pd.DataFrame(data, columns=["Implementation", "K", "Run", "Time"])
    # Printing the dataframe
    print(markov_results)

    # Creating the plot
    plot = sns.pointplot(
        data=markov_results,
        x="K",
        y="Time",
        hue="Implementation",
        linestyles="-",
        markers="o",
    )
    plot.set_ylabel(f"Average Time (Runs={runs})")
    plot.set_ylim(
        markov_results["Time"].min() - 0.1, markov_results["Time"].max() + 0.1
    )
    plot.set_title("HashTable vs. Python dict")

    # Saving the figure
    fig = plot.get_figure()
    fig.savefig("execution_graph.png")
