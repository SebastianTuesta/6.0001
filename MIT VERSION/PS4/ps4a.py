# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def join_every_index(s0, sequence):
    """
    s0: an string of lenght 1
    sequence: an arbitrary string or a list of string. Must not be empty.
    
    This function insert s0 in the position 0,1,...len of every string that is part of the list
    or of the string if sequence is a string
    
    """
    
    assert (isinstance(s0, str) and bool(sequence) and 
            all(isinstance(elem, str) for elem in sequence) 
            and len(s0) == 1), "Wrong input"
    
    answer = []

    for seq in sequence:
        n = len(seq)
        for i in range(n+1):
            l1 = seq[0:i] + s0 + seq[i:n]
            answer.append(l1)
        
    return answer
    
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    assert isinstance(sequence,str), "Wrong input"
    
    n = len(sequence)
    
    if n==1:
        return list(sequence)
    else:
        return join_every_index(sequence[0],get_permutations(sequence[1:]))
         
if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
