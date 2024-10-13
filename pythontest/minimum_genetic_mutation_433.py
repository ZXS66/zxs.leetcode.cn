# https://leetcode.cn/problems/minimum-genetic-mutation/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0
        geneLib = set(bank)
        if endGene not in geneLib:
            return -1
        mutations = "ACGT"
        queue = deque([(startGene, 0)])
        while queue:
            gene, mutate = queue.popleft()
            for i in range(len(gene)):
                for m in mutations:
                    new_gene = gene[:i] + m + gene[i + 1 :]
                    if new_gene != gene and new_gene in geneLib:
                        if new_gene == endGene:
                            return mutate + 1
                        geneLib.remove(new_gene)
                        queue.append((new_gene, mutate + 1))
        return -1
