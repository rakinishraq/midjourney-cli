import config
import requests
from time import sleep
import webbrowser
import json
import os
 
def verbose(*a): return a 
headers = {"X-API-KEY": config.API_KEY}


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

    # Prompt
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

    # Imagine
    out = goapi("imagine", prompt=prompt,
                aspect_ratio=aspect_ratio,
                process_mode=process_mode)
    if not (id := out["task_id"]):
        raise Exception(out)
    status = "started"
    print("imagining:", url := "https://img.midjourneyapi.xyz/mj/%s.png" % id)

    while status != "finished":
        out = goapi("fetch", task_id=id)
        status = out["status"]

        if status == "failed": raise Exception(out)
        elif status == "finished":
            print("imagined")
            try:
                response = requests.get(url)
                with open(f'output/{id}.png', 'wb') as f:
                    f.write(response.content)
                    os.system("feh output/%s.png" % id)
            except Exception as e:
                webbrowser.open(url)
                print("Downloading image failed, opening in browser.")
                print(e)
            with open(f'output/{id}.json', 'w') as f:
                json.dump(out, f, indent=4)        
            break

        sleep(1)
    
    # Seed
    seed_id = goapi("seed", task_id=id)["task_id"]
    status = "pending"

    while status in ["pending", "processing"]:
        out = goapi("fetch", task_id=seed_id)
        status = out["status"]

        if status == "failed": raise Exception(out)
        elif status == "finished":
            with open(f'output/{id}.json', 'w') as f:
                json.dump(out, f, indent=4)
            print("seeded:", out["task_result"]["seed"])
            break

        sleep(1)
    
    return id

def main():
    if not os.path.exists("output"): # TODO: globalize
        os.makedirs("output")
    imagine("artistic, business card, strong typography, eye-catching, minimal, QR code, silver foil")


if __name__ == "__main__":
    main()