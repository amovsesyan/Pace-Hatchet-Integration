import zipfile
import glob
import tarfile
import shutil
import os
import urllib.request
from contextlib import contextmanager
from hatchet import GraphFrame
from plotting.core import profile_timeline
@contextmanager
def temporary_change_dir(new_dir):
    original_dir = os.getcwd()  # Save the current working directory
    try:
        os.chdir(new_dir)  # Change to the new directory
        yield
    finally:
        os.chdir(original_dir)  # Revert to the original directory

class GPTL_Timing:
    def __init__(self, exp_id: int):
        self.exp_id = str(exp_id)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.join(self.base_dir, 'tmp')
        self.base_dir = os.path.join(self.base_dir, str(exp_id))
        print(self.base_dir)
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        os.chdir(self.base_dir)
        self.zip_path = self._download_zip()
        self.name = self.zip_path.split('/')[-1].removesuffix('.zip')
        print(self.name)
        print(os.path.join(self.base_dir, self.name,  'timing.*.tar.gz'))
        self._unzip_dir()
        self._untar_timing()
        self.graphframe = self._get_graphframe()
        self._delete_tmp()



    def _download_zip(self):
        url = "https://pace.ornl.gov/downloadexp/" + str(self.exp_id)
        path = os.path.join(self.base_dir, 'experiment.zip')
        urllib.request.urlretrieve(url, path)
        return path


    
    def _unzip_dir(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.name)
    
    def _untar_timing(self):
        timing_dir = glob.glob(os.path.join(self.base_dir, self.name, 'timing.*.tar.gz'))[0]
        # print(timing_dir)
        with temporary_change_dir(os.path.join(self.base_dir, self.name)):
            # print current working directory
            print(os.getcwd())
            with tarfile.open(timing_dir, 'r:gz') as tar:
                self.timing_dir = os.path.join(self.base_dir, 'extracted_timing')
                tar.extractall(self.timing_dir)
                self.timing_dir = glob.glob(os.path.join(self.timing_dir, '*'))[0]
                print(self.timing_dir)
    
    def _delete_tmp(self):
        shutil.rmtree(self.base_dir)
        # pass

    def _get_graphframe(self):
        gf = GraphFrame.from_gptl(self.timing_dir)
        # print(gf.tree(metric_column='Wallclock'))
        # print(gf.tree())
        return gf


def get_profile_timeline(exp_ids: [int], group_by: str, compare: str):
    cases = []
    for exp_id in exp_ids:
        cases.append(GPTL_Timing(exp_id))
    intersect: GraphFrame = GraphFrame.intersect([case.graphframe for case in cases], [case.exp_id + ' ' for case in cases])
    compared_columns = [str(case.exp_id) + ' ' + compare for case in cases]
    p1 = profile_timeline(intersect, group_by, compared_columns)
    return p1

