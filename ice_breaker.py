from agents.tools.tools import get_profile_url_tavily
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from scripts.third_parties.linkedin import scrape_linkedin_profile
from scripts.third_parties.twitter import scrape_user_tweets
from langchain.prompts.prompt import PromptTemplate 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)  # this will be a URL
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username)

    summary_template = """
    Given the following information about a person from LinkedIn and {information} and their latest twitter posts {twitter_posts}: 
    I want you to create :
    1. A short summary 
    2. Two interesting facts about them 

    Use both information from linkedin and twitter
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})
    print(res)

if __name__ == "__main__":
    load_dotenv()
    print("Ice breaker enter")
    ice_break_with(name="Eden Marco")
