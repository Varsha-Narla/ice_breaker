from langchain.prompts.prompt import PromptTemplate 
from langchain_openai import ChatOpenAI
from scripts.third_parties.linkedin import scrape_linkedin_profile
from .agents.tools.tools import get_profile_url_tavily

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) ->str:
    linkedin_username=linkedin_lookup_agent(name=name) #this will be a url
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """
    Given the following information about a person:
    {information}
    
    Create the following:
    1. A short summary 
    2. Two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template|llm
    linkedin_data=scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
    )
    res = chain.invoke(input={"information": linkedin_data})
    print(res)

if __name__ == "__main__":
    load_dotenv()
    print("Ice breaker enter")
    ice_break_with(name="Eden Marco")
    
