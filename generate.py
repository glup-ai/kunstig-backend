"""Generate images using pretrained network pickle."""

from io import BytesIO
import random
import numpy as np
import PIL.Image
import torch

import legacy
import dnnlib

def generate_images(network_pkl: str):
    print('Loading networks from "%s"...' % network_pkl)
    device = torch.device('cpu')
    with dnnlib.util.open_url(network_pkl) as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device) # type: ignore

    label = torch.zeros([1, G.c_dim], device=device)

    # Generate images.
    seed = random.randint(1, 1000)
    z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
    img = G(z, label, truncation_psi=1, noise_mode='const', force_fp32=True)
    img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
    image = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')
    image_byte_array = BytesIO()
    image.save(image_byte_array, format="PNG")
    inference_result = image_byte_array.getvalue()
    return inference_result
