def __init__(self, generate_frame=20):
# 原始爱心坐标集合
self._points = set()  
# 边缘扩散效果点坐标集合
self._edge_diffusion_points = set()  
# 中心扩散效果点坐标集合
self._center_diffusion_points = set()  
# 每帧动态点坐标
self.all_points = {}  
self.build(2000)
self.random_halo = 1000
self.generate_frame = generate_frame
for frame in range(generate_frame):
 self.calc(frame)

def build(self, number):
for _ in range(number):
 t = random.uniform(0, 2 * pi)
 x, y = heart(t)
 self._points.add((x, y))
# 爱心内扩散
for _x, _y in list(self._points):
 for _ in range(3):
  x, y = scatter_inside(_x, _y, 0.05)
  self._edge_diffusion_points.add((x, y))
# 爱心内再次扩散
point_list = list(self._points)
for _ in range(4000):
 x, y = random.choice(point_list)
 x, y = scatter_inside(x, y, 0.17)
 self._center_diffusion_points.add((x, y))

@staticmethodstaticmethod
def calc_position(x, y, ratio):
force = 1 / (((x - X) ** 2 +
     (y - Y) ** 2) ** 0.520)
dx = ratio * force * (x - X) + random.randint(-1, 1)
dy = ratio * force * (y - Y) + random.randint(-1, 1)
return x - dx, y - dy

def calc(self, generate_frame):
ratio = 10 * curve(generate_frame / 10 * pi)
halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
halo_number = int(
 3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
all_points = []
# 光环
heart_halo_point = set()
for _ in range(halo_number):
 t = random.uniform(0, 2 * pi)
 x, y = heart(t, shrink_ratio=11.6)
 x, y = shrink(x, y, halo_radius)
 if (x, y) not in heart_halo_point:
  heart_halo_point.add((x, y))
  x += random.randint(-14, 14)
  y += random.randint(-14, 14)
  size = random.choice((1, 2, 2))
  all_points.append((x, y, size))
# 轮廓
for x, y in self._points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 3)
 all_points.append((x, y, size))
# 内容
for x, y in self._edge_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
for x, y in self._center_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
