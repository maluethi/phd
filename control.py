

import time
import re
import datetime
import plotly.graph_objs as go

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check_score(old_score):
    pass

def Play():
    driver.get('http://www.cl.cam.ac.uk/~yf261/2048/')
    body = driver.find_element_by_tag_name('body')
    t0 = datetime.datetime.now()
    score = 0
    delay = 0
    while True:
        old_score = score

        try:
            rel = driver.find_element_by_xpath('.//span[@class = "rel"]')
        except:
            delay = 0
        else:
            try:
                if rel.text == "Relationship":
                    delay = 0.5
                else:
                    delay = 0
            except:
                pass


        time.sleep(delay)
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(delay)
        body.send_keys(Keys.ARROW_LEFT)
        time.sleep(delay)
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(delay)
        body.send_keys(Keys.ARROW_RIGHT)


        for elem in driver.find_elements_by_class_name("score-container"):
            try:
                score = int(elem.text)
            except:
                continue

        if old_score - score >= 0:
            delta = datetime.datetime.now() - t0
            if delta.seconds > 11:
                body.send_keys(Keys.ARROW_UP)
        else:
            t0 = datetime.datetime.now()

        try:
            driver.find_element_by_link_text("Try again")
        except:
            pass
        else:
            print "End"
            return score


driver = webdriver.Chrome("/home/matthias/bin/chromedriver/chromedriver")

scores = []

# encoding: utf-8

import plotly.plotly as py
import plotly.graph_objs as py_gr
import plotly.tools as py_tls



maxpoints = 10000
streamit = False

stream =[]


if streamit:
    stream_id = "" # Put your own token

    trace1 = py_gr.Scatter(
            x=[],
            y=[],
            xaxis=dict(title="Game"),
            yaxis=dict(title="Score"),
            mode='line',
            name="Game",
            stream=py_gr.Stream(
                token=stream_id,
                maxpoints=maxpoints
            )
    )

    data = go.Data([trace1])
    layout = go.Layout(title='Martins stupid PhD algorithm')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, auto_open=False)

    stream = py.Stream(stream_id)
    stream.open()



for game in range(maxpoints):
    print("game:", game)

    scores.append(Play())
    print(scores[-1])
    if streamit:
        stream.write(
                dict(
                    x=game,
                    y=scores[-1]
                )
        )

if streamit:
    stream.close()
print(scores)

