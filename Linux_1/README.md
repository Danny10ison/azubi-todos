# Linux basics
The objective of this project is to create a Movie-Record System on a Linux operating system and utilize Git and GitHub for version control. By following the instructions below, students will gain hands-on experience in Linux file management, Git versioning, and repository setup.
- Install a Linux operating system of their choice on a virtual machine or on own computer.
- Use your knowledge of Linux file types and hierarchy to create a Movie-record system. A folder that will contain 2 sub-directories (movies & series)
- The sub-directories would then contain movie-series names e.g. moviex, seriesy...
- Use basic Linux commands and file navigations to create, edit, move, and delete files and directories in your Movie-record system.
- Create a GitHub repository to store your Movie-record system and version your changes.
- Use Git to push and pull changes to and from your GitHub repository.


```
Movie-Record-System/
├── movies/
│   ├── moviex/
│   │   ├── movie_x1.txt
│   │   ├── movie_x2.txt
│   │   └── ...
│   ├── moviey/
│   │   ├── movie_y1.txt
│   │   ├── movie_y2.txt
│   │   └── ...
│   └── ...
└── series/
    ├── seriesa/
    │   ├── series_a1.txt
    |   ├── series_a2.txt
    |   └── ...
    ├── seriesb/
    │   ├── series_b1.txt
    │   ├── series_b2.txt
    │   └── ...
    └── ...
```

## Commands
```bash
$ mkdir Movie-Record-System # create directory

$ mkdir -p Movie-Record-System/movies/movie{x,y} # create parent directory and subdirectories all at once

$ mkdir -p Movie-Record-System/series/series{a,b} # create parent directory and subdirectories all at once

$ touch Movie-Record-System/movies/moviex/movie_x{1..3}.txt

$ touch Movie-Record-System/movies/moviey/movie_y{1..3}.txt

$ touch Movie-Record-System/series/seriesa/series_a{1..3}.txt

$ touch Movie-Record-System/series/seriesb/series_b{1..3}.txt
som
$ tree Movie-Record-System/ # display folder structure using tree command

Movie-Record-System/
├── movies
│   ├── moviex
│   │   ├── movie_x1.txt
│   │   ├── movie_x2.txt
│   │   └── movie_x3.txt
│   └── moviey
│       ├── movie_y1.txt
│       ├── movie_y2.txt
│       └── movie_y3.txt
└── series
    ├── seriesa
    │   ├── series_a1.txt
    │   ├── series_a2.txt
    │   └── series_a3.txt
    └── seriesb
        ├── series_b1.txt
        ├── series_b2.txt
        └── series_b3.txt

6 directories, 12 files
```
