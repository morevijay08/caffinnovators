from fastapi import APIRouter, HTTPException
from app.schemas.career_assistant import AssistantRequest, AssistantResponse
from app.services.gemma_assistant import ask_gemma, ModelInvalidResponse, ModelTimeout, ModelUnavailable

router = APIRouter(prefix="/api/v1/career-assistant", tags=["career assistant"])

@router.post("", response_model=AssistantResponse)
async def career_assistant(request: AssistantRequest):
    try:
        return await ask_gemma(
            request.message,
            [item.model_dump() for item in request.conversation_history],
        )
    except ModelTimeout as exc:
        raise HTTPException(status_code=504, detail="The local Gemma assistant took too long to respond. Check that Ollama and the model are running, then try again.") from exc
    except ModelUnavailable as exc:
        raise HTTPException(status_code=503, detail="The local Gemma assistant is unavailable. Start Ollama and verify the configured model.") from exc
    except ModelInvalidResponse as exc:
        raise HTTPException(status_code=502, detail="The career assistant returned an incomplete reply. Please try again.") from exc
