# UniEnquiry 

A university admission enquiry chatbox system for assissting international students with application procedures by allowing them to interact with a chatbot that gives them responses about admission requirements, cost requirements, aid information, universities abroad etc.

## Prerequisites

Make sure you have the following before beginning:

```bash
python3-dev
git
pip
virtualenv
npm
```

## Getting the api key from College Score Card API

The actual open-source data can be found on the Department of Education's API documentation page at https://collegescorecard.ed.gov/data/documentation/ where users and developers alike can register for their own API key at this link: https://api.data.gov/signup/. The API key will be emailed to the email you provided once you complete the sign up.

Once you have the API key, navigate to the file `path/to/your/directory/uni_admission_chatbox_app/university_admission_chatbox_project_backend/chatbox/chat.py` and edit line 28 by replacing the field `your_api_key` with the generated API key. (This will be modified later on to allow easy entry of the API key)

## Setting up the projects dependencies (backend)

Navigate into the projects directory from the terminal.
```bash
$ cd path/to/your/directory/uni_admission_chatbox_app/university_admission_chatbox_project_backend
```
Create a virtual environment for your project
```bash
$ python3 -m venv name-of-your-virtualenv
```
Activate your virtual environment.
```bash
$ source name-of-your-virtualenv/bin/activate
```
Install the requirements.
```bash
(name-of-your-virtualenv)$ pip3 install -r requirements.txt
```

## Running the project (backend)

Make database migrations:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

To train the data:
```bash
$ python manage.py shell

- Run this in the shell:

>>> from chatbox import train

- You should see the following output (the epoch loss score may vary):

```
epoch 100/1000, loss=0.7308
epoch 200/1000, loss=0.0857
epoch 300/1000, loss=0.0177
epoch 400/1000, loss=0.0059
epoch 500/1000, loss=0.0014
epoch 600/1000, loss=0.0023
epoch 700/1000, loss=0.0013
epoch 800/1000, loss=0.0007
epoch 900/1000, loss=0.0004
epoch 1000/1000, loss=0.0008
final loss, loss=0.0008
Training complete. File saved to data.pth
```

-  Exit the shell by pressing Ctrl+D
```

To run the project:
```bash
(name-of-your-virtualenv)$ python manage.py runserver 

# the information below will be displayed if everything is okay
Performing system checks...

System check identified no issues (0 silenced).
January 18, 2020 - 18:55:56
Django version 3.0, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Setting up the projects dependencies (frontend)

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```bash

npm install

```

### Compile and Hot-Reload for Development (runs the frontend)

```bash

npm run dev

# the information below will be displayed if everything is okay:

> university_admission_chatbox_project_frontend@0.0.0 dev
> vite


  VITE v4.4.4  ready in 6063 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help


```
Navigate to:
- http://localhost:5173/signup - To create an account.
- http://localhost:5173/login - To log into your account
- http://localhost:5173/- Home Page
- http://localhost:5173/chat - To interact with the chatbot



