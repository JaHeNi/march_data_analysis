from utils import read_gpx_file

def main():

    b = [[94.36, 148.46],
    [87.31, 135.61],
    [96.44, 150.72],
    [98.18, 142.53],
    [104.15, 144.65],
    [106.09, 150.20]]
    
    read_gpx_file("./data/echo.gpx")
    
if __name__ == "__main__":
    main()