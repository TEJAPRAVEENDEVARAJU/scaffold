class MemoryBank:
    def __init__(self):
        self.applications = []
        self.profiles = {}

    def save_application(self, entry):
        self.applications.append(entry)

    def get_applications(self):
        return self.applications

    def save_profile(self, user_id, profile):
        self.profiles[user_id] = profile

    def get_profile(self, user_id):
        return self.profiles.get(user_id, {})
