import sys, os, discord
from piazza_api import Piazza
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pprint import pprint

ZERO_WHITE_SPACE = "\u200b"

def piazza_parse(pi_url, EMAIL, PASSWD):
    '''
    Called by connect.py to get post from Piazza.
    It will format the post json into a more readable message for server.
    '''

    # Create Piazza object, login, and get the users classes
    data = {}
    p = Piazza()
    p.user_login(email=EMAIL, password=PASSWD)
    classes = p.get_user_classes()

    # Parse the piazza url into components
    piazza_url = urlparse(pi_url)

    # Get class id and the post number from piazza_url
    class_id = piazza_url.path.split('/')[2]
    post_num = piazza_url.query.split('=')[1]
    
    # Returns a class network
    class_net = p.network(class_id)

    # Get the piazza post from the post number and class network
    post = class_net.get_post(post_num)

    # Get class name
    class_name = "None"
    for i in classes:
        if i['nid'] == class_id:
            class_name = i['num']

    # Get question and subject of the post
    question = post["history"][0]["content"]
    subject = post["history"][0]["subject"]

    # Format data to return
    data.setdefault("class_name", class_name)
    if not data['class_name']:
        data['class_name'] = ZERO_WHITE_SPACE
    data.setdefault("question", subject)
    if not data['question']:
        data['question'] = ZERO_WHITE_SPACE
    # data.setdefault("subject", subject)
    data.setdefault("question_text", BeautifulSoup(question, features='lxml').text)
    if not data['question_text']:
        data['question_text'] = ZERO_WHITE_SPACE
    if not data['question_text']:
        data['question'] = ZERO_WHITE_SPACE
    data.setdefault("answer", {'instructor': '', 'student': ''})
    
    
    # Get answers json
    answers = post["children"]

    # Assign student and instructor answers if they exist
    for answer in answers:
        if answer['type'] == 's_answer':
            data['answer']['student'] = BeautifulSoup(answer['history'][0]['content'], features='lxml').text
        elif answer['type'] == 'i_answer':
            data['answer']['instructor'] = BeautifulSoup(answer['history'][0]['content'], features='lxml').text

    return embed_creator(data, pi_url)

def embed_creator(data, pi_url):
    embed=discord.Embed(title=data['class_name'], url=pi_url, color=0x00fffb)
    embed.add_field(name=data['question'], value=data['question_text'], inline=False)
    if data['answer']['student']:
        embed.add_field(name="Student Answer", value=data['answer']['student'], inline=True)
    if data['answer']['instructor']:
        embed.add_field(name="Instructor Answer", value=data['answer']['instructor'], inline=True)
    embed.set_footer(text=pi_url)
    return embed