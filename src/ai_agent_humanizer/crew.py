from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()


llm = LLM(
    model="gpt-4",  # или gpt-3.5-turbo
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.5
)


@CrewBase
class AiHumanizer():
    """AiHumanizer crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def text_humanizer(self) -> Agent:
        return Agent(
            config=self.agents_config['text_humanizer'],
            llm=llm, 
            verbose=True
        )

    @task
    def humanizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['humanizer_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiHumanizer crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
