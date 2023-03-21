import time

from pathlib import Path
from multiprocessing.pool import ThreadPool
from tqdm.auto import tqdm

from util import (
    convert_pdf2img,
)


def main():
    pdf_dir = Path(__file__).parent/'raw_pdf_100/'
    path_pdfs = list(pdf_dir.glob("*.pdf"))
    png_dir = Path("pdf2png")
    png_dir.mkdir(exist_ok=True, parents=True)
    for p in tqdm(path_pdfs):
        convert_pdf2img(p, png_dir, dpi=300)


if __name__ == "__main__":
    import cProfile
    import pstats

    timestr = time.strftime("%Y%m%d-%H%M%S")

    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(f'profiling_eval_{timestr}.prof')
