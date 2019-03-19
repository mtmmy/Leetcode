import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        domainHash = collections.defaultdict(int)
        
        for record in cpdomains:
            times, domain = record.split(" ")
            times = int(times)
            domainHash[domain] += times
            for i in range(len(domain)):
                if domain[i] == ".":
                    domainHash[domain[i + 1:]] += times
        
        return ["{} {}".format(val, key) for key, val in domainHash.items()]