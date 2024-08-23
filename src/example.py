from gptl_timing import get_profile_timeline, get_operation_histogram, get_profile_trace_view
from plotting._util import show
if __name__ == '__main__':
    # p = get_operation_histogram([177089, 178145], 'name', 'wallmax (inc)')
    # p = get_profile_timeline([177089, 178145], 'name', 'wallmax (inc)')
    p = get_profile_trace_view(177089, 'wallmax (inc)', 0.02)
    show(p)