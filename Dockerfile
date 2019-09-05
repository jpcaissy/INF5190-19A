FROM nginx:mainline-alpine
COPY vendor  /usr/share/nginx/html/vendor/
COPY cours  /usr/share/nginx/html/cours/
COPY index.html  /usr/share/nginx/html/
