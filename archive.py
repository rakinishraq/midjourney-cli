from PIL import Image
import os
import traceback
from pprint import pprint
import io
import piexif
import json

def generate(prompt):
    init_print = False
    output = goapi("imagine", prompt=prompt, aspect_ratio="4:3", process_mode="fast")
    id = output["task_id"]

    if not id: return output

    status = "started"
    print("loading: https://img.midjourneyapi.xyz/mj/%s.png" % id)
    
    while status != "finished":
        output = goapi("fetch", task_id=id)
        status = output["status"]
        if not init_print:
            print(output)
            init_print = True

        if status == "failed": return
        
        if status == "finished":
            id = goapi("seed", task_id=id)["task_id"]
            init_print = False
            status = "pending"

            while status in ["pending", "processing"]:
                output = goapi("fetch", task_id=id)
                status = output["status"]
                if not init_print:
                    print(output)
                    init_print = True
                sleep(1)
            
            print("done:", url := output["task_result"]["image_url"])
            response = requests.get(url)
            if not os.path.exists("output"):
                os.makedirs("output")
            with open(f'output/{id}.png', 'wb') as f:
                f.write(response.content)
            with open(f'output/{id}.json', 'w') as f:
                json.dump(output, f, indent=4)

            #webbrowser.open(url)
            return output
        sleep(1)
