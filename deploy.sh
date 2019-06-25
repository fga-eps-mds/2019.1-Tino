docker stop $(docker ps -a -q) &&  docker login -u jppgomes -p 250595 && docker pull jppgomes/jp:latest && docker pull jppgomes/telegram-jp:latest && docker-compose up -d
