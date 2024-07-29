import sys
from markov import identify_speaker

if __name__ == "__main__":
    """This main method receives system arguments for filenameA, filenameB, filenameC, an integer value k, and whether the user would like the program to use a 'hashtable' or 'dict'. It then prints to the console the probability that speaker A (from filename A) and speaker B (from filenameB) is speaker C(from filenameC). It also provides a conclusion indicating whether speaker A or speaker B is most likely. The variable k indicates the length of strings that should be considered. The variable hashtable_or_dict indicates whether the program should use a hashtable or dictionary."""
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <k> <hashtable-or-dict>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, k, hashtable_or_dict = sys.argv[1:]
    k = int(k)
    if hashtable_or_dict not in ("hashtable", "dict"):
        print("Final parameter must either be 'hashtable' or 'dict'")
        sys.exit(1)

    # Reading in speaker text files
    with open(filenameA) as speakerA:
        speakerA = speakerA.read()
    with open(filenameB) as speakerB:
        speakerB = speakerB.read()
    with open(filenameC) as speakerC:
        speakerC = speakerC.read()

    # Create new variable, use_hashtable, that uses hashtable_or_dict to indicate whether a hashtable should be used
    if hashtable_or_dict == "hashtable":
        use_hashtable = True
    else:
        use_hashtable = False

    # Getting results from identify_speaker prediction
    speakerA_result, speakerB_result, conclusion = identify_speaker(
        speakerA, speakerB, speakerC, k, use_hashtable
    )

    # Printing the result
    print(
        f"Speaker A: {speakerA_result}\nSpeaker B:{speakerB_result}\n\nConclusion: Speaker {conclusion} is most likely"
    )
