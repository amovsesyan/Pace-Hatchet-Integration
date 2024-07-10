import zipfile
import glob
import tarfile
import shutil
import hatchet
from hatchet import GraphFrame
from hatchet.plotting.core import operation_histogram, profile_timeline

class GPTL_Timing:
    def __init__(self, location: str):
        self.location = location
        self.name = location.split('/')[-1].removesuffix('.zip')
        self._unzip_dir()
        self._untar_timing()
        self.graphframe = self._get_graphframe()

    
    def _unzip_dir(self):
        with zipfile.ZipFile(self.location, 'r') as zip_ref:
            zip_ref.extractall('./tmp/' + self.name)
    
    def _untar_timing(self):
        timing_dir = glob.glob('./tmp/' + self.name + '/timing.*.tar.gz')[0]
        # print(timing_dir)
        with tarfile.open(timing_dir, 'r:gz') as tar:
            tar.extractall('./tmp/timing')
            self.timing_dir = glob.glob('./tmp/timing/*')[0]
            # print(self.timing_dir)
    
    def _delete_tmp(self):
        shutil.rmtree('./tmp/' + self.name)

    def _get_graphframe(self):
        gf = GraphFrame.from_gptl(self.timing_dir)
        # print(gf.tree(metric_column='Wallclock'))
        return gf
        
# def unzip_dir(zip_file: str):

#     with zipfile.ZipFile(zip_file, 'r') as zip_ref:
#         zip_ref.extractall()

if __name__ == '__main__':
    loc_1 = '/home/alex/Downloads/exp-ac.ngmahfouz-183250.zip'
    loc_2 = '/home/alex/Downloads/exp-ac.ngmahfouz-183252.zip'
    case_1 = GPTL_Timing(loc_1)
    case_2 = GPTL_Timing(loc_2)
    intersect: GraphFrame = GraphFrame.intersect([case_1.graphframe, case_2.graphframe], [case_1.name + ' ', case_2.name + ' '])
    print(intersect.dataframe)

    profile_timeline(intersect, 'name', [case_1.name + ' max (inc)', case_2.name + ' max (inc)' ])
    operation_histogram(intersect, 'name', [case_1.name + ' max (inc)', case_2.name + ' max (inc)' ])
    

    # gptl.unzip_dir()
    # gptl.untar_timing()
    # gptl.get_graphframe()
    # gptl.delete_tmp()