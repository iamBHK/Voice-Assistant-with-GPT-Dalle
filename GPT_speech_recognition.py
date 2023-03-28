from properties import *


def talk(asked):
    machine.say(asked)
    machine.runAndWait()

# Runs from input_cmd function. Always runs when the file is executed.
def activator():
    print("Listening...")
    
    try:
        with speech.Microphone() as source:
            s_to_t = listener.listen(source)
            act_command = listener.recognize_google(s_to_t)
            return act_command
                     
    except:
        pass

# This listen actual question and feed forward to isha function. Also works for stop execution function.
def input_cmd():
    act_command = activator()
    act_command = act_command.lower()
    if 'isha' in act_command:
        print("Hellow, how can I help you")
        talk("Hellow, how can I help you")
        
        try:
            with speech.Microphone() as source:
                s_to_t = listener.listen(source)
                command = listener.recognize_google(s_to_t)
                return command
                
        except:
            pass
    elif 'stop isha' in act_command:
        stop()
    # If no isha in the command, will restart the program by isha()
    else:
        isha()

def isha():    
    command = input_cmd()
    talk("Please give me a moment to pull it up")
    # Just to categorize while analyzing data, you can make this dynamic.
    cmd_user_id = 2168
    user_device = 1562
    cmd_date = datetime.datetime.now()
    cmd_frame = '%s^%s' %(cmd_user_id,user_device)
    command = command.lower()
    # Stores command in json format
    with open("jjsonGPT.json", "r+") as jsonfile:
        get_jsonfile = json.load(jsonfile)
        GPT_json = {
            "user_id" : cmd_frame,
            "command_date" : cmd_date,
            "asked_cmd" : command
        }
        get_jsonfile["data"].append(GPT_json)
        jsonfile.seek(0)
        # Stores the command as mp3 file after saving onto json format.
    directory = os.path.dirname("AllAudio/")
    machine.save_to_file(command, directory+"/2168.mp3")
    
    # Only on GPT (language model) execution. But, logically it might not work sometimes.
    if 'generate image' not in command:
        build = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [{
                "role" : "user",
                "content" : command
            }]
        )
        answer = build['choices'][0]['message']['content']
        print(answer)
        talk(answer)

    elif 'stop isha' in command:
        stop()
# Generates the image using dale
    else:
        response = openai.Image.create(
        prompt= command,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(image_url)
        talk('Image generated, click on url to view')
        
        
# Stop the assistant execution
def stop():
    talk('Alright! Please press power button to turn me on again. Bye bye')
    exit(0)

# Initially runs this command
while True:
    isha()