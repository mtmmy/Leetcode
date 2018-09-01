class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((id, timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]
        
        return [id for id, timestamp in self.logs if start <= timestamp[:index] <= end]

if __name__ == '__main__':
    target = LogSystem()
    target.put(1,"2017:01:01:23:59:59")
    target.put(2,"2017:01:01:22:59:59")
    target.put(3,"2016:01:30:00:00:00")
    target.put(4,"2016:07:01:00:00:00")
    print(target.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
    print(target.retrieve("2016:12:01:01:01:01","2017:02:01:23:00:00","Month"))
    print(target.retrieve("2016:01:01:01:01:01","2017:12:01:23:00:00","Month"))
    print(target.retrieve("2016:01:01:01:01:01","2017:12:01:23:00:00","Day"))
    print(target.retrieve("2016:01:01:01:01:01","2017:12:01:23:00:00","Day"))