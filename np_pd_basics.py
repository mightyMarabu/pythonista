# read las-file (liblas)
from liblas import file as lf
las = lf.File('/data/job461230_20156_72_90.las', mode='r')


# numpy array (incl liblas.point)
las_nparray = [[p.x, p.y, p.z] for p in lf.File('/data/job461230_20156_72_90.las', mode='r')]

# pandas dataframe
las_df = pd.DataFrame([[p.x, p.y, p.z] for p in lf.File('/data/job461230_20156_72_90.las', mode='r')], columns = ["x", "y", "z"])

# triangulation las pointcloud with scipy.spatual module
las_tri = Delaunay(las_nparray)
