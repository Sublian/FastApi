from fastapi import APIRouter, HTTPException

router = APIRouter(prefix= "/products", tags=["products"], responses= {404: {"message": "No encontrado"}})
# inicia el server: uvicorn products:app --reload

products_list = ["Producto 0","Producto 1",
                 "Producto 2","Producto 3",
                 "Producto 4","Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]

# agregamos un producto
@router.post("/",response_model=str, status_code=201)                   
async def product(product: str):
    if type(search_product(product))==product:
        #con esta linea generamos una excepcion de status_code con detalles
        raise HTTPException(status_code = 404, detail="El producto ya existe")
            
    products_list.append(product)            
    return product

# funciones
def search_product(product: str):
    users = filter(lambda product: product == products_list)
    try:        
        return list(product)[0]
    except:
        return {"error": "No existe ese producto"}