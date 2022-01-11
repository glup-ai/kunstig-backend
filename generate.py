"""Generate images using pretrained network pickle."""

from io import BytesIO
import random
import numpy as np
import PIL.Image
import torch

import legacy
import dnnlib


def generate_images(G, device, input_string):
    label = torch.zeros([1, G.c_dim], device=device)

    # Generate images.
    if input_string:
        seed = generate_seed(input_string)
    else:
        seed = random.randint(1, 1000)

    z = torch.from_numpy(np.random.RandomState(seed).randn(1,
                                                           G.z_dim)).to(device)

    img = G(z, label, truncation_psi=1, noise_mode='const', force_fp32=True)
    img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
    image = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')
    image_byte_array = BytesIO()
    image.save(image_byte_array, format="PNG")
    inference_result = image_byte_array.getvalue()
    return inference_result


def load_model(url, device):

    print('Loading networks from "%s"...' % url)
    with dnnlib.util.open_url(url) as f:
        G = legacy.load_network_pkl(f)['G_ema'].to(device)
        return G


def generate_seed(input_string):
    print(input_string)
    seed_size_limit = 2**32 - 1
    seed = hash(input_string) % seed_size_limit
    print(seed)
    return seed