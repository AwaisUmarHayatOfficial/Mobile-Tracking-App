# Use Ubuntu-based Apache2 image
FROM ubuntu/apache2:2.4-20.04_beta

# Set working directory to Apache's web root
WORKDIR /var/www/html

# Remove default files (optional)
RUN rm -rf /var/www/html/*

# Copy your website files into Apache root
COPY ./html/ .

# Expose port 80
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2-foreground"]
