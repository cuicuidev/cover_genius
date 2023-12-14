from fastapi.routing import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def root_user():
	check = {
		"route": "/user",
		"status": "OK",
		"message": "This is the user route"
	}
	return check
