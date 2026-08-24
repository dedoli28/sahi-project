"""API uç noktaları: görsel/video/ses analiz istekleri buradan yönlendirilir."""

from fastapi import APIRouter, UploadFile

from app.detectors import audio_detector, image_detector, video_detector

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/image")
async def analyze_image(file: UploadFile):
    """Yüklenen görselin yapay zeka ile üretilip üretilmediğini tespit eder."""
    contents = await file.read()
    result = image_detector.detect(contents)
    return result


@router.post("/video")
async def analyze_video(file: UploadFile):
    """Yüklenen videonun yapay zeka ile üretilip üretilmediğini tespit eder."""
    contents = await file.read()
    result = video_detector.detect(contents)
    return result


@router.post("/audio")
async def analyze_audio(file: UploadFile):
    """Yüklenen sesin yapay zeka ile üretilip üretilmediğini tespit eder."""
    contents = await file.read()
    result = audio_detector.detect(contents)
    return result
