from min_dalle import MinDalle
import argparse
import torch
import numpy
from PIL import Image
import time
import os
import tqdm

#take arguments for seed and model
parser = argparse.ArgumentParser()
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--seeds', type=int, default=0)
parser.add_argument('--grid', type=int, default=1)
parser.add_argument('--model', type=int, default=2)
parser.add_argument('--text', type=str, default="Infinite chaos in a void")
args = vars(parser.parse_args())


def main():
    models = {0: torch.float32, 1: torch.float16, 2: torch.bfloat16}

    model = MinDalle(
        models_root='./pretrained',
        dtype=models[args['model']],
        device='cuda',
        is_mega=True,
        is_reusable=True
    )

    temp_time = time.time()

    if not os.path.exists(args['text']):
        os.makedirs(args['text'])

    if not int(args["seeds"]) == 0:
        for i in tqdm.tqdm(range(int(args["seeds"]))):
            image = model.generate_images(
                text=args["text"],
                seed=i,
                temperature=1,
                top_k=256,
                supercondition_factor=32,
                is_verbose=False,
            )
            images = image.to('cpu').numpy()
            image_out = Image.fromarray(images[0])
            image_out.save(f"./{args['text']}/mindalle_{temp_time}_{i}.png")
    else:
        image = model.generate_images(
            text=args["text"],
            seed=args["seed"],
            temperature=1,
            top_k=256,
            supercondition_factor=32,
            is_verbose=False
        )
        images = image.to('cpu').numpy()
        image_out = Image.fromarray(images[0])
        image_out.save(f"./{args['text']}/mindalle_{temp_time}_{args['seed']}.png")


if __name__ == "__main__":
    main()