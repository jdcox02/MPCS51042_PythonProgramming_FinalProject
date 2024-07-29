from hashtable import Hashtable
import math

HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2


class Markov:
    def __init__(self, k, text, use_hashtable):
        """
        Construct a new k-order markov model using the text 'text'.
        """
        self.k = k
        self.text = text
        self.use_hashtable = use_hashtable
        if self.use_hashtable:
            self.known_text = Hashtable(HASH_CELLS, 0, TOO_FULL, GROWTH_RATIO)
        else:
            self.known_text = dict()

        # Using get_slice generator to identify k and k+1 slices and add their counts to the known_text hashtable
        for k_slice, kplus1_slice in zip(
            self._get_slice(text, k), self._get_slice(self.text, k + 1)
        ):
            try:
                self.known_text[k_slice] += 1
            except KeyError:
                self.known_text[k_slice] = 1
            try:
                self.known_text[kplus1_slice] += 1
            except KeyError:
                self.known_text[kplus1_slice] = 1

    def _get_slice(self, str, k):
        """Returns all slices of size k using the wraparound technique described in the final project"""
        str = str + str[: k - 1]
        while len(str) >= k:
            yield str[:k]
            str = str[1:]

    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        """
        # Get k+1 slices in the unknown text
        unknown_text_slices = [x for x in self._get_slice(s, self.k + 1)]

        prob_sum = 0

        # Iterate overall k+1 slices from the unknown text
        for slice in unknown_text_slices:
            # In this case, slices is the k+1 slice, so we will rename it to kplus1_slice
            kplus1_slice = slice

            # If we remove one character from slice, we have the k slice. We will rename it to k_slice
            k_slice = slice[0:-1]

            # Obtain the number of times that the kplus1_slice from the unknown text is seen in the known text and set m equal to this value
            try:
                m = self.known_text[kplus1_slice]

            # If kplus1_slice is not found in the known text, set m equal to 0.
            except KeyError:
                m = 0

            # Obtain the number of times that k_slice from the unknown text is seen in the known text and set n equal to this value
            try:
                n = self.known_text[k_slice]

            # If k_slice is not found in the known text, set n equal to 0.
            except KeyError:
                n = 0
            # Obtain the number of unique characters in the known_text
            unique_chars = len(set(self.text))

            # Use the formula provided in the initial assignment to add up the probabilities for each k, k+1 slice
            prob_sum += math.log((m + 1) / (n + unique_chars))

        # Return the sum of the probabilities
        return prob_sum


def identify_speaker(speech1, speech2, speech3, k, use_hashtable):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "order" order
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    """
    # Obtain the Markov model for speaker A
    speaker1 = Markov(k, speech1, use_hashtable)

    # Obtain the Markov model for speaker B
    speaker2 = Markov(k, speech2, use_hashtable)

    # Use the Markov model for speaker A to get the probability that the speaker in speech3 is speaker A
    speaker1_prob = speaker1.log_probability(speech3) / len(speech3)

    # Use the Markov model for speaker B to get the probability that the speaker in speech3 is speaker B
    speaker2_prob = speaker2.log_probability(speech3) / len(speech3)

    # Compare the results to determine whether speaker A or B is more likely to be the speaker in speech3
    if speaker1_prob > speaker2_prob:
        result = "A"
    elif speaker2_prob > speaker1_prob:
        result = "B"
    # Note in the unlikely case that speaker A and speaker B have the same probability, we will indicate that the result is a tie.
    else:
        result = "TIE"

    # Return a tuple - the first item indicates the probability that speaker A is the speaker in speech3, the second item indicates the probability that speaker B is the speaker in speech3, and the third item indicates the speaker that was most likely to be the speaker (A or B)
    return (speaker1_prob, speaker2_prob, result)


if __name__ == "__main__":
    pass
