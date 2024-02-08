# Fauxbank
An app that simulates an E-banking application, it's only intended as a practice project. It was built using FastAPI, SQLAlchemy, Vue.js, and Ionic + Capacitor.
For more information on the dependencies, check the pipfile or the package.json file.

## Deployment
### Backend
The backend can be deployed straight to vercel from the repository. However you still need to set some enviroment variables.
**SECRET_KEY** will be used to sign your jwt tokens. You can generate one using openssl by running:
```bash
openssl rand -hex 32
```
**ALGO** is the algorithm that is used, i used HS256.
**POSTGRES_URL** is the url to your database. This was meant to use postgresql from the start, hence the name.

the address of the API can be changed in src/store.ts.

### Frontend
There is already a project you can build in android studio inside of src/frontend/android. But if you just want to test it, or modify it, follow these steps.
firstly, you will need npm and the ionic cli, then run these commands
```bash
npx ionic build && npx cap copy
npx vite build
```
Now you can run it in the browser using
```bash
npx ionic serve
```
You can also use the Ionic extension for vscode to do all of this.
