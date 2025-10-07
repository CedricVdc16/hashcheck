    # --- build+test stage ---
    FROM python:3.12-slim AS build
    WORKDIR /app
    COPY app /app/app
    COPY tests /app/tests
    RUN pip install --no-cache-dir pytest
    # lancer les tests
    RUN pytest -q

    # --- runtime stage ---
    FROM python:3.12-slim
    WORKDIR /app
    COPY app /app/app
    # durcissement basique: utilisateur non-root
    RUN useradd -m -u 10001 -s /usr/sbin/nologin appuser && \
chown -R appuser:appuser /app
    USER appuser
    ENTRYPOINT ["python","-m","app.hashcheck"]
