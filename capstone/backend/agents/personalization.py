# personalization.py
class PersonalizationAgent:
    def __init__(self, memory_bank, logger):
        self.memory = memory_bank
        self.logger = logger

    def generate_documents(self, job_post, user_profile):
        """
        Create tailored CV bullets and a cover letter.
        In production: call LLM (Gemini) with a prompt containing user_profile + job_post.
        Here: we create a simple templated output.
        """
        title = job_post.get('title','')
        company = job_post.get('company','')
        # quick templated cover letter
        cover_letter = f"Dear {company} hiring team,\n\nI am excited to apply for the {title} role. " \
                       f"My background in {' ,'.join(user_profile.get('skills',[]))} suits this position.\n\nRegards,\n{user_profile.get('name')}"
        # CV variant: pick top 3 skills into bullets
        skills = user_profile.get('skills',[])[:5]
        cv_bullets = [f"- Experience with {s}" for s in skills]
        cv_text = f"{user_profile.get('name')}\n\n" + "\n".join(cv_bullets)
        self.logger.info(f"Generated docs for {title} at {company}")
        return cv_text, cover_letter
