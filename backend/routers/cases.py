from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import CaseCreate, Case, DocumentCreate, Document
from backend.models import Case as CaseModel, Document as DocumentModel
from backend.services import cases_service

router = APIRouter(prefix="/api/cases", tags=["Cases"])

@router.post("/", response_model=Case, status_code=status.HTTP_201_CREATED)
async def create_case(case: CaseCreate, db: Session = Depends(get_db)):
    return await cases_service.create_case(case, db)

@router.get("/{case_id}", response_model=Case)
async def get_case(case_id: int, db: Session = Depends(get_db)):
    return await cases_service.get_case(case_id, db)

@router.post("/{case_id}/documents", response_model=Document, status_code=status.HTTP_201_CREATED)
async def create_document(case_id: int, document: DocumentCreate, db: Session = Depends(get_db)):
    return await cases_service.create_document(case_id, document, db)
