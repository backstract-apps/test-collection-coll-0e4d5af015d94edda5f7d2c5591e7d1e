from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - test-collection-coll-0e4d5af015d94edda5f7d2c5591e7d1e',debug=False,docs_url='/ecstatic-montalcini-a201e522a02711ef98050242ac12000480/docs',openapi_url='/ecstatic-montalcini-a201e522a02711ef98050242ac12000480/openapi.json')

app.include_router(router, prefix='/ecstatic-montalcini-a201e522a02711ef98050242ac12000480/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()