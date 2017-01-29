#!/opt/python3/bin/python3
"""
THIS IS METER PETER, NAMED AFTER THE GREAT METASPLOIT PAYLOAD METERPRETER. HE WAS BORN A MAN AHEAD OF HIS TIME. WITHOUT A MOTHER, YOUNG METER TURNED TO HIS FATHER FOR ADVICE. HIS FATHER SAID, "BE FREE SON".
"""
import discord
import asyncio
import random
import re
import requests
import os
import sys
import psutil
import logging


client = discord.Client()

jokez = ['my life',
	'god (dyme) left me unfinished',
	'sarah only dates matt out of sympathy',
	'feminism!!!!',
	'childish gambino',
	'macklemore',
	'white privilege 2: the greatest hip hop album of our generation',
	'i love g easy!!']

jones = ["What a bunch of garbage, liberal, Democratic, conservative, Republican, it's all there to control you, two sides of the same coin! Two management teams, bidding for control of the CEO job of Slavery Incorporated!",
    "People say, 'The government couldn't carry out the September 11th attack, it's too big, they'd get caught!' They DID get caught! They're just counting on you to be dumb and to go along with it.",
    "I don't give a damn what queers do, and don't give a damn what Christians do. Just get the hell out of my way because I want to live my life and I don't want the government sucking 60\% of my wages off my ass.",
    "I mean there are a bunch of people who I’ve heard worship Adolf Hitler who don’t like me because I don’t think Jews have 14 inch fangs and drink blood and sneak around in bushes.",
    "The answer to 1984 is 1776.",
    "When John Kennedy attempted to take the government back from the back from the robber barons, he was brutally murdered. The message to future US president and leaders across the world was clear: do as you're told, or die. John Fitzgerald Kennedy was the last true president of the United States. And until the globalists are removed from power, we will never have another real one.",
    "The New World Order is a more palatable name for the Anglo American world empire. It's the planetary domination of London, New York, Washington over the rest of the world. It's hard to get people to join that or think they have a part in it if you called it the Anglo American world empire. If you call it the New World Order, then people in India or some place like that or the European Union might think, \"Well, there's something there for us too.\" But that's not what it is; it's the Anglo American New World Order.",
    "Within 2 years Im predicting...that youre going to see a suitcase nuke in this country. Youre probably going to see a release in a few years of something communicable. & I am predicting that you will see a lot of conventional bombings...in the next year or so.",
    "A lot of people are waking up to human history, but so many people have been conditioned by the government controlled media to think that it's cool not to care.",
    "The average person is either a weakling, or just a happy person who wants to get along, or thinks being tough is having big muscles and strutting around town and having a good-looking girlfriend.",
    "It's a different kind of economic recovery. The kind where bankers steal trillions and you don't have a job.",
    "There are people who are avaricious parasites. There are psychotic geniuses in control of this planet, and to them human beings are only a commodity to be bought and sold and traded.",
    "Hollywood is owned by the Arabs.",
    "If humanity has any hope of effecting real change for the better, it will not come from the Madison Avenue false reality makers who've cast Barack Obama as the savior of the world. To alter our course from tyranny to liberty, to defeat the corrupt elite, we must get past the puppets and confront the real power structure of the planet.",
    "In a dictatorship there is no choice, the elections are controlled, the police are the military, fear equals control, speech is suppressed, the economy is looted, the people are slaves.",
    "It’s…it’s easy to have some little bitty website and use a fake name and sit there and…you know…talk bad about Jews all day and enjoy yourselves…uh, you know…getting your kicks ’cause you live in, you know…a…a one room apartment and your mad at life or whatever and wanna blame us…you know.",
    "And the Arabs are the biggest owners now of media in the United States, okay, and over stock exchanges. And in many major U.S. cities they’re the majority owners.",
    "The Hubbell space telescope, it's first year up after they fixed it, categorized and counted 500 billion galaxies in any one photograph field of view of dark matter. That's like grains of sand at the beach and you've just got a handful. It's massive amounts. I'm sure that of all of the galaxies, and I'm sure the universe is teeming with life.",
    "Damn it, if just 5\% of people got motivated in some direction, and it doesn't necessarily have to be what I believe in, but if they just got motivated and stopped getting their political ideologies from the mainstream media, they would go out and figure out what they want.",
    "I do a real analysis of who actually owns things - it’s the British…the Dutch…then it’s the Arabs…then it’s the French…then it’s the Jews…and then, on down the line.",
    "We have, without any fanfare or much conversation, moved into a era in which news organizations are expected to explain themselves. Twenty years ago, it would not be expected that the New York Times would explain itself. The concept of what accountability.",
    "People want everything to come out of a drive thru window. They want it instant and they want it fast. I succumb to that, we all succumb to that. We're in it. That's the culture. So the enemy, the powers that be, the manipulators behind the scenes play to our natural weaknesses.",
    "You don't know who's good or bad until you get to that crisis point.",
    "And I certainly don’t like the white supremacists and those whose religion is hating the Jews, period.",
    "Every time we look, they're killing Jews.",
    "I know this, the Federal Reserve is private and the I.R.S. is screwing us.",
    "Some people say they're gathering DNA. Perhaps they're gathering it for the future when the human race is stronger or weaker, who knows. That's science fiction and mere speculation.",
    "Most people in the media aren't bad people. They just go along to get along and it's the group culture and the conditioning. As soon as they see that things are wrong, some of them will start speaking out and making a stand.",
    "People are used to being stimulated. People are drunk on entertainment and when you're going out and seeing movies where 200 people are machine gunned down and vampires are tearing people's throats out, and I'm not saying that is bad or it should be censored, but people are drunk on stimuli.",
    "I'm not saying that people shouldn't go out to football games and drink beer and have a good time, I do it myself. But, at the same time, people are so apathetic and that shows me that they don't care about themselves. They have no self-image. Their image is projected to them via the television and that is where they make decisions about who they are according to what the public says they ought to be.",
    "The Jew haters and white supremacists…all they do is fight with each other all day too.",
    "The economy is a ponzi scheme. People are working harder than they ever have for less wages, but we have so many bobbles because manufacturing has come up so quickly over the past hundred years that people have the illusion of wealth.",
    "Criminality is now legal. I guess criminal racketeering these days would be like burning little children at the stake or something. That's about what it takes to get anyone to care.",
    "And everybody’s running around talking about ‘Zionists’ all day. Okay, just keep parroting that over and over again.",
    "They’re good people. I have a lot of Jewish friends.",
    "And I got a lot of friends in Hollywood.",
    "These powerbrokers, which bomb innocent countries and slaughter people, and, you know, pump the food chain full of garbage and just everything else they do, it's probably something fun for them. They really get off on being bad little boys.",
    "Why? Why are they always wanting to kill Jews?",
    "The majority of world stock markets are now owned by the Arabs."]

