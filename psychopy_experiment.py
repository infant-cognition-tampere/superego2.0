from psychopy import visual, core, event
import feedparser
import random


# parameters
res = [1024,768];
rounds = 4;
stimulus_display_time = 5;
waittime = 0.5; #s
#rss_url = "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss"
rss_url = "http://www.iltalehti.fi/rss/rss.xml";

# get rss-information
feed = feedparser.parse(rss_url)

distraction_texts = [];
for item in feed["items"]:
    distraction_texts.append(item["title"])

#create a window
win = visual.Window(res, monitor="testMonitor", units="norm")

#create stimuli
fixation = visual.GratingStim(win=win, size=0.02, pos=[0,0], sf=0, rgb=-1)
#image1 = visual.ImageStim(win=win, image="test.jpg")


random.shuffle(distraction_texts);

print("Try to avoid distraction.")
for i in range(0, rounds):
    print("round " + str(i))
    x = 0;
    y = 0;

    # place for the new off-stimulus
    while (0.3 > abs(x) or 0.3 > abs(y)):
        x = random.random()*1.8 -0.9;
        y = random.random()*1.4 -0.7;

    #image1.pos = (x,y)
    #image1.size = 0.5
    #image1.draw()
    fixation.draw()
    v = visual.TextStim(win, distraction_texts[i], pos=(x, y), height=0.05)
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
