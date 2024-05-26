import os 
import requests 
from dotenv import load_dotenv 

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    '''scrape information from linkedin profiles. manually scrape the info from linkedin profile '''
    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/Varsha-Narla/e0f032f572b25d35a79feed35cf69d28/raw/5096b8ac20edfe057ab555ac804e0143f2a45782/eden-marco.json"
        response=requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint="https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic={"Authorization":f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response=requests.get(
            api_endpoint,
            params={"url":linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    
    data=response.json()
    #below is the code for removing empty fields :
    data={
        k: v
        for k,v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


if __name__=='__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",mock=True
        )
    )



__all__ = ['scrape_linkedin_profile']
