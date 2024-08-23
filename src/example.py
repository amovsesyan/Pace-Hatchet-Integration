from gptl_timing import get_profile_timeline
from plotting._util import show
if __name__ == '__main__':
    p = get_profile_timeline([177089, 178145], 'name', 'wallmax (inc)')
    show(p)