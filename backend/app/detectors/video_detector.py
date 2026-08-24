"""Video içerikler için yapay zeka üretimi tespit modülü.

Planlanan yaklaşım:
- Kare bazlı görsel analiz (image_detector ile aynı mantık, örneklenen karelerde)
- Kareler arası zamansal tutarlılık (temporal consistency) incelemesi
"""

from __future__ import annotations


def detect(video_bytes: bytes) -> dict:
    """Bir videonun yapay zeka ile üretilmiş olma olasılığını döndürür.

    Args:
        video_bytes: Yüklenen videonun ham bayt verisi.

    Returns:
        dict: {"is_ai_generated": bool, "confidence": float, "label": str}
    """
    # TODO: Kare örnekleme + zamansal tutarlılık analizini burada uygula.
    return {
        "is_ai_generated": False,
        "confidence": 0.0,
        "label": "belirsiz (model henüz eğitilmedi)",
    }
