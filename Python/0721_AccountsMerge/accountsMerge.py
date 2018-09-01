import unittest

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def find(s, root):
            return s if root[s] == s else find(root[s], root)

        result = []
        root = {}
        owner = {}
        dic = {}
        for account in accounts:
            for i in range(1, len(account)):
                root[account[i]] = account[i]
                owner[account[i]] = account[0]

        for account in accounts:
            p = find(account[1], root)
            for i in range(2, len(account)):
                q = find(account[i], root)
                root[q] = p

        for account in accounts:
            for i in range(1, len(account)):
                p = find(account[i], root)
                if p in dic:
                    dic[p].add(account[i])
                else:
                    dic[p] = set([account[i]])

        for key, val in dic.items():
            v = list(val)
            v.sort()
            v.insert(0, owner[key])
            result.append(v)

        return result

    def accountsMerge2(self, accounts):
        n = len(accounts)
        acc2per = [-1] * n  # initial:  acc2per[i] = i
        
        def findSet(x):
            if acc2per[x] < 0:
                return x
            acc2per[x] = findSet(acc2per[x])
            return acc2per[x]
        
        def union(x, y):  # union the 2 sets of x & y
            xx = findSet(x)
            yy = findSet(y)
            if xx < yy:
                acc2per[xx] += acc2per[yy]
                acc2per[yy] = xx
            elif yy < xx:
                acc2per[yy] += acc2per[xx]
                acc2per[xx] = yy
        
        # merge accounts to persons
        email2acc = {}
        for acc, emails in enumerate(accounts):
            for i in range(1, len(emails)):
                e = emails[i]
                if e not in email2acc:
                    email2acc[e] = acc
                else:
                    union(acc, email2acc[e])
        
        # collect emails for each person
        per2emails = {}
        for acc, emails in enumerate(accounts):
            per = findSet(acc)
            if per not in per2emails:
                per2emails[per] = set()
            for i in range(1, len(emails)):
                per2emails[per].add(emails[i])
        
        # process each person & corresponding info
        res = []
        for per, emails in per2emails.items():
            info = [accounts[per][0]]  # fetch person name
            info.extend(sorted(list(emails)))
            res.append(info)

        return res

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        test = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        expected = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        self.assertEqual(expected, target.accountsMerge2(test))

if __name__ == '__main__':
    unittest.main()
        