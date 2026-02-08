# frontend/Dockerfile
FROM ubuntu/apache2:2.4-20.04_beta

# Remove default files as root
RUN rm -rf /var/www/html/*

# Copy website files as root
COPY ./html/ /var/www/html/

# Create non-root user
#RUN useradd -m WebUI

# Give WebUI ownership of Apache directories
#RUN mkdir -p /var/run/apache2 /var/lock/apache2 \
#    && chown -R WebUI:WebUI /var/www/html /var/run/apache2 /var/lock/apache2

# Switch to non-root
#USER WebUI

WORKDIR /var/www/html
EXPOSE 80

CMD ["apache2-foreground"]
