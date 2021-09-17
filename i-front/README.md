# i-front

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```
Блоки для nginx

	root /w/blue/m/test-front;

    server_name _;

    location / {
        try_files $uri $uri/ /index.html;
    }

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).
