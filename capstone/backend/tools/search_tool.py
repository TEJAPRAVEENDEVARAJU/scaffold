# search_tool.py
import asyncio
class SearchTool:
    def __init__(self):
        pass

    async def search(self, query, max_results=10):
        # Demo stub: return mocked results
        await asyncio.sleep(0.5)
        results = []
        for i in range(max_results):
            results.append({
                "title": f"{query} - Role {i+1}",
                "company": f"Company {i+1}",
                "location": "Remote",
                "apply_link": f"https://example.com/apply/{i+1}",
                "description": f"Looking for {query} with experience in React, JS, HTML. Role {i+1}."
            })
        return results
