import multiprocessing
from itertools import combinations

def lcs_pairwise(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[len1][len2]

def lcs_worker(seq_pair):
    return lcs_pairwise(seq_pair[0], seq_pair[1])

def TA_1997(sequences):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    sequence_pairs = list(combinations(sequences, 2))
    lcs_lengths = pool.map(lcs_worker, sequence_pairs)
    
    pool.close()
    pool.join()

    return max(lcs_lengths)

