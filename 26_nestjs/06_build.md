### Build & Deploy

- npm run build

- npm run start:prod

npm i cross-env
npm i pm2 - ec2 server 안꺼지게

"start": cross-env NODE_ENV=production PORT=90 nest start

안되면 sudo 붙이기
