import time
from functools import partial
from pathlib import Path
from multiprocessing import Pool
from tqdm.auto import tqdm

from util import (
    convert_pdf2img,
)

pdf_dir = Path(__file__).parent/'raw_pdf_100/'
path_pdfs = list(pdf_dir.glob("*.pdf"))
png_dir = Path("pdf2png")
png_dir.mkdir(exist_ok=True, parents=True)
#convert = partial(convert_pdf2img, png_dir, dpi=300)
def convert(path_pdf):
    convert_pdf2img(path_pdf, png_dir, dpi=300)


def main():
    print('Start')
    start = time.perf_counter()
    with Pool() as pool:
        ## Unsuccessful tqdm code
        #tasks = tqdm(
        #    #pool.imap(
        #    #pool.imap_unordered(
        #    pool.map(
        #        convert,
        #        path_pdfs,
        #        #chunksize=5,
        #    ),
        #    total=len(path_pdfs),
        #)

        tasks = pool.map(
            convert,
            path_pdfs,
            #chunksize=10,
        )

    end = time.perf_counter()
    print('End')
    print(f'took {end-start:.2f}s')


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
