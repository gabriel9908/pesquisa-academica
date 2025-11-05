from fastapi import FastAPI
import os

app = FastAPI(title="Pesquisa Acadêmica - API (MVP)")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/env")
async def env():
    # exemplo leve para checar vars no dev (remova em prod)
    return {
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "MINIO_ENDPOINT": os.environ.get("MINIO_ENDPOINT"),
    }
