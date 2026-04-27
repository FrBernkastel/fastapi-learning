class VisitCounter:
    def __init__(self):
        self._counts = {"visit": 0}

    def increment(self, key="visit"):
        self._counts[key] = self._counts.get(key, 0) + 1
        return self._counts[key]

    def get(self, key="visit"):
        return self._counts.get(key, 0)
