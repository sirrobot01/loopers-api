from fastapi import FastAPI, status, HTTPException, responses
from loopers import loop

app = FastAPI()


@app.post('/', status_code=status.HTTP_200_OK)
async def view(link: str):
    try:
        links = loop(link)
        return responses.JSONResponse(links, status_code=status.HTTP_200_OK)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid url {link}')
