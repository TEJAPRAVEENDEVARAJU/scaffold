from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from agents.orchestrator import AutoApplyOrchestrator
from memory.memory_bank import MemoryBank
from tools.search_tool import SearchTool
from tools.browser_tool import BrowserTool
from observability.logger import logger

app = FastAPI(title="AutoApply API")

# global demo memory & tools (single-user demo)
memory = MemoryBank()
tools = {
    "search": SearchTool(),
    "browser": BrowserTool()
}
orchestrator = AutoApplyOrchestrator(memory=memory, tools=tools, logger=logger)

class ApplyRequest(BaseModel):
    query: str
    user_profile: dict
    max_results: int = 10

@app.post("/run")
async def run_apply(req: ApplyRequest, background_tasks: BackgroundTasks):
    """Kick off orchestration in background for demo (returns job tracking summary)"""
    # start in background to simulate long-running loop; also return immediate ack
    background_tasks.add_task(orchestrator.run_pipeline, req.query, req.user_profile, req.max_results)
    return {"status": "started", "query": req.query}

@app.get("/status")
async def status():
    return orchestrator.tracker.summary()
