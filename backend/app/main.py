"""Sahi backend - FastAPI giriş noktası."""

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Sahi API",
    description="Yapay zeka ile üretilen içerikleri tespit eden servis.",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    """Servisin ayakta olup olmadığını kontrol etmek için basit uç nokta."""
    return {"status": "ok"}
