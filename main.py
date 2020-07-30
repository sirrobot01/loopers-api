from fastapi import FastAPI, status, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
from loopers import loop

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://loopers.biodun.dev",
    "https://loopers.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/', status_code=status.HTTP_200_OK)
async def view(link: str):
    try:
        links = loop(link)
        return responses.JSONResponse(links, status_code=status.HTTP_200_OK)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid url {link}')
