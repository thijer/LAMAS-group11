# Getting Started

## Project setup

```
# yarn
yarn

# npm
npm install

# pnpm
pnpm install
```

### Compiles and hot-reloads for development

```
# yarn
yarn dev

# npm
npm run dev

# pnpm
pnpm dev
```

### Compiles and minifies for production

Running this will empty the docs folder and write the new build to deploy.

```
# yarn
yarn build --emptyOutDir

# npm
npm run build

# pnpm
pnpm build --emptyOutDir
```

## How to make changes

Changes are made on /src directory. Content.vue file inside the /src/components folder has all the content from the report.
[Vuetify](https://vuetifyjs.com/en/introduction/why-vuetify/) is used as component library and [Vue3](https://vuejs.org/) as framework.

## Build
CI/CD is not configured yet, so manual build is necesarry to update the github site. You need to run the build command ```npm run build``` inside the site folder, or run ```npm run build --prefix site``` if you are on the root repo folder. Then commit the changes and push.
