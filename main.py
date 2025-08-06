from crewai import LLM
import os 
import argparse
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from eda_agent import  EDAAnalysisTool ,EDAInput
from crewai_tools import DirectoryReadTool, FileWriterTool, FileReadTool
from datetime import datetime
load_dotenv()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run EDA using CrewAI")
    parser.add_argument("--folder", required=True, help="Path to the folder containing CSV files")
    args = parser.parse_args()

    folder_path = args.folder
    llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key= os.getenv("GOOGLE_API_KEY")
    )

    # eda_agent = get_eda_agent(llm)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    eda_tool_instance = EDAAnalysisTool()
    eda_agent = Agent(
        name="eda_agent",
        role="Senior EDA & Data Quality Analyst",
        goal="Perform full EDA on CSVs and generate actionable cleaning suggestions. Don't give generic suggestion.Suggestion must be file specific.Give suggestion in 10 points dont return tool responce to output use it for your understanding.Try to use simple english anyone can understand. If multiple files then prepare report accordingly.",
        backstory="You help data analysts by automating EDA and providing tailored, data-quality recommendations.",
        tools=[eda_tool_instance , DirectoryReadTool('resources/drafts'),
                FileWriterTool(),
                FileReadTool()],
        llm=llm,
        verbose=True
    )

    eda_task = Task(
        description = "Perform full EDA on CSV files in the target folder and produce data-quality suggestions.",
        agent = eda_agent,
        args={"folder_path": folder_path},
        expected_output = f"Consise summary of analysis. Report must be save in 'reports/' folder in markdown format. File name should be report_{timestamp}.md "

    )
    crew = Crew(
    agents=[eda_agent],
    tasks=[eda_task],
    verbose=True
)
    crew.kickoff()