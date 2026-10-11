from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "ak_x4hivs5roanffcwa9mi40lpg"

EMAIL = "24f2002795@ds.study.iitm.ac.in"

@app.post("/analytics")
async def analytics(request: Request):

    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await request.json()
    events = data.get("events", [])

    user_totals = defaultdict(float)
    unique_users = set()
    revenue = 0.0

    for event in events:
        user = event["user"]
        amount = float(event["amount"])

        unique_users.add(user)

        if amount > 0:
            revenue += amount
            user_totals[user] += amount

    top_user = max(user_totals, key=user_totals.get) if user_totals else None

    return {
        "email": "24f2002795@ds.study.iitm.ac.in",
        "total_events": len(events),
        "unique_users": len(unique_users),
        "revenue": round(revenue, 2),
        "top_user": top_user
    }
