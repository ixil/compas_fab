import System

o = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIlSURBVEhL7VM7aFRREN0mYqWIYLHkztzPW5UVQVw/+CNoYZNGC1EsRfxWFoIKQgqxUBDRThS0kbSJJqKCjSgIKdIFf6AWUQSttLCKZ+47q9n1hY1dihwYHnPmP3debRELH2vr9ZXJ+bGkfqa36Jvo4iaG9gYCds8Kvh5Uj0BOJpHTbSlUTxkP+wX4TZtvVD3HFHMjpeTMOTj/jNS8wEIzhYQDpKqBLkaCk19U/wtB/CMU+Vl4v5fUX6xxri4iKyw5ujmfnFuHYrei+EuQy+CuJAlHY4zLGfIPkHjApkji75MqgXW8LA2yEd/vQWQQ+72RuQqxogztAIqvos8EKSRX/y4Hqe43nQkuZmMXms3mEtiulf7+Nuk/sEtirtHsjI7vGmHroY8VfAFummolsK59THSCVAbO+o7xyfuDNZzZmezU1W0IYQuDr5KqBNY4jEIPqJo+yHxnMwHj81ytPxWZmIXo/XGz4R3e2upCf1iPaVv4bm54v9V0NLIaK9kZRfbA9yH97zFF3vWEkfYwpDqAhNth/2Y+VWLXVl5cqXevy+79Jg2HSFXC3gdd7sDE26x767ohEhuqG2y6qg1kFCJNPMoUdveJ1LxRFMUyxH3FvR8jVQ37mfKIIq9I9YR1XE7uf6jqUtJzI7iwq73H5GQSXzyYPoE8bQtW9BjTjsP+gQ29timYojdarVYfEg3hH3iPRJ9zok75CPkCmcSlHGbYIhY0arXfMz6/PVGPpY0AAAAASUVORK5CYII="
ros_connect_icon = System.Drawing.Bitmap(System.IO.MemoryStream(System.Convert.FromBase64String(o)))

o = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAATNSURBVEhLlZV7TNtVFMcvhjDNxlS2OZ/DxT+UxemM7yBz0RkXzUb8AxNjdBNjFJ1sU+cG5VFwY7w2ZDwV3VRCwEWUMbdS+qDl2fJoYWyM8WYFyruUN6X0672/3koLBOcnOcnvd+79nXvuef3IfxJY4ElEJbtJmOIoEStT3KJU6UQsTyah8sMkRO5H9lxZw3f+T77+25tEqc54p1YbAi62I6bOhNz2GUh655HdNo2omlHs++MmHjiraSORajH58vdN/MvbIFx+cGua1hSjM6NjYgGr0TRmxXHNCDYnV/cQUfF73MIqiBVZewtvocVs5SbsLNhsCFO2Y+v3FUjRGrh2kbphC17JawV1LppbWoEIWVagchCWFZwenbYIxt3ECjz7YzWsCza+sohpzoa3qXMkrDiSW3QiojjoA5mRb10Ou8HzWdVYc0KJt3LquXY59Ay8md9ObyLdyy0T8lBsycMe0erJwMttGJic41td+VnXB580DdRdJjxyphyy9hG+4kqXaRr7/myFu1hx66nf6tcKB2yIUyXtKejGxvhSbEooFWJssS6GwDw7jwdPl+MnXa/wznKxPUMDK72Vg/FZK6LVnVgbo4J3Ujlez++CZ4wqmJDPL6zbklg+OEgdvzE0Bf/cBhpDGXZkanHp5pDw8dHiVjxH4+5gymKlRiqQXmNPdnaDEY+drQSJkOPDv66jxzyL62YbvE6qrxLyjWT3u4XtwkYHBc1DeJQmNLKkA8aJOaw/pUalYYyv2sm71o/7E8swM7+AAwVN2J6ugbJzlK/SnFHZea7ORkho8bE4vevHjEnqJcM/rwHv51/DPK0aR36YhyzpO8/X4pCkBSxSziF1EKwygpBIWWpexwxXuSLvGMU9sWqM0BINkbfRPJThW1kr7o5VIYvmo3l4CutOqdBMQ7sSifVjIG5RisxCg4WrFmEJfJJeW6zqEN7Luk3Y9YtOiDO7VX3/hKBn4XkjWy88LyW1cZzdQHo2h86YpSRrDEIeWEIdFLWNgIRIUW+0G2f0TczCK06Ni82DXLMICz0hx6Vfnag1cZWdxoEJbKFVUsiryEELDcknhTeExDtD5yG20R7pHnN1NEjRSw84fMnPP7+FqyDUMq1fPJ2hhZ56qjOO/yuNA5PoNM3gKg2PQ6enUt49JpQt66PM2h7BzjyVF7LqrITsP3/n5sRSQ/eUvQp80qpwR5QCG+jmJ1Kr8DiTFLuwd+apoOc6YZ3KvTRMJFKO137VCXaqhqy06Uq0QicTkUws0tprmDXNDup9fEU3hqYsggw7Caso53e2zsr3mKwNz9DmlLQOC3Y+onONhEoP2A84UuS1MaFisNHkOqKXojGY8WJWjVCeqyHvteCuk4omEnDBw34AQ1Qc4EvnudmyvGEcFNIOJ+EyVC3pamcMkwvw+UHPqs2XW3ZCVBTN5vno7MqHXG4Zhsd3Smh7zFzjSteEFb659KcTKvmMW1yBcJn4pZxmlA8sH9urHXDFMIttGbU2GokgbmkVQqXveCVpWw+qB1E9NA9HZkrpv8A9WilMXQb7uaiMFuyX9cEzoVJPRJJd3MJtQMc4iVAd8jpdqfOjU/GIuh+fKoy4L60BweoBfKHsxcvn9Jb18RVlJEL5MXk10p1/6QQh/wBQQTKbAO90IQAAAABJRU5ErkJggg=="
default_icon = System.Drawing.Bitmap(System.IO.MemoryStream(System.Convert.FromBase64String(o)))