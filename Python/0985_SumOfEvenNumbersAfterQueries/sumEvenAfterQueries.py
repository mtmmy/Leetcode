class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        result, evenSum = [], sum([num for num in A if num % 2 == 0])
        
        for q in queries:
            if A[q[1]] % 2 == 0:
                evenSum -= A[q[1]]
            A[q[1]] += q[0]
            if A[q[1]] % 2 == 0:
                evenSum += A[q[1]]
            result.append(evenSum)
        
        return result