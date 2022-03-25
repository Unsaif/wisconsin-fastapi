from sqlalchemy.orm import Session
from . import models, schemas

def get_subject_demos(db: Session):
    return db.query(models.Demographics).all()

def get_metabolite(db: Session, metabolite: str):
    print(metabolite)
    return db.query(models.Diet).filter(models.Diet.metabolite == metabolite).first()

def get_species(db: Session, species: str):
    return db.query(models.Abundance).filter(models.Abundance.species == species).first()

def create_subject(db: Session, subject: schemas.Demo):
    db_item = models.Demographics(**subject.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_metabolite(db: Session, metabolite: schemas.Diet):
    db_item = models.Diet(**metabolite.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_species(db: Session, species: schemas.Abundance):
    db_item = models.Abundance(**species.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item