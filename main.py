import midjourney

unis = [[ # https://postimg.cc/gallery/ZTdXhpS/98cad494
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
lina = [[
    "https://i.postimg.cc/PJV0ys2M/1.png",
    "https://i.postimg.cc/hPhkjvtZ/2.png",
    "https://i.postimg.cc/15TLNSgm/3.png",
    "https://i.postimg.cc/Cxq9G2Dj/4.png",
    "https://i.postimg.cc/7LrdmNMj/5.png",
    "https://i.postimg.cc/mr3qqFmk/6.png"
][i] for i in [0, 2, 3, 4, 5]]


persona = [
    "https://i.postimg.cc/43vXPLZz/Joker-Persona-5-600-3993730.jpg::1",
    "https://i.postimg.cc/qvdYwk75/Shin-Megami-Tensei-PERSONA-5-600-2160093.jpg::1",
    "https://i.postimg.cc/P5z7FBpr/913616.png::1",
    "https://i.postimg.cc/NjZGkTc6/4k-version-of-the-official-p3re-art-for-wallpapers-and-such-v0-rs7t7e32oxjb1.webp::1",
	"https://i.postimg.cc/TPmd7wdZ/vrmf7qtu83gc1.jpg::1"
]
wlop = [
    "https://i.postimg.cc/CMv4gNsw/de1yw9w-905ef3c0-5fd6-4aef-9f07-d6e8417fad2c.jpg::1",
	"https://i.postimg.cc/7YfnY2K0/detefg1-b4da83de-3b6e-46ea-8a98-275a7ed7300e.jpg::1"
]
spiderverse = [
    "https://i.postimg.cc/T1YfmtgC/Bert-Spider-Verse.jpg",
	"https://i.postimg.cc/kgkJZFPg/gwen-stacy-spider-gwen-aka-ghost-spider.jpg",
    
]

sref = '--sw 800 --sref ' + ' '.join(spiderverse)
cref = '--cref ' + ' '.join(lina)
print(midjourney.generate(f"anime girl, white hair, ninja outfit, pretty, digital painting, dramatic, dynamic pose {cref} {sref}"))
