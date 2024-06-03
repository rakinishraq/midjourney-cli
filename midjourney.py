import config
import requests
from time import sleep
import webbrowser
 
verbose = print 

def is_valid_url(url):
    if not url: return False
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        if verbose: print(f"Invalid URL: {url}. Error: {e}")
        return False


headers = {"X-API-KEY": config.API_KEY}
# ADD WEBHOOK AND BOT_ID HANDLING HERE
def goapi(endpoint, **kwargs):
    url = "https://api.midjourneyapi.xyz/mj/v2/"+endpoint
    verbose(url, kwargs)

    response = requests.post(url, headers=headers, json=kwargs)
    json = response.json()
    verbose(response.status_code, json)
    return json


def imagine(prompt, aspect_ratio="1:1", process_mode="fast",
            cref=[], cw=100, sref=[], sw=100,
            bot_id=None, skip_prompt_check=False):
    """
    prompt (str): The prompt for image processing
    aspect_ratio (str): Aspect ratio of the image (relax/fast/turbo)
    process_mode (str): Which mode to use for processing
    cref (list): List of character references
    cw (int): Overall weight of character references
    sref (list): List of style references (can be list of tuples with weights)
    sw (int): Overall weight of style references
    bot_id (str): Force task processing on specific Discord account
    """

    if sref:
        sref_strings = ['--sref']
        for r in sref:
            if isinstance(r, tuple):
                sref_strings.append(f"{r[0]}:{r[1]}")
            else:
                sref_strings.append(r)
        if sw: sref_strings.extend(('--sw', str(sw)))
        prompt += ' ' + ' '.join(sref_strings)
    
    if cref:
        prompt += ' --cref ' + ' '.join(cref)
        if cw: prompt += ' --cw ' + cw

    out = goapi("imagine", prompt=prompt,
                aspect_ratio=aspect_ratio,
                process_mode=process_mode)
    id = out["task_id"]
    if not id: return out


def main():
    imagine("test")


if __name__ == "__main__":
    main()