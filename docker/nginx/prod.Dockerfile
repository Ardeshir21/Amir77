# Dockerfile_prod.nginx

# Start from the official Nginx image
FROM nginx:1.27.2

# Copy custom Nginx configuration file to the container
COPY ./docker/nginx/default_prod.conf /etc/nginx/conf.d/default.conf
