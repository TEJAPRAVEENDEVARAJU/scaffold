class FormFillerAgent:
    def __init__(self, browser_tool, logger):
        self.browser = browser_tool
        self.logger = logger

    async def attempt_apply(self, job_post, cv_text, cover_letter):
        apply_link = job_post.get('apply_link')
        self.logger.info(f"Attempting apply to {apply_link}")
        return {"status":"prepared", "message":"Prepared draft application (demo)", "apply_link":apply_link}