banned = ['gay']

help_me = """```-------- *Meter Peter Developmental Build* --------

Available commands:
    !play [video url] - play youtube, soundcloud, pornhub video
    !stop             - stop video playback
    !joke             - tell a funny joke (ha ha)
    !porn             - list top porn vids
    !malevitality     - print alex jones quote
    !asciifart        - take an ascii fart
    !attack           - kill all humans```"""

asciifart = """
            ---,_,----                                    
           /    .     \                                   
          /     |      \                                  
         (      @@      )       SO ANYWAY DO I GET THE JOB
         /   _/----\_   \                                 
        /   '/      \`   \                                
       /    /   .    \    \                               
      /    /|        |\    \                              
      /   / |        | \   \                              
     /   /`_/_      _\_'\   \                             
    /  '/  (  . )( .  )  \  `\                            
    <_ ' `--`___'`___'--' ` _>                            
   /  '     @ @/ =\@ @     `  \                           
  /  /      @@(  , )@@      \  \                          
 /  /       @@| o o|@@       \  \                         
' /          @@@@@@@@          \ ` LWR                    """


def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        """
        if p.get_open_files():
            for handler in p.get_open_files() + p.connections():
                os.close(handler.fd)
        """
    except Exception as e:
        logging.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for channel in client.get_all_channels():
        if channel.name == "This Voice Channel Is":
            global vchan
            vchan = channel
    #voice = await client.join_voice_channel(vchan)
    #stream = await voice.create_ytdl_player('https://www.youtube.com/watch?v=tufeOCd2M94')
    #stream.start()
    #print(vchan)
    #for whatever in voice:
    #    print(whatever.is_connected())

