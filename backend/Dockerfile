# 1. PHP 8.2 with Apache
FROM php:8.2-apache

# 2. Install essential system dependencies
RUN apt-get update && apt-get install -y \
    libpng-dev \
    zip \
    unzip \
    git \
    && docker-php-ext-install pdo_mysql

RUN a2enmod rewrite

# 4. Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# 5. Set working directory
WORKDIR /var/www/html

# 6. Create fresh Laravel project
RUN composer create-project laravel/laravel .

RUN cp .env.example .env && \
    sed -i 's/DB_CONNECTION=mysql/DB_CONNECTION=sqlite/g' .env && \
    sed -i 's|DB_DATABASE=laravel|DB_DATABASE=/var/www/html/database/database.sqlite|g' .env && \
    mkdir -p /var/www/html/database && \
    touch /var/www/html/database/database.sqlite

RUN sed -i 's|/var/www/html|/var/www/html/public|g' /etc/apache2/sites-available/000-default.conf

RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 775 /var/www/html/storage /var/www/html/bootstrap/cache /var/www/html/database

# 10. Generate Laravel Application Key
RUN php artisan key:generate

EXPOSE 80

# Apache automatically starts in this image, so no CMD needed
