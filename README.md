# FlowSpace UI

This is the React UI for [FlowSpace](http://flowspace.bvn.works).

## Getting started

1. Clone the repo
1. run `npm install`
1. make an `.env.local` file, the format is below, you can get the missing values from Ishaan or Ben.
   ```
   NODE_PATH=src
   REACT_APP_API_URL="http://0.0.0.0:5001/v1"
   REACT_APP_FIREBASE_API_KEY="long hex mess"
   REACT_APP_FIREBASE_AUTH_DOMAIN="sensicorn.firebaseapp.com"
   REACT_APP_FIREBASE_DATABASE_URL="https://sensicorn.firebaseio.com"
   REACT_APP_FIREBASE_PROJECT_ID="sensicorn"
   REACT_APP_FIREBASE_STORAGE_BUCKET="sensicorn.appspot.com"
   REACT_APP_FIREBASE_MESSAGING_SENDERID="a number"
   ```
1. run `npm run dev`
1. open `http://localhost:1234/` in your browser
1. profit

### Useful commands:

#### Frequent use

- `npm run dev` builds, watches and runs a server on localhost:1234
- `npm run test` runs all the tests, do this before you push
- `npm run lint` runs the linter, do this before you push

These last two commands are what the CI server runs to verify things, so if they pass on your machine, they should pass on the CI server.

#### Handy

- `npm run test:update` If you've changed a file that has snapshot tests, then you need to run this command, then check in the updated snapshots. That lets the CI server know that the component that it renders is the same as the component that you're rendering locally.
- `npm run test:coverage` Gives you a coverage report. No real target yet for coverage, but one day it'd be nice to get green numbers in the table!
- `npm run test:watch` Runs the tests continuously on save, has some smart presets that keep things fast (e.g. runs the last failing test first).
- `npm run format` Runs prettier across the repo. This is mostly for people who use VIM because prettier runs in the browser for most people. (wierdos).
- `npm run build` builds the app, but doesn't serve it.

## launch.json for debugging tests in VS code

```
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Jest All",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": ["--runInBand"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "disableOptimisticBPs": true,
      "windows": {
        "program": "${workspaceFolder}/node_modules/jest/bin/jest"
      }
    },
    {
      "type": "node",
      "request": "launch",
      "name": "Jest Current File",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": ["${fileBasenameNoExtension}", "--config", "jest.config.js"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "disableOptimisticBPs": true,
      "windows": {
        "program": "${workspaceFolder}/node_modules/jest/bin/jest"
      }
    }
  ]
}
```

## Helpful things to know

- Everything is still very unfinished!
- This project uses prettier to reformat on save
- There are quite a lot of material design react components. [Their docs are here](https://github.com/material-components/material-components-web-react)
- There are some useful VS code plugins that will make your life easier.
  - [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
  - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
