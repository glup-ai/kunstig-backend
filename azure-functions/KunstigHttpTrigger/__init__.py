import azure.functions as func
from . import generate
from . import cms
import torch

models_dict = cms.get_models()
device = torch.device('cpu')

def main(req: func.HttpRequest) -> func.HttpResponse:
    generate.load_models(models_dict, device)
    
    req_body = req.get_json()

    model_name = req_body.get("model")

    if not model_name or not model_name in models_dict:
        return func.HttpResponse(f"Nope.")

    input_string = req.params.get("inputString")

    img = generate.generate_images(models_dict[model_name]["model"], device, input_string)

    func.HttpResponse.mimetype = 'image/jpeg'
    return func.HttpResponse(img, status_code=200)
