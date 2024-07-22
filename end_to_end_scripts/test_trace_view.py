from hatchet import GraphFrame
from helper_functions import GPTL_Timing
from plotting.core import profile_trace_view

if __name__ == '__main__':
    loc_1 = '/home/alex/Downloads/exp-ac.ngmahfouz-183250.zip'
    loc_2 = '/home/alex/Downloads/exp-ac.ngmahfouz-183252.zip'
    case_1 = GPTL_Timing(loc_1)
    gf = case_1.graphframe
    profile_trace_view(gf)
    # case_2 = GPTL_Timing(loc_2)
    # intersect: GraphFrame = GraphFrame.intersect([case_1.graphframe, case_2.graphframe], [case_1.name + ' ', case_2.name + ' '])
    # p1 = profile_timeline(intersect, 'name', [case_1.name + ' max (inc)', case_2.name + ' max (inc)' ])
    # return p1