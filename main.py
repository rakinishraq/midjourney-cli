import os
import requests
import traceback
from pprint import pprint
from time import sleep
import webbrowser
 
headers = {"X-API-KEY": "70a1326d270e3d2d21a62ade6cbd128bb201a74322436caf77e812ac2ea74ec1"}
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


lina = "https://i.postimg.cc/PJV0ys2M/1.png https://i.postimg.cc/hPhkjvtZ/2.png https://i.postimg.cc/15TLNSgm/3.png https://i.postimg.cc/Cxq9G2Dj/4.png https://i.postimg.cc/7LrdmNMj/5.png https://i.postimg.cc/mr3qqFmk/6.png"
portrait = [
    "https://i.postimg.cc/FFCjwyMv/image.jpg",
    "https://i.postimg.cc/026pv6vw/image.jpg", 
    "https://i.postimg.cc/ncwFBkXX/PXL-20240306-192129675-PORTRAIT.jpg",
    "https://i.postimg.cc/FHd9ZLSD/PXL-20240306-192157928-PORTRAIT.jpg",
    "https://i.postimg.cc/bw7qFwH8/PXL-20240306-192211125-PORTRAIT.jpg",
    "https://i.postimg.cc/Prw48YVn/image.jpg"
][:2]
alt = [[ # https://postimg.cc/gallery/ZTdXhpS/98cad494
    "https://i.postimg.cc/HLPdJr8S/0.png", 
	"https://i.postimg.cc/Ss2qcmWm/1.png", 
	"https://i.postimg.cc/50hJ3D3L/2.png", 
	"https://i.postimg.cc/Y0BcgYrx/3.png", 
	"https://i.postimg.cc/RVz9n5qz/4.png", 
	"https://i.postimg.cc/NFRcPbJV/5.png", 
	"https://i.postimg.cc/QN7htx8b/6.png", 
	"https://i.postimg.cc/3x8TnXgS/7.png", 
	"https://i.postimg.cc/zDTYNt72/8.png", 
	"https://i.postimg.cc/65LKrjG4/9.png"
	"https://i.postimg.cc/sgTR8MmV/10.png", 
	"https://i.postimg.cc/Gp911bgv/11.png", 
	"https://i.postimg.cc/BbTrCbtf/12.png", 
	"https://i.postimg.cc/bN8cwxFy/13.png", 
	"https://i.postimg.cc/1tqhfJQt/14.png", 
	"https://i.postimg.cc/cJjGxPP2/15.png", 
][i] for i in [1, 12, 10, 14, 11]]
"""
#prompt = lina+" short ponytail hair, young woman, dynamic action poses, full body, indian, black ninja outfit, pretty, cute, full body --niji 6 --sref https://i.postimg.cc/W4k7dRBk/image.png --sw 500"
#prompt = "silver hair, woman, character sheet, full body, multiple poses and expressions, black ninja outfit, cute asian, relaxed, pretty eyes, simple cartoon style --niji 6 --seed 1715235611"
#prompt = "https://i.pinimg.com/originals/1b/18/81/1b1881af32921a38e29d96bbb50747ef.jpg" + " beautiful anime girl, bright red hair, digital painting pastel colors, portrait, pretty --niji 6"
#prompt = "https://i.postimg.cc/pVm8HscF/image.jpg" + " beautiful anime girl, dark red hair, black streetwear outfit, portrait, pretty --niji 6"
#prompt = " ".join(alt) + " short ponytail hair, young woman, dynamic action poses, full body, black ninja outfit, pretty, cute --niji 6"
#prompt = "https://i.postimg.cc/sXps0Wz6/the-birth-of-a-legend-cropped.png mercenary woman, pink hair, streetwear, holding gun, next to car, city background, fog, manga style lineart, vibrant --niji 6"
#pprint(generate(prompt))
#print(generate("https://i.postimg.cc/gjFvb4CV/image.jpg monochrome, smiling man, masculine, strong jawline, portrait, attractive, handsome --sref https://i.postimg.cc/JhrXqfRB/dq8k50cb67b11.jpg --sw 300"))
#print(goapi("mj/v2/upscale", origin_task_id="62f7926d-b770-4398-a0ab-1ccbb0f55f05", index="3"))
#print(goapi("mj/v2/upscale", origin_task_id="62f7926d-b770-4398-a0ab-1ccbb0f55f05", index="4"))
#print(goapi("mj/v2/variation", origin_task_id="62f7926d-b770-4398-a0ab-1ccbb0f55f05", index="4"))
#print(goapi("mj/v2/upscale", origin_task_id="0cf50ff8-6e3c-43fc-a35b-4ffea7c12aeb", index="1"))
#print(goapi("mj/v2/seed", task_id="0cf50ff8-6e3c-43fc-a35b-4ffea7c12aeb"))
#print(goapi("mj/v2/fetch", task_id="0cf50ff8-6e3c-43fc-a35b-4ffea7c12aeb"))
#track("9d1ac625-a0c9-4f83-8133-68bff6fe28a7")
#scan_ids()

