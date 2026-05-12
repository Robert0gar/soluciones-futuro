FROM nginx:alpine

RUN echo '<html><body style="background-color: #f4f4f4; font-family: Arial;"> \
          <h1>Soluciones Tecnologicas del Futuro</h1> \
          <p>Estado del Despliegue: <span style="color: green;">EXITOSO</span></p> \
          <p>Version: 1.0 (DevOps Automated)</p> \
          </body></html>' > /usr/share/nginx/html/index.html

EXPOSE 80