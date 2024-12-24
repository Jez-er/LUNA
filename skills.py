import os
import webbrowser


def text_comparison(trigger, input_str):
    return trigger in input_str


def open_file(command, input_str: str = "", maker=None):
    if os.path.isfile(command['parameters']):
        absolute_path = os.path.abspath(command['parameters'])
        os.startfile(absolute_path)
        print(f"Start file отработал")
    else:
        print(f'Start file не отработал, файл {command["parameters"]} не найден')


def _close_file(command, input_str: str = "", maker=None):
    pass


def open_site(command, input_str: str = "", maker=None):
    webbrowser.open(command['parameters'])
    print("Open site сработал")


def _hotkey(command, input_str: str = "", maker=None):
    pass


def _hotkey_combination(command, input_str: str = "", maker=None):
    pass


def google_request(command, input_str: str = "", maker=None):
    input_str = input_str
    for trigger in command["triggers"]:
        if text_comparison(trigger, input_str):
            input_str = input_str.replace(trigger, "").strip()

    webbrowser.open(
        f"https://www.google.com/search?q={input_str}&sca_esv=72d33d3480545cc7&hl=ru&sxsrf=ADLYWIJggtC2jGkH17ztJJaVUq48b1JY-Q%3A1719743068697&ei=XDKBZvqKKpaMxc8PjISJuAc&ved=0ahUKEwj6qNuVjoOHAxUWRvEDHQxCAncQ4dUDCBA&uact=5&oq={input_str}&gs_lp=Egxnd3Mtd2l6LXNlcnAiBHRlc3QyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAuGIAEMggQLhiABBjUAjIFEAAYgAQyBRAAGIAESIItUPgFWNcncAR4AZABAJgBvAGgAcAFqgEDNi4xuAEDyAEA-AEBmAILoALsBagCCsICChAAGLADGNYEGEfCAgwQABiABBhDGIoFGArCAgsQLhiABBjRAxjHAcICChAjGIAEGCcYigXCAgcQIxgnGOoCwgIQEC4YgAQY0QMYQxjHARiKBZgDBIgGAZAGB5IHAzkuMqAHy0Q&sclient=gws-wiz-serp")
    print('Google request отработал')


def _cmd(command, input_str: str = "", maker=None):
    pass


def _keyboard_write(command, input_str: str = "", maker=None):
    pass


def chat_gpt_request(command, input_str: str = "", maker=None):
    client = OpenAI(
        organization='org-am1j9WgEuy1yF6ji50rzOjmK',
        project='proj_J2lg1urzJKbxBRZGiXNrrTZB',
    )
    messages = []

    input_str = input_str
    for trigger in command["triggers"]:
        if text_comparison(trigger, input_str):
            input_str = input_str.replace(trigger, "").strip()

    messages.append({'role': 'user', 'content': input_str})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    reply = response['choices'][0]['message']['content']

    new_voice.speaker(reply)
    print(reply)



def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
