# tracker.py
from datetime import datetime

class TrackerAgent:
    def __init__(self, memory, logger):
        self.memory = memory
        self.logger = logger
        self.entries = []

    def record(self, job, result):
        entry = {
            "title": job.get('title'),
            "company": job.get('company'),
            "link": job.get('apply_link'),
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.entries.append(entry)
        # also persist to memory
        self.memory.save_application(entry)
        self.logger.info(f"Recorded application for {entry['company']}")

    def summary(self):
        return {"count": len(self.entries), "entries": self.entries}
