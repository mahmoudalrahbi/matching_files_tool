# Matching files tool
Usually, when we want to train a deep learning model, we need a lot of data and a lot of files. For example, if yx`ou want to train the YOLO model, you need image files and XML files that describe the labeled objects in every picture. So it necessary to make sure that every XML file in your dataset has a corresponding image. Matching files tool come to help you to manage these files.

Matching files tool aims to help in finding files that not have a corresponding file and delete it or copy the files which have a corresponding file.

## Getting Started

For example, if you want to know which images in the below picture does not have a corresponding XML file.
![files](https://user-images.githubusercontent.com/44264942/71631106-41a30600-2c20-11ea-922f-25e6c430b881.PNG)

You can do that by using this tool by simply writing this command:
```bash
python main.py -dir1 D:\d1 -ext1 xml -dir2 D:\d2 -ext2 jpg
```
where:

```-dir1 D:\d1```: specify the path of the first directory (in this case D:\d1).

```-ext1 xml```: specify the type of files that are in the first directory( e.g xml). 

```-dir2 D:\d2```: specify the path of the second directory (in this case D:\d2).
 
```-ext2 jpg```: specify the type of files that are in the second directory( e.g jpg). 

The result of the above command should be the same as this:
![ouput_crossponding](https://user-images.githubusercontent.com/44264942/71631540-9a739e00-2c22-11ea-9295-0e4442a6e0f2.PNG)

### Delete files with no matching:
You can delete files which not have a matching file by this command:
```bash
python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -delete_dir1
```
``` -delete_dir1```: to delete files from dir1.

You can replace it by :

``` -delete_dir2```: to delete files from dir2.

``` -delete_both```: to delete files from both directories (dir1 and dir2).

### Copy files which have a match:

You can copy files which have corresponding files to a specific directory.
```bash
python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -copy_dir1 d3
```

where:

```-copy_dir1 d3```: copy files which have corresponding files from dir1 into a destination (in this case d3)

You can replace it by :

```-copy_dir1 path```: copy files which have corresponding files from dir2 into a destination(path).

```-copy_both path```: copy files which have corresponding files from both directories (dir1 and dir2) into a destination(path).

## Authors
•	Mahmoud Said ALRahbi. [mahmoudalrahbi](https://github.com/mahmoudalrahbi)

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.





