from polls import fetch_polls
from fastapi import FastAPI, Query

polls = fetch_polls()

app = FastAPI(
    title="Polish Polls API"
)

@app.get("/")
def get_all():
    return polls

@app.get("/parties/{party_name}")
async def party(party_name: str, amount: int = Query(5, title="amount", description="Amount of latest polls")):
    output = {}
    results = polls.head(amount).loc[:, party_name]
    output['results'] = results
    output['mean'] = round(results.mean(),2)
    return(output)