@client.event
async def on_message(message):
    global voice
    global stream
    if str(message.author) not in banned:
        if message.content.startswith('!test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        elif message.content.startswith('!joke'):
            await client.send_message(message.channel, jokez[random.randint(0, len(jokez)-1)])
        elif message.content.startswith('!malevitality'):
            await client.send_message(message.channel, jones[random.randint(0, len(jones)-1)])
        elif message.content.startswith('!play'):
            url = message.content[6:]
            print('im gonna cry')
            try:
                if client.is_voice_connected(vchan.server) == True:
                    stream.stop()
                    await voice.disconnect()
                #global voice
                voice = await client.join_voice_channel(vchan)
                #global stream
                stream = await voice.create_ytdl_player(url)
                stream.start()
                print(stream)
            except:
                await client.send_message(message.channel, 'pls lrn2use (!help)')
                await voice.disconnect()
                #restart_program()
        elif message.content.startswith('!porn'):
            page = requests.get('http://www.pornhub.com/video?o=ht&cc=us').content
            result = re.findall('title="(.*?)"', str(page), re.DOTALL)
            final = []
            for title in result:
                if len(title) > 10 and title not in final and "&amp" not in title:
                    final.append(title)
            print(final)
            await client.send_message(message.channel, 'Today\'s hottest videos on pornhub:')
            string = ""
            for title in final:
                string += title
                string += "\n"
            #print(string)
            await client.send_message(message.channel, string)
        elif message.content.startswith('!stop'):
            print(stream)
            stream.stop()
            await voice.disconnect()
        elif message.content.startswith('!attack'):
            print(client.is_voice_connected(vchan.server))
            if client.is_voice_connected(vchan.server) == True:
                stream.stop()
                await voice.disconnect()
            voice = await client.join_voice_channel(vchan)
            player = voice.create_ffmpeg_player('/home/nancy/speech.wav')
            try:
                player.start()
                #player.stop()
                #print("HOLLY")
                #await voice.disconnect()
                #print("WHATTT")
                #logf = open("m.log", "w")
                #logf.write("Count: %s\n" % str(2))
                #logf.close()
                #count = 0
                
                while player.is_playing() == True:
                    pass
                player.stop()
                await voice.disconnect()
            except Exception as e:
                print("WOAH")
                os.system("id > /tmp/fff")
        elif message.content.startswith('!help'):
            await client.send_message(message.channel, help_me)
        elif message.content.startswith('!asciifart'):
            #f = asciifart.replace("'", "'")
            f = "```%s```" % asciifart
            print(f)
            await client.send_message(message.channel, f)
        elif message.content.startswith('!ban'):
            if str(message.author) == "DYME#3994":
                user = message.content[5:]
                banned.append(user)
                await client.send_message(message.channel, '%s NO SOUP FOR U (lol jerry)' % user)
            else:
                await client.send_message(message.channel, 'you arent daddy!!!!!')
        elif message.content.startswith('!unban'):
            if str(message.author) == "DYME#3994":
                user = message.content[7:]
                banned.remove(user)
                await client.send_message(message.channel, '%s ok hav sum soup' % user)
            else:
                await client.send_message(message.channel, 'you\'re not my dad!!!!!')
        elif message.content.startswith('!sleep'):
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')
        if str(message.author) == "DYME#3994" and message.content.lower() == "hi son i love you":
            await client.send_message(message.channel, 'daddy!')
        if str(message.author) == "DYME#3994" and message.content.lower() == "!restart":
            await client.send_message(message.channel, 'meter peter RELOADING!!!!')
            restart_program()
    else:
        if message.content.startswith('!'):
            await client.send_message(message.channel, 'ha ha fuck you')

client.run('MjQ2ODI0ODA0ODIzMzM0OTE0.CwgRGg.d04CjryRYZ6bw_ub1shd_v93pwo')
