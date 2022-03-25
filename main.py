from fastapi import FastAPI, Depends, HTTPException
from wisonsin_database import schemas, models, crud
from wisonsin_database.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/demo', response_model=list[schemas.Demo])
async def demo(db: Session = Depends(get_db)):
    subject_demos = crud.get_subject_demos(db)
    return subject_demos

@app.get('/diet/{metabolite}', response_model=schemas.Diet)
async def diet(metabolite: str, db: Session = Depends(get_db)):
    db_metabolite = crud.get_metabolite(db, metabolite=metabolite)
    if db_metabolite is None:
        raise HTTPException(status_code=404, detail="Metabolite not found")
    return db_metabolite

@app.get('/abundance/{species}', response_model=schemas.Abundance)
async def abundance(species: str, db: Session = Depends(get_db)):
    db_species = crud.get_species(db, species=species)
    if db_species is None:
        raise HTTPException(status_code=404, detail="Species not found")
    return db_species

# not for production

# @app.post('/demo', response_model=schemas.Demo)
# def create_subject(subject: schemas.Demo, db: Session = Depends(get_db)):
#     return crud.create_subject(db=db, subject=subject)

# @app.post('/metabolite', response_model=schemas.Diet)
# def create_metabolite(metabolite: schemas.Diet, db: Session = Depends(get_db)):
#     return crud.create_metabolite(db=db, metabolite=metabolite)

# @app.post('/species', response_model=schemas.Abundance)
# def create_species(species: schemas.Abundance, db: Session = Depends(get_db)):
#     return crud.create_species(db=db, species=species)
