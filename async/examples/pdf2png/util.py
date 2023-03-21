from __future__ import annotations

import asyncio
import os
import aiofiles
import time
from io import BytesIO
from pathlib import Path

import cv2
import fitz
import numpy as np
from tqdm.auto import tqdm


def convert_pdf2img(
    pdf_path, output_dir, *args,
    dpi=None, zoom=None, zoom_x=1.28, zoom_y=1.28,
):
    if isinstance(zoom, (int, float)):
        zoom_x = zoom
        zoom_y = zoom

    pdf_stem = Path(pdf_path).stem
    matrix = fitz.Matrix(zoom_x, zoom_y)
    resolution = (1500, 1500)

    with fitz.open(pdf_path) as doc:
        for idx, page in enumerate(doc):
            if dpi is not None:
                pix = page.get_pixmap(
                    dpi=dpi,
                )
            else:
                pix = page.get_pixmap(
                    matrix=matrix,
                )

            if len(doc) > 1:
                save_to = output_dir/f'{pdf_stem}_page{idx}.png'
            else:
                save_to = output_dir/f'{pdf_stem}.png'

            pix.pil_save(
                str(save_to),
                optimize=True,
                dpi=resolution,
            )


# https://stackoverflow.com/questions/70306307/python-how-can-i-asynchronously-save-the-pil-images
async def save_image(path: str, image: memoryview) -> None:
    async with aiofiles.open(path, "wb") as file:
        file.write(image)


async def pdf2png(
    pdf_path, output_dir, *args,
    dpi=None, zoom_x=1.28, zoom_y=1.28,
):
    pdf_stem = Path(pdf_path).stem
    matrix = fitz.Matrix(zoom_x, zoom_y)
    resolution_parameter = None
    resolution = (1500, 1500)

    with fitz.open(pdf_path) as doc:
        tasks = []
        for idx, page in enumerate(doc):
            if dpi is not None:
                pix = page.get_pixmap(
                    dpi=dpi,
                )
            else:
                pix = page.get_pixmap(
                    matrix=matrix,
                )

            if len(doc) > 1:
                save_to = output_dir/f'{pdf_stem}_page{idx}.png'
            else:
                save_to = output_dir/f'{pdf_stem}.png'

            buffer = BytesIO()
            pix.pil_save(
                buffer,
                optimize=True,
                dpi=resolution,
                format="PNG",
            )
            #await save_image(save_to, buffer.getbuffer())
            tasks.append(asyncio.create_task(
                save_image(save_to, buffer.getbuffer())
            ))

        #done, pending = await asyncio.wait(tasks)
        return tasks


def seq_count_pages(pdf_dir):
    start = time.perf_counter()
    path_pdfs = pdf_dir.glob("*.pdf")
    n_pages = 0
    for p in path_pdfs:
        with fitz.open(p) as doc:
            n_pages += len(doc)

    end = time.perf_counter()
    print(f'(seq) took {end-start:.2f}s')
    return n_pages


async def read_pdf(path_pdf):
    async with aiofiles.open(path_pdf, "rb") as file:
        content = await file.read()
    return content


async def async_count_pages(pdf_dir):
    start = time.perf_counter()
    path_pdfs = pdf_dir.glob("*.pdf")
    tasks = [asyncio.create_task(read_pdf(p)) for p in path_pdfs]
    done, pending = await asyncio.wait(tasks)
    n_pages = 0
    for task in done:
        mem_area = task.result()
        with fitz.open(stream=mem_area, filetype="pdf") as doc:
            n_pages += len(doc)

    end = time.perf_counter()
    print(f'(async) took {end-start:.2f}s')
    return n_pages


def pdf2buffer(
    path_pdfs, *args,
    dpi=None, zoom_x=1.28, zoom_y=1.28,
):
    matrix = fitz.Matrix(zoom_x, zoom_y)
    resolution_parameter = None
    resolution = (1500, 1500)

    filename2buffer = {}
    for pdf_path in tqdm(path_pdfs):
        pdf_stem = Path(pdf_path).stem
        with fitz.open(pdf_path) as doc:
            for idx, page in enumerate(doc):
                if dpi is not None:
                    pix = page.get_pixmap(
                        dpi=dpi,
                    )
                else:
                    pix = page.get_pixmap(
                        matrix=matrix,
                    )

                if len(doc) > 1:
                    filename = f'{pdf_stem}_page{idx}.png'
                else:
                    filename = f'{pdf_stem}.png'

                buffer = BytesIO()
                pix.pil_save(
                    buffer,
                    optimize=True,
                    dpi=resolution,
                    format="PNG",
                )
                filename2buffer[filename] = buffer

    return filename2buffer
