# job_finder.py
import asyncio
from typing import List

class JobFinderAgent:
    def __init__(self, search_tool, logger):
        self.search_tool = search_tool
        self.logger = logger

    async def find(self, query: str, max_results=10) -> List[dict]:
        """Use search tool to discover job postings. Returns list of job dicts."""
        self.logger.info(f"JobFinder: searching for {query}")
        results = await self.search_tool.search(query, max_results=max_results)
        # results: list of dict {'title','company','location','apply_link','description'}
        return results
