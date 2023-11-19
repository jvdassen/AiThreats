docker rm -f api-threatfinder
docker run -d --restart unless-stopped \
      	   --name api-threatfinder \
	   -p 8080:8080 \
	   -v "$PWD":/app python:3 \
	   /bin/bash -c '/app/entry.sh'
