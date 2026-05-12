FROM nginx:alpine as builder
RUN echo "Construyendo sitio..." > /usr/share/nginx/html/index.html

FROM nginx:alpine
COPY --from=builder /usr/share/nginx/html/index.html /usr/share/nginx/html/index.html
EXPOSE 80