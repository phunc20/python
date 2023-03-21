import asyncio
import time

from pathlib import Path
from tqdm.auto import tqdm

from util import (
    save_image,
    pdf2buffer,
)


async def main():
    #print('Start')
    start = time.perf_counter()
    pdf_dir = Path(__file__).parent/'raw_pdf_100/'
    path_pdfs = list(pdf_dir.glob("*.pdf"))
    png_dir = Path("pdf2png")
    png_dir.mkdir(exist_ok=True, parents=True)
    batchsize = 8
    n_batches = len(path_pdfs) // batchsize + (len(path_pdfs) % batchsize > 0)
    for i in tqdm(range(n_batches)):
        print(f'Buffering batch-{i+1}/{n_batches}')
        batch = path_pdfs[i*batchsize:(i+1)*batchsize]
        print(f'{batch = }')
        filename2buffer = pdf2buffer(batch, dpi=300)
        #import ipdb; ipdb.set_trace()
        print(f'Saving batch-{i+1}/{n_batches}')
        tasks = [
            asyncio.create_task(
                save_image(
                    png_dir/filename,
                    buffer.getbuffer(),
                )
            ) for filename, buffer in filename2buffer.items()]
        done, pending = await asyncio.wait(tasks)

    end = time.perf_counter()
    print('End')
    print(f'took {end-start:.2f}s')


if __name__ == "__main__":
    import cProfile
    import pstats

    timestr = time.strftime("%Y%m%d-%H%M%S")

    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(main())
    pr.disable()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(f'profiling_eval_{timestr}.prof')
