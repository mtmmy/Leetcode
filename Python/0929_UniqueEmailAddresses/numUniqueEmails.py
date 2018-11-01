class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        domains = {}
        
        def normalizeLocal(name):
            name = name.replace(".", "")
            plusIdx = name.find("+")
            if plusIdx > -1:
                return name[:plusIdx]
            return name
                
        
        for email in emails:
            local, domain = email.split("@")
            local = normalizeLocal(local)
            
            if domain not in domains:
                domains[domain] = set()
            domains[domain].add(local)
        
        return sum([len(s) for s in domains.values() ])
                