# Simple example
import rhino3dm
center = rhino3dm.Point3d(1,2,3)
arc = rhino3dm.Arc(center, 10, 1)
nc = arc.ToNurbsCurve()
start = nc.PointAtStart
points = nc.Points
print("printing {}".format('start'))
print(start)

#print("printing {}".format('arc'))
#print(arc)
#
#print("printing {}".format('nc'))
#print(nc)

print("printing {}".format('points'))
print(len(points))

for i in range(len(points)):
  pt = points[i].Encode()
  print("xyzw = {} {} {} {}".format(pt['X'], pt['Y'],
    pt['Z'], pt['W']))
  #print("xyzw = {}".format(pt))
