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

### Frontend
There is already a project you can build in android studio inside of src/frontend/android. But if you just want to test it, or modify it, follow these steps.
firstly, you will need npm, then run these commands
```bash
npm install
npx cap sync
npx cap build android
```
I dont have an Iphone, so i didnt add an IOS project, but since you can build it for ios using these.
```bash
npx cap add ios
npx cap sync
npx cap build ios
```
After building everything, i'd recommend you to open it in which ever IDE is pertinent and use it to test it. Just use:
```bash
npx cap open [android or ios]
```
From those IDE's you will have an easier time emulating or building apks. If you just want to open it in a browser use 
```bash 
ionic serve
```
