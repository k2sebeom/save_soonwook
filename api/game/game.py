from fastapi import APIRouter
from pydantic import BaseModel

from core.gpt import give_soonwook

game_router = APIRouter(prefix='/game')


class GameReq(BaseModel):
    item: str

class GameResp(BaseModel):
    response: str


@game_router.post("/")
async def think(req: GameReq) -> GameResp:
    resp = give_soonwook(req.item)
    return GameResp(response=resp)
