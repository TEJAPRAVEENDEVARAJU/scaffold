# browser_tool.py
class BrowserTool:
    def __init__(self):
        pass

    async def fill_form(self, url, data):
        # In production, use Playwright to open url, fill and attach files
        return {"status":"ok", "message":"filled (demo)", "url": url}
