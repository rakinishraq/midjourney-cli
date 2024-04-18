import os
import requests
import traceback
from pprint import pprint
from time import sleep
import webbrowser
import config
 
headers = {"X-API-KEY": config.API_KEY}
def goapi(endpoint, verbose=False, **kwargs):
    url = "https://api.midjourneyapi.xyz/mj/v2/"+endpoint
    if verbose: print(url, kwargs)

    response = requests.post(url, headers=headers, json=kwargs)
    json = response.json()
    if verbose: print(response.status_code, json)
    return json


def track(id):
    status = "started"
    print("loading: https://img.midjourneyapi.xyz/mj/%s.png" % id)
    while status != "finished":
        output = goapi("fetch", task_id=id)
        #print(output)
        status = output["status"]
        
        if status == "finished":
            seed_output = goapi("seed", task_id=id)
            id = seed_output["task_id"]
            print(seed_output)

            status = "pending"
            while status in ["pending", "processing"]:
                output = goapi("fetch", task_id=id)
                status = output["status"]
                sleep(1)
            print("done:", url := output["task_result"]["image_url"])
            webbrowser.open(url)
            return output
        sleep(1)


def generate(prompt):
    output = goapi("imagine", prompt=prompt, aspect_ratio="4:3", process_mode="fast")
    id = output["task_id"]
    if not id: print(output)
    else:
        return track(id)


def main():
    pass


if __name__ == "__main__":
    main()

"""
def scan_ids():
    pics = r"D:\Gallery\AI Art Collection\midjourney\api"
    files = []
    for root, directories, filenames in os.walk(pics):
        for filename in filenames:
            id = os.path.join(filename[:-4])
            try:
                output = goapi("mj/v2/fetch", task_id=id)
                prompt, seed = "", ""
                
                try: prompt = output["meta"]["task_request"]["prompt"]
                except:
                    try: prompt = output["meta"]["task_param"]["prompt"]
                    except: pass
                
                try: seed = output["task_result"]["seed"]
                except: pass

                print(id, '[%s]' % seed, prompt)
            except Exception as e:
                seed = output["task_result"]["seed"]
                print(id, '[%s]' % seed)
"""