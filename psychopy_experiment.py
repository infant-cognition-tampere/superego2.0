from psychopy import visual, core, event
import feedparser
import random
import os

# parameters
res = [1024,768];
rounds = 4;
stimulus_display_time = 5;
waittime = 0.5; #s
#rss_url = "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss"
rss_url = "http://www.iltalehti.fi/rss/rss.xml";
imagedir = "images";


# get rss-information
feed = feedparser.parse(rss_url)

distraction_texts = [];
for item in feed["items"]:
    distraction_texts.append(item["title"])

# get image information
images = os.listdir(imagedir);

#create a window
win = visual.Window(res, monitor="testMonitor", units="norm")

#create stimuli
fixation = visual.GratingStim(win=win, size=0.02, pos=[0,0], sf=0, rgb=-1)
#image1 = visual.ImageStim(win=win, image="test.jpg")



print("Try to avoid distraction.")
for i in range(0, rounds):
    print("round " + str(i))
    x = 0;
    y = 0;

    # place for the new off-stimulus
    while (0.3 > abs(x) or 0.3 > abs(y)):
        x = random.random()*1.6 -0.8;
        y = random.random()*1.4 -0.7;

    #image1.pos = (x,y)
    #image1.size = 0.5
    #image1.draw()
    fixation.draw()
 
    if random.random()<0.5 and len(images) >0:
        random.shuffle(images);
        img = visual.ImageStim(win=win, image=os.path.join(imagedir, images[0]), pos=(x,y), size= 0.4)
        img.draw()
    else:
        random.shuffle(distraction_texts);
        v = visual.TextStim(win, distraction_texts[0], pos=(x, y), height=0.05)
        v.wrapWidth = 0.7;
        v.draw()
        
    win.flip()

    core.wait(stimulus_display_time)
    win.flip()
    
    # wait for sometime
    core.wait(waittime);

    # check for keypresses
    if len(event.getKeys())>0:
        break
    event.clearEvents()





#cleanup
win.close()
core.quit()
