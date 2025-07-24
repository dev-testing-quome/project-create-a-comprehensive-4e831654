from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.models import Case as CaseModel, Document as DocumentModel
from backend.schemas import CaseCreate, Case, DocumentCreate, Document

async def create_case(case: CaseCreate, db: Session):
    new_case = CaseModel(title=case.title, description=case.description, client_name=case.client_name)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return Case.from_orm(new_case)

async def get_case(case_id: int, db: Session):
    case = db.query(CaseModel).filter(CaseModel.id == case_id).first()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    return Case.from_orm(case)

async def create_document(case_id: int, document: DocumentCreate, db: Session):
    case = db.query(CaseModel).filter(CaseModel.id == case_id).first()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    new_document = DocumentModel(filename=document.filename, filepath=document.filepath, case_id=case_id)
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return Document.from_orm(new_document)
