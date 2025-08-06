import os
import json
import google.generativeai as genai
from crewai import Agent
# from crewai_tools import tool
from eda_utils import analyze_csv
from crewai.tools import BaseTool
from pydantic import BaseModel , Field

# @tool("eda_tool_with_suggestions")
class EDAInput(BaseModel):
    folder_path: str = Field(description="Path to the folder containing CSV files")


class EDAAnalysisTool(BaseTool):
    name: str = "EDA Analysis Tool"
    description: str = "Performs full exploratory data analysis on CSV files in a folder and generates suggestions."
    args_schema: type = EDAInput

    def _run(self, folder_path: str) -> str:
        reports = []

        for fname in os.listdir(folder_path):
            if fname.endswith(".csv"):
                path = os.path.join(folder_path, fname)
                result = analyze_csv(path)

                # prompt = (
                #     "You are a senior data analyst assistant.\n"
                #     f"Here is the EDA report:\n{json.dumps(result, indent=2)}\n\n"
                #     "Provide:\n"
                #     "1. Summary of dataset\n"
                #     "2. Specific recommendations, e.g., remove outliers, change datatype, fill nulls.\n"
                #     "Return suggestions as a numbered list."
                # )

                # resp = genai.chat(messages=[{"role": "user", "content": prompt}])
                # result["analysis_summary"] = resp.text
                reports.append(result)

        return json.dumps(reports, indent=2)



if __name__ == "__main__":
    from dotenv import load_dotenv
    import os 
    from crewai.llm import LLM
    load_dotenv()

    llm = LLM(
    
    model="gemini/gemini-2.5-flash",
    temperature=0.1,
    api_key= os.getenv("GOOGLE_API_KEY")
    )   

    tool = EDAAnalysisTool()
    print(tool.run(r"data"))



