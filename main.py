from fastapi import FastAPI
from fastapi import Request

app= FastAPI(
    title="SWIGGY ORDER SERVICE",
    description=(
        "Internal API for managing orders"
        "Handle creation, tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint- Health check"""
    #FastAPI converts this dict into JSON
    return {"message": "Welcome to swiggy order service",
            "status":"healthy"}

@app.get("/about")
def about():
    """Return API metadata"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "ap-south-1",
        "version": "1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders": [
            {"id":1 , "item":"Butter Chicken", "status": "delivered"},
            {"id":2 , "item":"kadai Chicken", "status": "preparing"},
            {"id":3 , "item":"tandoori Chicken", "status": "delivered"},
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "total_today": 2_340_23,
        "top-city": "Bengluru"
    }

@app.get("/debug/request-info")
async def request_info(request:Request):
    """Inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "querry_params": dict(request.query_params)
    }

@app.get(
    "/orders/active",
    summary="Get Acitve Orders",
    description=(
        "Return all orders that are currently being prepared"
        "or are out for delivery"
    ),
    #tag: groups the request together
    tags=["orders"],
    response_description="List of active objects",
    deprecated=False
)
def get_active_order():
    """This docstring also appears in docs"""
    return{
        "active_orders":[
            {"id":1, "item":"Masala Dosa",
             "status":"out_for_delivery"}
        ]
    }

@app.get("/restaurants", tags=["Restaurants"])
def list_rest():
    """another docstring  for another endpoint"""
    return {
        "restaurants":[
            {"test": "test"}
        ]
    }