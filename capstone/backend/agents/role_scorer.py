# role_scorer.py
class RoleScorerAgent:
    def __init__(self, logger):
        self.logger = logger

    async def score_jobs(self, jobs, user_profile):
        scored = []
        for job in jobs:
            score = self._basic_score(job, user_profile)
            job['score'] = score
            scored.append(job)
        scored.sort(key=lambda j: j['score'], reverse=True)
        self.logger.info(f"Scored {len(jobs)} jobs")
        return scored

    def _basic_score(self, job, user_profile):
        # naive keyword overlap scoring
        job_text = (job.get('title','') + ' ' + job.get('description','')).lower()
        skills = [s.lower() for s in user_profile.get('skills',[])]
        match = sum(1 for s in skills if s in job_text)
        return match * 10  # scale up
