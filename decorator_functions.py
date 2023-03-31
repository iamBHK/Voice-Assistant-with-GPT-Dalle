from properties import *


def talk(asked):
    machine.say(asked)
    machine.runAndWait()

def stop():
    talk('Alright! Please press power button to turn me on again. Bye bye')
    exit(0)

def isha(take2):
    def execute_inside_isha():
        command = take2()
        talk("Please give me a moment to pull it up")
        cmd_user_id = 2168
        user_device = 1562
        cmd_date = datetime.datetime.now()
        cmd_frame = '%s^%s' %(cmd_user_id,user_device)
        command = command.lower()
        with open("jjsonGPT.json", "r+") as jsonfile:
            get_jsonfile = json.load(jsonfile)
            GPT_json = {
                "user_id" : cmd_frame,
                "command_date" : cmd_date,
                "asked_cmd" : command
            }
            get_jsonfile["data"].append(GPT_json)
            jsonfile.seek(0)
            
        directory = os.path.dirname("AllAudio/")
        machine.save_to_file(command, directory+"/2168.mp3")

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

        else:
            response = openai.Image.create(
            prompt= command,
            n=1,
            size="1024x1024"
            )
            image_url = response['data'][0]['url']
            print(image_url)
            talk('Image generated, click on url to view')
    return execute_inside_isha

def input_cmd(take1):
    def execute_inside_inp_cmd():
        act_command = take1()
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
        
        else:
            isha()
    return execute_inside_inp_cmd

@isha
@input_cmd
def activator():
    print("Listening...")

    try:
        with speech.Microphone() as source:
            s_to_t = listener.listen(source)
            act_command = listener.recognize_google(s_to_t)
            return act_command

    except:
        print("Error while listening initial stage.")

while True:
    activator()