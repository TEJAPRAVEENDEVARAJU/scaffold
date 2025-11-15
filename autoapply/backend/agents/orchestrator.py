import asyncio
from .job_finder import JobFinderAgent
from .role_scorer import RoleScorerAgent
from .personalization import PersonalizationAgent
from .form_filler import FormFillerAgent
from .tracker import TrackerAgent

class AutoApplyOrchestrator:
    def __init__(self, memory, tools, logger):
        self.memory = memory
        self.tools = tools
        self.logger = logger
        self.job_finder = JobFinderAgent(self.tools['search'], logger)
        self.scorer = RoleScorerAgent(logger)
        self.personalizer = PersonalizationAgent(memory, logger)
        self.form_filler = FormFillerAgent(self.tools['browser'], logger)
        self.tracker = TrackerAgent(memory, logger)
        self.user_profile = None

    async def run_pipeline(self, query, user_profile, max_results=10):
        self.user_profile = user_profile
        self.logger.info(f"Starting pipeline for query={query}")
        jobs = await self.job_finder.find(query, max_results)
        scored = await self.scorer.score_jobs(jobs, user_profile)
        top = scored[: min(len(scored), 5)]
        tasks = []
        for job in top:
            tasks.append(self._handle_job(job))
        await asyncio.gather(*tasks)
        self.logger.info("Pipeline finished")
        return self.tracker.summary()

    async def _handle_job(self, job):
        cv_text, cover_letter = self.personalizer.generate_documents(job, self.user_profile)
        result = await self.form_filler.attempt_apply(job, cv_text, cover_letter)
        self.tracker.record(job, result)
