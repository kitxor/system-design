class BackingStore:
    """
    BackingStore for demonstration.
    It should be a Postgres or similar database backed repository layer
    """
    def __init__(self):
        self.data=dict() # using dict as persistent storage

    def get(self, key):
        print(f"** cache miss; fetching {key} from backing store **")
        return self.data.get(key)

    def put(self, key, value):
        self.data[key] = value
